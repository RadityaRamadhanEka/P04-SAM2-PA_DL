# Proyek Akhir Deep Learning S1 (Kelas A) — Paket P04: SAM 2

> **Perbaikan**: Penentuan Titik Tambahan Otomatis dari Area Kesepakatan Dua Mask Teratas (*Consensus-Guided 2nd Point*) pada **SAM 2 (`sam2_hiera_tiny`)**  
> **Lingkungan Utama**: Google Colab (GPU) · Mode FP32  
> **Periode**: 24 November – 15 Desember 2026

---

## Anggota Tim

| No | Nama Lengkap | NIM |
| :-: | :--- | :--- |
| 1 | **Raditya Ramadhan Eka Widhianto** | `245150207111054` |
| 2 | **Mochammad Fani Al Gibran** | `245150207111008` |
| 3 | **Muhammad Sulthon Aulia Wijaya** | `245150207111103` |

---

## Dokumen Briefing & Panduan Tim

1. **[BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md)** — Briefing teknis & operasional khusus Paket P04 (mekanisme perbaikan, desain eksperimen COCO di Colab, pembagian tugas 3 anggota, dan roadmap 3 minggu).
2. **[TAHAP1_BREAKDOWN_PENDAHULUAN.md](./TAHAP1_BREAKDOWN_PENDAHULUAN.md)** — Breakdown progres **Tahap 1 · Pendahuluan** (tenggat **Selasa, 1 Des 2026, 23.59 WIB**), struktur 6 blok pendahuluan, daftar pustaka, timeline 4 hari, dan checklist QC.
3. **[BRIEFING_PROYEK_AKHIR.md](./BRIEFING_PROYEK_AKHIR.md)** — Ringkasan lengkap panduan resmi Proyek Akhir Kelas A, rubrik 100 poin, ketentuan eksperimen, serta daftar seluruh paket `P01`–`P15`.

---

## Jadwal Pengumpulan

| Tahap | Tenggat | Fokus | Poin |
| :-: | :--- | :--- | :-: |
| **1** | **Selasa, 1 Desember 2026, 23.59 WIB** | Draf Paper: **Pendahuluan** + Daftar Pustaka (PDF) | **15** |
| **2** | **Selasa, 8 Desember 2026, 23.59 WIB** | **Metode & Hasil Awal** (baseline + bukti prototipe validasi + kode) | **30** |
| **3** | **Selasa, 15 Desember 2026, 23.59 WIB** | **Paper Lengkap & Kode Akhir** (uji test set, ablasi, biaya, contoh berhasil/gagal) | **55** |

---

## Struktur Repositori

```text
.
├── README.md
├── .gitignore
├── BRIEFING_PROYEK_AKHIR.md
├── BRIEFING_P04_SAM2.md
├── TAHAP1_BREAKDOWN_PENDAHULUAN.md
├── configs/        # Daftar sampel COCO (samples_val.json, samples_test.json) & titik awal p1
├── notebooks/      # Notebook Google Colab (smoke test & evaluasi COCO)
├── results/        # Log CSV per objek & gambar visualisasi berhasil/gagal
└── src/            # Modul Python toggleable (baseline_1pt, ablation_bestmask_2pt, proposed_consensus_2pt)
```

---

## Tautan Resmi Paket P04

- **Paper Asli SAM 2**: [OpenReview PDF](https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf) — https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf
- **Repositori GitHub SAM 2**: [facebookresearch/sam2](https://github.com/facebookresearch/sam2) — https://github.com/facebookresearch/sam2
- **Contoh Kode (`image_predictor_example.ipynb` · GitHub)**: [notebooks/image_predictor_example.ipynb](https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb) — https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb
- **Notebook Resmi di Google Colab**: [Buka di Colab](https://colab.research.google.com/github/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb)
- **Checkpoint Hiera Tiny**: [`sam2_hiera_tiny.pt`](https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_tiny.pt)
- **Pembanding Pembahasan**: [Pracetak BALD-SAM](https://arxiv.org/abs/2603.10828)
