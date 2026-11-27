# Breakdown Progres Tahap 1 — Pendahuluan (Paket P04 · SAM 2)

> **Dokumen Acuan**: [BRIEFING_PROYEK_AKHIR.md](./BRIEFING_PROYEK_AKHIR.md) · [BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md)  
> **Laman Tugas Resmi**: [Panduan Proyek Akhir Deep Learning S1 Kelas A](https://brone.ub.ac.id/mod/page/view.php?id=246059)

---

## 1. Ringkasan Administratif & Target Nilai (Tahap 1)

| Komponen | Ketentuan Resmi Tahap 1 |
| :--- | :--- |
| **Dibuka** | Selasa, 24 November 2026, 00.00 WIB |
| **Tenggat Pengumpulan** | **Selasa, 1 Desember 2026, 23.59 WIB** *(tersisa ±4 hari dari 27 November 2026)* |
| **Bobot Nilai** | **15 poin** *(dari total 100 poin proyek)* |
| **Rubrik Penilaian Tahap 1** | *"Masalah dan konteks paper dijelaskan secara tepat. Keterbatasan, tujuan, dan hipotesis terhubung dengan perbaikan pada paket."* |
| **Format Berkas** | **1 file PDF** dengan template paper ilmiah bebas *(disarankan langsung memilih satu template tetap — misal IEEE 2-kolom di LaTeX/Overleaf atau Word/Google Docs — yang dipakai terus hingga Tahap 3)* |
| **Mekanisme Unggah** | Diunggah oleh **1 perwakilan tim** |
| **Identitas Wajib di Halaman 1** | 1. **Judul paper** tim<br>2. **Kode paket**: `P04`<br>3. **Nama lengkap & NIM seluruh anggota**:<br>&nbsp;&nbsp;&nbsp;• Raditya Ramadhan Eka Widhianto (`245150207111054`)<br>&nbsp;&nbsp;&nbsp;• Mochammad Fani Al Gibran (`245150207111008`)<br>&nbsp;&nbsp;&nbsp;• Muhammad Sulthon Aulia Wijaya (`245150207111103`) |

---

## 2. Breakdown Struktur & Isi Wajib Naskah Tahap 1 (Khusus P04 · SAM 2)

Pada Tahap 1, naskah PDF berisi **Header Identitas**, **Bagian 1 · Pendahuluan**, dan **Daftar Pustaka**. Berikut rincian blok demi blok agar setiap poin rubrik terpenuhi secara langsung.

### A. Opsi Judul Paper Tim
Pilih atau sesuaikan salah satu opsi judul berikut (menggambarkan model, masalah, dan perbaikan P04 secara akurat):
1. *Penentuan Titik Tambahan Otomatis Berbasis Area Kesepakatan Dua Mask untuk Mengurangi Ambiguitas Segmentasi Satu-Titik pada SAM 2*
2. *Peningkatan Segmentasi Interaktif Satu-Titik pada SAM 2 melalui Titik Petunjuk Kedua dari Irisan Tererosi Kandidat Mask*
3. *Strategi Pemilihan Titik Kedua Berbasis Kesepakatan Mask untuk Mengatasi Ambiguitas Prompt Tunggal pada SAM 2*

### B. Breakdown Paragraf Bagian 1 · Pendahuluan

| Blok | Fokus Utama | Poin Spesifik yang Harus Ditulis (Khusus P04 · SAM 2) |
| :-: | :--- | :--- |
| **1** | **Konteks & Masalah yang Diteliti** | • Jelaskan peran *promptable segmentation* / segmentasi interaktif berbasis *foundation model* melalui **SAM 2** (*Segment Anything Model 2*) dalam menandai objek pada citra hanya dari **satu titik awal** di dalam objek.<br>• Jelaskan masalah inti: **ambiguitas prompt satu titik** (*single-point prompt ambiguity*). Satu titik di dalam objek sering dapat ditafsirkan sebagai bagian objek (*part*) maupun keseluruhan objek (*whole*), misalnya titik pada kursi bisa menghasilkan mask seluruh kursi atau hanya dudukannya. |
| **2** | **Mengapa Masalah Ini Penting** | • Pada skenario anotasi interaktif berbiaya rendah (*low-click annotation*) maupun inferensi otomatis dengan prompt minimal, pengguna atau sistem ingin mempertahankan **beban interaksi serendah mungkin** (mendekati 1 titik per objek) tanpa mengorbankan akurasi mask (IoU).<br>• Jika prediksi 1-titik meleset akibat ambiguitas, kualitas segmentasi turun drastis atau pengguna harus memberi koreksi manual berulang. |
| **3** | **Keterbatasan Metode Asli (SAM 2) yang Ingin Ditangani** | • SAM 2 sebenarnya menghasilkan beberapa kandidat mask (*multimask output*) beserta skor kepercayaannya, namun dalam inferensi 1-titik standar, sistem langsung mengambil mask dengan skor tertinggi tanpa memanfaatkan **ketidaksepakatan antar kandidat mask**.<br>• Ketika dua kandidat mask teratas berbeda jauh ($\text{IoU}(M_1, M_2)$ rendah), ketidaksepakatan itu adalah sinyal alami adanya ambiguitas, tetapi metode asli tidak memiliki aturan otomatis untuk menyelesaikannya dengan satu titik tambahan.<br>• Singgung secara ringkas bahwa pendekatan berbasis ketidakpastian interaktif seperti **BALD-SAM** membutuhkan estimasi ketidakpastian tersendiri, sedangkan aturan kesepakatan dua mask menawarkan mekanisme otomatis yang ringan tanpa melatih ulang model. |
| **4** | **Tujuan Penelitian** | • Rumuskan secara terukur: mengimplementasikan dan mengevaluasi aturan pemilihan titik positif kedua secara otomatis pada **SAM 2 (`sam2_hiera_tiny`)** menggunakan area yang disepakati oleh dua kandidat mask teratas ketika terjadi ketidaksepakatan ($\text{IoU} < 0{,}6$), lalu mengukur dampaknya terhadap **IoU** terhadap mask acuan dan **rata-rata jumlah titik per objek** pada subset **COCO**. |
| **5** | **Hipotesis Penelitian** | • **Hipotesis utama ($H_1$)**: Pada objek dengan ambiguitas prediksi 1-titik ($\text{IoU}(M_1, M_2) < 0{,}6$), penambahan satu titik positif kedua yang diambil dari area irisan dua mask teratas setelah erosi $3 \times 3$ (pada piksel terjauh dari titik awal) akan menghasilkan **IoU rata-rata lebih tinggi** dibanding prediksi 1-titik saja maupun penambahan titik kedua dari mask terbaik saja, dengan tambahan titik rata-rata di bawah 2 titik per objek.<br>• **Batas hipotesis**: Apabila **kedua mask awal sama-sama salah** sehingga area kesepakatannya meleset dari objek acuan, titik kedua yang dipilih tetap berada di wilayah keliru dan tidak akan memperbaiki (bahkan dapat menurunkan) IoU. |
| **6** | **Ringkasan Perbaikan & Rencana Pengujian** | • Uraikan alur ringkas metode:<br>&nbsp;&nbsp;1) Beri 1 titik awal $p_1$ pada SAM 2 dan simpan dua mask dengan skor tertinggi ($M_1, M_2$).<br>&nbsp;&nbsp;2) Hitung $\text{IoU}(M_1, M_2)$. Jika $\ge 0{,}6$, pertahankan prediksi awal.<br>&nbsp;&nbsp;3) Jika $< 0{,}6$, ambil irisan $M_1 \cap M_2$, lakukan erosi kernel $3 \times 3$; jika tidak ada piksel tersisa, pertahankan prediksi awal.<br>&nbsp;&nbsp;4) Jika ada piksel tersisa, pilih piksel terjauh dari $p_1$ sebagai titik positif kedua $p_2$ dan jalankan ulang SAM 2 dengan kedua titik.<br>• Ringkas rencana uji pada subset objek COCO (dengan titik awal yang sama): bandingkan **1 titik awal**, **titik kedua dari mask terbaik saja**, dan **titik kedua dari area kesepakatan dua mask**, dengan pelaporan **IoU** dan **rata-rata jumlah titik**. |

