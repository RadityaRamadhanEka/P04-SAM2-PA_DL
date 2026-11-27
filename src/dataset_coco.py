"""Generate deterministic COCO val2017 validation/test splits and p1 points for P04 (SAM 2)."""

from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np
from pycocotools.coco import COCO


def compute_interior_point(gt_mask: np.ndarray) -> tuple[int, int]:
    """Return deterministic interior (x, y) maximizing Euclidean distance to mask boundary."""
    if gt_mask.ndim != 2 or not gt_mask.any():
        raise ValueError("gt_mask must be a non-empty 2D boolean mask.")

    padded = np.pad(gt_mask.astype(np.uint8), pad_width=1, mode="constant", constant_values=0)
    dist = cv2.distanceTransform(padded, cv2.DIST_L2, 5)[1:-1, 1:-1]
    y, x = np.unravel_index(int(np.argmax(dist)), dist.shape)
    if not gt_mask[y, x]:
        ys, xs = np.nonzero(gt_mask)
        y, x = int(ys[0]), int(xs[0])
    return int(x), int(y)


def _collect_samples(
    coco: COCO,
    image_ids: list[int],
    grouped_anns: dict[int, list[dict]],
    categories: dict[int, str],
    target_count: int,
    max_per_image: int,
) -> tuple[list[dict], int]:
    """Collect up to target_count valid object samples sequentially across image_ids."""
    samples: list[dict] = []
    idx = 0
    while idx < len(image_ids) and len(samples) < target_count:
        img_id = image_ids[idx]
        idx += 1
        img_info = coco.imgs[img_id]
        taken = 0
        for ann in grouped_anns[img_id]:
            if taken >= max_per_image or len(samples) >= target_count:
                break
            gt_mask = coco.annToMask(ann).astype(bool)
            pixel_count = int(np.count_nonzero(gt_mask))
            if pixel_count == 0:
                continue
            p1_x, p1_y = compute_interior_point(gt_mask)
            samples.append(
                {
                    "image_id": int(img_id),
                    "ann_id": int(ann["id"]),
                    "p1_x": p1_x,
                    "p1_y": p1_y,
                    "category_id": int(ann["category_id"]),
                    "category_name": categories[int(ann["category_id"])],
                    "file_name": str(img_info["file_name"]),
                    "area": float(ann["area"]),
                    "mask_pixels": pixel_count,
                }
            )
            taken += 1
    return samples, idx


def _validate_splits(
    coco: COCO,
    val_samples: list[dict],
    test_samples: list[dict],
) -> None:
    """Verify split disjointness, uniqueness, and strict p1 containment in ground truth."""
    if not val_samples or not test_samples:
        raise RuntimeError("Both val_samples and test_samples must be non-empty.")

    val_images = {s["image_id"] for s in val_samples}
    test_images = {s["image_id"] for s in test_samples}
    if val_images & test_images:
        raise AssertionError("Data leakage detected: overlapping image_id between val and test.")

    seen_anns: set[int] = set()
    for split_name, split in (("val", val_samples), ("test", test_samples)):
        for s in split:
            ann_id = int(s["ann_id"])
            image_id = int(s["image_id"])
            if ann_id in seen_anns:
                raise AssertionError(f"Duplicate ann_id {ann_id} across splits.")
            seen_anns.add(ann_id)

            ann = coco.anns[ann_id]
            if int(ann["image_id"]) != image_id:
                raise AssertionError(f"Mismatched image_id for ann_id={ann_id} in {split_name}.")

            gt = coco.annToMask(ann).astype(bool)
            x, y = int(s["p1_x"]), int(s["p1_y"])
            if not (0 <= x < gt.shape[1] and 0 <= y < gt.shape[0] and gt[y, x]):
                raise AssertionError(f"p1=({x}, {y}) outside ground truth for ann_id={ann_id}.")


def generate_splits(
    annotations_path: Path,
    out_dir: Path,
    n_val: int = 100,
    n_test: int = 300,
    min_area: float = 1024.0,
    max_per_image: int = 3,
    seed: int = 42,
) -> dict:
    """Create and save samples_val.json, samples_test.json, and split_metadata.json."""
    coco = COCO(str(annotations_path))
    categories = {int(cat["id"]): str(cat["name"]) for cat in coco.dataset.get("categories", [])}

    grouped_anns: dict[int, list[dict]] = defaultdict(list)
    for ann in coco.anns.values():
        if int(ann.get("iscrowd", 0)) == 0 and float(ann.get("area", 0.0)) >= min_area:
            grouped_anns[int(ann["image_id"])].append(ann)

    for img_id in grouped_anns:
        grouped_anns[img_id].sort(key=lambda a: int(a["id"]))

    eligible_image_ids = sorted(grouped_anns.keys())
    rng = random.Random(seed)
    rng.shuffle(eligible_image_ids)

    val_samples, next_idx = _collect_samples(
        coco, eligible_image_ids, grouped_anns, categories, n_val, max_per_image
    )
    test_samples, _ = _collect_samples(
        coco, eligible_image_ids[next_idx:], grouped_anns, categories, n_test, max_per_image
    )

    if len(val_samples) < n_val or len(test_samples) < n_test:
        raise RuntimeError(
            f"Insufficient eligible objects: got val={len(val_samples)}/{n_val}, "
            f"test={len(test_samples)}/{n_test}."
        )

    _validate_splits(coco, val_samples, test_samples)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "samples_val.json").write_text(
        json.dumps(val_samples, indent=2) + "\n", encoding="utf-8"
    )
    (out_dir / "samples_test.json").write_text(
        json.dumps(test_samples, indent=2) + "\n", encoding="utf-8"
    )

    metadata = {
        "source_annotations": annotations_path.name,
        "seed": seed,
        "min_area": min_area,
        "max_per_image": max_per_image,
        "p1_method": "euclidean_distance_transform_argmax",
        "val": {
            "num_objects": len(val_samples),
            "num_images": len({s["image_id"] for s in val_samples}),
            "num_categories": len({s["category_id"] for s in val_samples}),
        },
        "test": {
            "num_objects": len(test_samples),
            "num_images": len({s["image_id"] for s in test_samples}),
            "num_categories": len({s["category_id"] for s in test_samples}),
        },
    }
    (out_dir / "split_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate deterministic COCO val2017 splits and p1 points for P04 SAM 2."
    )
    parser.add_argument("--annotations", type=Path, required=True, help="Path to instances_val2017.json")
    parser.add_argument("--out-dir", type=Path, default=Path("configs"), help="Output directory")
    parser.add_argument("--n-val", type=int, default=100, help="Number of validation objects")
    parser.add_argument("--n-test", type=int, default=300, help="Number of test objects")
    parser.add_argument("--min-area", type=float, default=1024.0, help="Minimum COCO annotation area")
    parser.add_argument("--max-per-image", type=int, default=3, help="Max objects sampled per image")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for image-level shuffle")
    args = parser.parse_args()

    metadata = generate_splits(
        annotations_path=args.annotations,
        out_dir=args.out_dir,
        n_val=args.n_val,
        n_test=args.n_test,
        min_area=args.min_area,
        max_per_image=args.max_per_image,
        seed=args.seed,
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
