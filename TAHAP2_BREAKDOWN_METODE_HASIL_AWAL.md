# Breakdown Progres Tahap 2 — Metode dan Hasil Awal (Paket P04 · SAM 2)

> **Dokumen Acuan**: [README.md](./README.md) · [BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md) · [TAHAP1_BREAKDOWN_PENDAHULUAN.md](./TAHAP1_BREAKDOWN_PENDAHULUAN.md)  
> **Laman Tugas Resmi**: [Panduan Proyek Akhir Deep Learning S1 Kelas A](https://brone.ub.ac.id/mod/page/view.php?id=246059)

---

## 1. Ringkasan Administratif & Target Nilai (Tahap 2)

| Komponen | Ketentuan Resmi Tahap 2 |
| :--- | :--- |
| **Dibuka** | Selasa, 24 November 2026, 00.00 WIB |
| **Tenggat Pengumpulan** | **Selasa, 8 Desember 2026, 23.59 WIB** *(Minggu 2)* |
| **Bobot Nilai** | **30 poin** *(20 poin Pembanding Asli + 10 poin Prototipe Perbaikan)* |
| **Rubrik Penilaian Tahap 2** | • **Pembanding asli (20 poin)**: *"Kode berjalan, metrik baseline dicatat, dan pengaturan eksperimen dapat dilacak."*<br>• **Prototipe perbaikan (10 poin)**: *"Perubahan utama sudah diterapkan dan menghasilkan keluaran awal pada validasi."* |
| **Format Berkas** | **1 file PDF** lanjutan dari draf Tahap 1 + **tautan repositori yang dapat diakses dosen di dalam paper** *(atau unggah kode dalam 1 file ZIP)* + **perintah untuk menjalankan kode**. |
| **Mekanisme Unggah** | Diunggah oleh **1 perwakilan tim** |
| **Identitas Wajib di Paper** | Judul paper, kode paket (`P04`), nama lengkap & NIM seluruh anggota (`245150207111054`, `245150207111008`, `245150207111103`). |

> [!IMPORTANT]
> **Syarat Akses Repositori**: Karena tautan repo harus **dapat diakses dosen di dalam paper**, pastikan repo GitHub tim sudah diubah ke **Public** sebelum pengumpulan Tahap 2 (atau siapkan ekspor `.zip` sebagai cadangan bila menggunakan repo privat).

---

## 2. Breakdown Isi Wajib Naskah Tahap 2 (Lanjutan dari Tahap 1)

Naskah Tahap 2 tetap memuat bagian **Pendahuluan** dari Tahap 1 (diperbaiki bila ada masukan), lalu dilanjutkan dengan **Bagian 2 · Metode** dan **Bagian 3 · Hasil Awal**.

### A. Bagian 2 · Metode (Harus Lengkap & Dapat Dilacak)

| Subbagian | Poin Wajib yang Harus Dijelaskan (Khusus P04 · SAM 2) | Penanggung Jawab Utama |
| :--- | :--- | :--- |
| **2.1 Metode Asli (SAM 2)** | • Jelaskan cara kerja inferensi gambar pada **SAM 2** (*image encoder* `Hiera Tiny`, *prompt encoder*, dan *mask decoder* dengan `multimask_output=True`).<br>• Jelaskan bagaimana baseline 1-titik mengambil mask dengan skor prediksi tertinggi ($M_1$). | **Gibran** & **Sulthon** |
| **2.2 Perbaikan yang Diterapkan** | • Jelaskan alur modular (*toggleable*) metode usulan (`proposed_consensus_2pt`):<br>&nbsp;&nbsp;1) Ambil dua mask skor tertinggi $M_1, M_2$ dari 1 titik awal $p_1$.<br>&nbsp;&nbsp;2) Hitung $\text{IoU}(M_1, M_2)$.<br>&nbsp;&nbsp;3) Jika $\text{IoU} < 0{,}6$, ambil irisan $M_1 \cap M_2$, terapkan erosi morfologi kernel $3 \times 3$.<br>&nbsp;&nbsp;4) Jika ada piksel tersisa, pilih piksel terjauh secara Euclidean dari $p_1$ sebagai titik positif ke-2 ($p_2$) dan jalankan ulang SAM 2 dengan $[p_1, p_2]$; jika kosong atau $\text{IoU} \ge 0{,}6$, pertahankan $M_1$.<br>• Sertakan deskripsi singkat pembanding ablasi untuk Tahap 3 (`ablation_bestmask_2pt`: titik ke-2 dari $M_1$ saja). | **Gibran** |
| **2.3 Data & Pembagian Data** | • Jelaskan sumber data: subset objek dari **COCO** (`val2017`) beserta kriteria penyaringan (misal non-`iscrowd`, luas minimum objek).<br>• Jelaskan pemisahan tegas antara **Data Validasi** (untuk verifikasi prototipe Tahap 2) dan **Data Uji** (disimpan terpisah untuk Tahap 3 — tidak boleh bocor).<br>• Jelaskan cara pembuatan **titik awal $p_1$ deterministik** dari mask acuan sehingga identik di semua metode. | **Raditya** |
| **2.4 Metrik Evaluasi** | • **IoU terhadap mask acuan** (mIoU keseluruhan & pada kasus terpicu $\text{IoU}(M_1, M_2) < 0{,}6$).<br>• **Rata-rata jumlah titik per objek** (`1,00` s.d. `2,00`).<br>• Catat juga rencana pelacakan waktu inferensi (*latency*) per objek untuk biaya komputasi. | **Raditya** & **Sulthon** |
| **2.5 Pengaturan Eksperimen & Reproduksibilitas** | • Catat wajib: **commit hash** `facebookresearch/sam2`, nama config (`configs/sam2/sam2_hiera_t.yaml`), nama checkpoint (`sam2_hiera_tiny.pt`), versi `python`/`torch`/`torchvision`/`opencv-python`/`pycocotools`, jenis **GPU Colab** (misal Tesla T4), dan mode presisi (**FP32** tanpa `autocast` BF16).<br>• Cantumkan **tautan repo GitHub** dan **perintah untuk menjalankan kode** langsung di bagian ini (atau subbagian khusus Reproduksibilitas). | **Gibran** & **Raditya** |