### C. Daftar Pustaka Minimal Tahap 1
Cantumkan **paper utama** dan referensi konteks yang disitir di Pendahuluan (pastikan metadata lengkap dan sesuai sumber resmi sebelum PDF diunggah):
1. **Paper Utama Wajib — SAM 2**: Ravi, N., et al. (*SAM 2: Segment Anything in Images and Videos*, ICLR 2025). Tautan resmi paket: [OpenReview PDF](https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf).
2. **Dataset Acuan — COCO**: Lin, T.-Y., et al. (*Microsoft COCO: Common Objects in Context*, ECCV 2014) — jika menyebut dataset COCO di ringkasan rencana pengujian.
3. **Konteks Dasar — SAM**: Kirillov, A., et al. (*Segment Anything*, ICCV 2023) — opsional jika membahas asal-usul desain *ambiguity-aware multimask*.
4. **Pembanding Ketidakpastian — BALD-SAM**: [arXiv:2603.10828](https://arxiv.org/abs/2603.10828) — *(catatan: cek judul & daftar penulis persis di halaman arXiv sebelum memasukkan ke Daftar Pustaka final)*.

---

## 3. Pemisahan Deliverable PDF vs Tugas Teknis Paralel Minggu 1

Agar fokus pengerjaan tidak tercampur antara apa yang harus selesai untuk unggahan **1 Desember** dan apa yang disiapkan agar **Tahap 2 (8 Desember)** tidak kewalahan:

| Kategori | Masuk ke PDF Tahap 1? | Keterangan |
| :--- | :---: | :--- |
| Judul, kode paket `P04`, nama & NIM 3 anggota | **Ya (Wajib)** | Cantumkan jelas di header halaman pertama PDF. |
| Bagian Pendahuluan (masalah, urgensi, keterbatasan, tujuan, hipotesis, ringkasan perbaikan) | **Ya (Wajib)** | Inti penilaian 15 poin Tahap 1. |
| Daftar Pustaka (minimal paper SAM 2) | **Ya (Wajib)** | Gunakan format sitasi konsisten (misal IEEE). |
| Bagian Metode rinci, split data, angka hasil baseline, & tabel perbandingan | **Belum** | Baru dikumpulkan di **Tahap 2** (8 Des) dan **Tahap 3** (15 Des). |
| *Smoke test* Colab: `sam2_hiera_tiny.pt` (FP32) jalan pada **1 gambar + 1 titik** | **Tidak wajib masuk PDF, tetapi WAJIB dikerjakan paralel di Minggu 1** | Ketentuan panduan mengharuskan tim memverifikasi contoh penulis berjalan di awal minggu pertama untuk memastikan tidak ada kendala perangkat/akses Colab. |

---

## 4. Pembagian Kerja Tim & Timeline 4 Hari (27 Nov – 1 Des 2026)

| Rentang Waktu | Fokus Utama | Pembagian Tugas Anggota |
| :--- | :--- | :--- |
| **Hari 1**<br>27 – 28 Nov 2026 | **Kunci Template, Pustaka, & Smoke Test Colab** | • **Raditya**: Pilih template paper final (LaTeX/Overleaf atau Word/Docs) + isi header identitas (`P04`, nama, NIM) + susun kerangka 6 blok Pendahuluan.<br>• **Gibran**: Buka [Colab resmi SAM 2](https://colab.research.google.com/github/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb), unduh `sam2_hiera_tiny.pt`, uji 1 gambar + 1 titik (nonaktifkan `autocast` BF16 $\rightarrow$ FP32 bila pakai T4), dan catat versi library + nama GPU.<br>• **Sulthon**: Baca paper **SAM 2** (bagian arsitektur/prompt/multimask ambiguity) & laman **[BALD-SAM](https://arxiv.org/abs/2603.10828)**, lalu rangkum poin sitasi untuk Pendahuluan & Daftar Pustaka. |
| **Hari 2**<br>29 Nov 2026 | **Penulisan Draf Lengkap Pendahuluan** | • **Sulthon**: Tulis Blok 1–3 (konteks, urgensi, keterbatasan SAM 2 + sitasi SAM 2 & BALD-SAM) serta Daftar Pustaka.<br>• **Raditya**: Tulis Blok 4–6 (tujuan, hipotesis beserta batas kegagalan, ringkasan mekanisme `IoU < 0.6` + erosi $3\times 3$ + rencana uji COCO).<br>• **Gibran**: Pastikan hasil *smoke test* 1 gambar + 1 titik beres (simpan screenshot & log versi dependensi sebagai bekal Tahap 2) dan bantu review akurasi teknis alur kode pada Blok 6. |
| **Hari 3**<br>30 Nov 2026 | **Review Silang & Konsistensi Rubrik** | • **Semua anggota**: Baca utuh dari judul sampai Daftar Pustaka; cek apakah alur *Masalah $\rightarrow$ Keterbatasan SAM 2 $\rightarrow$ Tujuan $\rightarrow$ Hipotesis $\rightarrow$ Ringkasan Perbaikan P04* tersambung mulus.<br>• **Raditya**: Finalisasi layout dan ekspor ke **PDF**. |
| **Hari 4**<br>1 Des 2026 *(sebelum 23.59 WIB)* | **QC Final & Unggah Berkas** | • **Raditya / 1 perwakilan tim**: Lakukan QC 10 poin di bawah, lalu unggah **1 file PDF** ke Brone jauh sebelum pukul **23.59 WIB** (target aman: sore/malam awal). |

---

## 5. Checklist Quality Control (QC) Sebelum Unggah PDF ke Brone

- [ ] **Judul paper** sudah dicantumkan dan sesuai isi perbaikan P04.
- [ ] **Kode paket `P04`** tertulis jelas di bagian identitas halaman pertama.
- [ ] **Nama lengkap & NIM ketiga anggota** (`245150207111054`, `245150207111008`, `245150207111103`) lengkap dan tidak ada salah ketik.
- [ ] Masalah ambiguitas prompt 1-titik pada SAM 2 dan **mengapa masalah itu penting** dijelaskan dengan jelas (disertai ilustrasi konseptual seperti kursi vs dudukan kursi).
- [ ] **Keterbatasan metode asli SAM 2** (sudah punya *multimask*, tetapi belum memanfaatkan ketidaksepakatan dua mask teratas untuk titik tambahan otomatis) tertulis eksplisit.
- [ ] **Tujuan** dan **hipotesis** (termasuk kondisi batas ketika kedua mask awal salah) terhubung langsung dengan mekanisme P04.
- [ ] **Ringkasan perbaikan** menyebut parameter kunci paket P04 dengan benar: dua mask skor tertinggi, ambang `IoU < 0,6`, irisan dua mask, erosi kernel `3 × 3`, piksel terjauh dari titik awal, serta 3 pembanding pada objek & titik awal COCO yang sama.
- [ ] **Paper utama SAM 2** tercantum di **Daftar Pustaka** dengan sitasi yang konsisten dan terverifikasi.
- [ ] File dalam format **PDF** tunggal, layout rapi (tidak ada teks terpotong atau gambar/tabel pecah), dan penamaan file jelas (misal: `Tahap1_Pendahuluan_P04_SAM2_KelasA.pdf`).
- [ ] *Smoke test* Colab (`sam2_hiera_tiny.pt`, FP32) sudah berhasil diuji pada 1 gambar + 1 titik agar tim siap langsung masuk ke Tahap 2.
