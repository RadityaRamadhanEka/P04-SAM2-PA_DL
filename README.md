# Proyek Akhir Deep Learning S1 (Kelas A) — Paket P04: SAM 2

> **Perbaikan**: Penentuan Titik Tambahan Otomatis dari Area Kesepakatan Dua Mask Teratas (*Consensus-Guided 2nd Point*) pada **SAM 2 (`sam2_hiera_tiny`)**  
> **Lingkungan Utama**: Google Colab (GPU) · Mode FP32  
> **Format Paper**: Template **IEEE Conference 2-Kolom** (A4, Times New Roman 10 pt)  
> **Google Docs Tim**: [Buka Naskah Paper (Google Docs)](https://docs.google.com/document/d/1yhD0Zz_ED-kEKbYtkoU5JcAHJr4lLNlThJ2I3ObtyGk/edit)  
> **Periode**: 24 November – 15 Desember 2026

---

## Anggota Tim & Peran

| No | Nama Lengkap | NIM | Fokus Peran *(Disepakati)* |
| :-: | :--- | :--- | :--- |
| 1 | **Raditya Ramadhan Eka Widhianto** | `245150207111054` | Lead Naskah, Repo, Pipeline COCO & Evaluasi |
| 2 | **Mochammad Fani Al Gibran** | `245150207111008` | Google Colab & Teknis Implementasi SAM 2 |
| 3 | **Muhammad Sulthon Aulia Wijaya** | `245150207111103` | Review Paper (SAM 2 & BALD-SAM), Analisis & Visualisasi |

---

## Dokumen Briefing & Panduan Tim

1. **[BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md)** — Briefing teknis & operasional khusus Paket P04 (mekanisme perbaikan, desain eksperimen COCO di Colab, pembagian tugas 3 anggota, dan roadmap 3 minggu).
2. **[TAHAP1_BREAKDOWN_PENDAHULUAN.md](./TAHAP1_BREAKDOWN_PENDAHULUAN.md)** — Breakdown progres **Tahap 1 · Pendahuluan** (tenggat **Selasa, 1 Des 2026, 23.59 WIB · 15 poin**).
3. **[TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md](./TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md)** — Breakdown progres **Tahap 2 · Metode & Hasil Awal** (tenggat **Selasa, 8 Des 2026, 23.59 WIB · 30 poin**).
4. **[TAHAP3_BREAKDOWN_PAPER_LENGKAP.md](./TAHAP3_BREAKDOWN_PAPER_LENGKAP.md)** — Breakdown progres **Tahap 3 · Paper Lengkap & Kode Akhir** (tenggat **Selasa, 15 Des 2026, 23.59 WIB · 55 poin**).
5. **[BRIEFING_PROYEK_AKHIR.md](./BRIEFING_PROYEK_AKHIR.md)** — Ringkasan lengkap panduan resmi Proyek Akhir Kelas A, rubrik 100 poin, ketentuan eksperimen, serta daftar seluruh paket `P01`–`P15`.

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
├── TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md
├── TAHAP3_BREAKDOWN_PAPER_LENGKAP.md
├── configs/        # Daftar sampel COCO (samples_val.json, samples_test.json) & titik awal p1
├── notebooks/      # Notebook Google Colab (smoke test & evaluasi COCO)
├── results/        # Log CSV per objek & gambar visualisasi berhasil/gagal
└── src/            # Modul Python toggleable (baseline_1pt, ablation_bestmask_2pt, proposed_consensus_2pt)
```

---

## Tautan Penting Tim & Paket P04

- **Google Docs Naskah Paper Tim (IEEE 2-Kolom)**: [Proyek Akhir Deep Learning (Kelas A) - P04 SAM 2](https://docs.google.com/document/d/1yhD0Zz_ED-kEKbYtkoU5JcAHJr4lLNlThJ2I3ObtyGk/edit?usp=drivesdk) — https://docs.google.com/document/d/1yhD0Zz_ED-kEKbYtkoU5JcAHJr4lLNlThJ2I3ObtyGk/edit?usp=drivesdk
- **Paper Asli SAM 2**: [OpenReview PDF](https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf) — https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf
- **Repositori GitHub SAM 2**: [facebookresearch/sam2](https://github.com/facebookresearch/sam2) — https://github.com/facebookresearch/sam2
- **Contoh Kode (`image_predictor_example.ipynb` · GitHub)**: [notebooks/image_predictor_example.ipynb](https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb) — https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb
- **Notebook Resmi di Google Colab**: [Buka di Colab](https://colab.research.google.com/github/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb)
- **Checkpoint Hiera Tiny**: [`sam2_hiera_tiny.pt`](https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_tiny.pt)
- **Pembanding Pembahasan**: [Pracetak BALD-SAM](https://arxiv.org/abs/2603.10828)