### B. Bagian 3 · Hasil Awal (Pada Data Validasi)

1. **Hasil Baseline Metode Asli (`baseline_1pt`) pada Data Validasi**:
   - Tabel angka mIoU baseline pada seluruh subset Validasi (dan berapa persen objek yang memiliki $\text{IoU}(M_1, M_2) < 0{,}6$).
2. **Satu Bukti Prototipe Bekerja pada Data Validasi**:
   - **Bukti Kuantitatif Awal**: Hasil sementara metode usulan (`proposed_consensus_2pt`) pada data Validasi dibanding baseline 1-titik (beserta rata-rata jumlah titik yang dipakai).
   - **Bukti Visual (Wajib Jelas)**: Tampilkan minimal 1 gambar/objek dari data Validasi yang memperlihatkan: citra asli + $p_1$, mask $M_1$ dan $M_2$ awal beserta nilai $\text{IoU}(M_1, M_2) < 0{,}6$, area irisan setelah erosi $3\times 3$, lokasi titik ke-2 ($p_2$), serta perbandingan hasil sebelum vs sesudah titik ke-2 terhadap *ground truth*.

---

## 3. Target Teknis Sebelum Masuk Minggu 3

Sesuai panduan resmi kelas:
- Sebelum minggu ketiga (9 Desember 2026), **metode asli sudah harus menghasilkan angka pembanding** dan **prototipe sudah dapat diuji**.
- Jika ada kendala teknis berat (misal batasan kuota Colab/ukuran subset), hasil Tahap 2 dipakai sebagai dasar untuk memperkecil cakupan percobaan **dengan persetujuan dosen**.

---

## 4. Pembagian Kerja & Timeline Minggu 2 (2 – 8 Des 2026)

| Rentang Waktu | **Raditya** (`245150207111054`)<br>*Lead Naskah, Repo & Pipeline COCO* | **Gibran** (`245150207111008`)<br>*Google Colab & Teknis SAM 2* | **Sulthon** (`245150207111103`)<br>*Review Paper, Literatur & Analisis* |
| :--- | :--- | :--- | :--- |
| **2 – 4 Des**<br>*(Rabu–Jumat)* | Bangun `src/dataset_coco.py` + buat `configs/samples_val.json` dan `configs/samples_test.json` (split terpisah + titik awal `p1` deterministik). | Bangun `src/consensus_prompt.py` dengan mode *toggleable* (`1pt`, `bestmask_2pt`, `consensus_2pt`) + notebook `02_eval_coco_p04.ipynb` di Colab. | Bantu verifikasi kriteria filter objek COCO & siapkan draf subbagian **2.1 Metode Asli SAM 2** + **2.4 Metrik**. |
| **5 – 6 Des**<br>*(Sabtu–Minggu)* | Jalankan `baseline_1pt` & `proposed_consensus_2pt` pada **Data Validasi** (`results_val.csv`); tulis **2.3 Data & Split** serta rekap **Hasil Awal**. | Pastikan perintah run sekali jalan di Colab/CLI berfungsi rapi, tulis **2.2 Perbaikan** & **2.5 Pengaturan Eksperimen**, update `README.md`. | Inspeksi hasil validasi, buat gambar bukti visual prototipe bekerja pada 1–2 objek validasi (`M1`, `M2`, irisan tererosi, `p2`, hasil vs GT). |
| **7 Des**<br>*(Senin)* | Integrasikan semua bagian (Tahap 1 + Metode + Hasil Awal), pastikan link repo GitHub **Public** & perintah run tertulis jelas di PDF. | Review silang bagian Metode & tes ulang perintah menjalankan kode dari repo yang baru di-clone. | Review silang keterbacaan tabel/gambar bukti validasi dan konsistensi notasi ($p_1, p_2, M_1, M_2$). |
| **8 Des**<br>*(Selasa < 23.59 WIB)* | Jalankan QC Tahap 2, ekspor **1 file PDF**, dan unggah ke Brone sebelum 23.59 WIB. | Standby perbaikan bug terakhir bila ditemukan saat QC. | Standby perbaikan teks/gambar terakhir bila ditemukan saat QC. |

---

## 5. Checklist Quality Control (QC) Sebelum Unggah PDF Tahap 2

- [ ] PDF adalah **kelanjutan utuh dari Tahap 1** (Judul, kode `P04`, nama & NIM seluruh anggota, Pendahuluan, lalu Metode & Hasil Awal).
- [ ] **Metode asli**, **perbaikan yang diterapkan**, **data**, **pembagian data (Val vs Test terpisah)**, **metrik**, dan **pengaturan eksperimen** (commit, library, checkpoint, GPU, FP32) tertulis lengkap.
- [ ] **Hasil baseline (`1pt`)** dan **minimal satu bukti prototipe bekerja pada data validasi** (angka + visual) ditampilkan jelas.
- [ ] **Tautan repositori GitHub** tertulis di dalam paper dan status repo sudah **Public** (atau tersedia 1 file ZIP kode).
- [ ] **Perintah untuk menjalankan kode** tercantum eksplisit di dalam paper dan `README.md`.
- [ ] Data Uji (`samples_test.json`) **belum dipakai** untuk menyetel ambang/keputusan model (disimpan bersih untuk Tahap 3).
