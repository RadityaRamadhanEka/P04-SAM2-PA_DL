# Briefing Teknis & Operasional — Paket P04 (SAM 2)

> **Mata Kuliah**: Deep Learning S1 — Kelas A  
> **Paket**: **P04 · SAM 2 — Titik Tambahan dari Area yang Disepakati Dua Mask** *(ICLR 2025 · GPU · Inferensi)*  
> **Periode**: 24 November – 15 Desember 2026  
> **Dokumen Panduan Umum**: [BRIEFING_PROYEK_AKHIR.md](./BRIEFING_PROYEK_AKHIR.md)

---

## 1. Profil Tim & Ringkasan Paket P04

| Komponen | Keterangan |
| :--- | :--- |
| **Anggota 1** | **Raditya Ramadhan Eka Widhianto** (`245150207111054`) |
| **Anggota 2** | **Mochammad Fani Al Gibran** (`245150207111008`) |
| **Anggota 3** | **Muhammad Sulthon Aulia Wijaya** (`245150207111103`) |
| **Lingkungan Komputasi** | **Google Colab (GPU gratis)** — mode **FP32** (nonaktifkan `autocast` BF16 bila GPU Colab tidak mendukung BF16) |
| **Model & Konfigurasi** | `configs/sam2/sam2_hiera_t.yaml` + checkpoint **`sam2_hiera_tiny.pt`** |
| **Dataset Evaluasi** | Subset **COCO** (memakai mask anotasi acuan / *ground truth* untuk menghasilkan titik awal & menghitung IoU) |
| **Strategi Target** | **Prioritas 1**: Nilai maksimal mata kuliah (100 poin sesuai rubrik 3 tahap).<br>**Prioritas 2**: Struktur eksperimen, pencatatan hasil per objek, dan kajian literatur dirapikan sejak awal agar siap dikembangkan ke publikasi jika hasilnya menjanjikan. |

### Tautan Resmi Wajib P04
- **Paper Asli SAM 2**: [OpenReview PDF](https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf)
- **Repositori GitHub SAM 2**: [facebookresearch/sam2](https://github.com/facebookresearch/sam2)
- **Notebook Contoh Penulis**: [`notebooks/image_predictor_example.ipynb`](https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb)
- **Notebook Resmi di Google Colab**: [Buka di Colab](https://colab.research.google.com/github/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb)
- **Checkpoint Resmi Hiera Tiny**: [`sam2_hiera_tiny.pt`](https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_tiny.pt)
- **Referensi Pembanding Pembahasan (Wajib Dibahas)**: [Pracetak BALD-SAM](https://arxiv.org/abs/2603.10828)

---

## 2. Masalah, Mekanisme Perbaikan, & Draft Hipotesis

### A. Masalah yang Diteliti
- SAM 2 dapat melakukan segmentasi objek hanya dari **satu titik awal** di dalam objek.
- Namun, satu titik sering **ambigu** secara semantik (skala bagian vs keseluruhan objek): misalnya ketika titik diletakkan di sebuah kursi, satu kandidat mask bisa menandai **seluruh kursi**, sedangkan kandidat mask lain hanya menandai **dudukan kursi**.
- Akibatnya, hasil dengan 1 titik bisa meleset dari anotasi acuan, terutama ketika dua kandidat mask teratas yang dihasilkan model memiliki bentuk yang berbeda jauh.

### B. Alur Algoritmik Metode Usulan (*Consensus-Guided 2nd Point*)
Untuk setiap objek uji dengan satu titik awal $p_1$:

1. **Inferensi Tahap 1 (1 Titik)**: Jalankan `SAM2ImagePredictor` dengan $p_1$ (label positif `1`) dan `multimask_output=True`. Ambil **dua mask dengan skor prediksi tertinggi**, sebut $M_1$ (skor tertinggi) dan $M_2$ (skor tertinggi kedua).
2. **Ukur Kesepakatan Dua Mask**: Hitung $\text{IoU}(M_1, M_2) = \frac{|M_1 \cap M_2|}{|M_1 \cup M_2|}$.
   - *Contoh konkret dari panduan*: Jika kedua mask sama-sama menandai `40` piksel dari total `100` piksel gabungan, maka $\text{IoU} = 0{,}40 < 0{,}60$.
3. **Cek Ambang Kesepakatan (`0.6`)**:
   - **Jika $\text{IoU}(M_1, M_2) \ge 0{,}6$**: kedua kandidat cukup sepakat $\rightarrow$ **hentikan**, gunakan prediksi awal (mask terbaik $M_1$, total **1 titik**).
   - **Jika $\text{IoU}(M_1, M_2) < 0{,}6$**:
     1. Ambil **irisan kesepakatan**: $I = M_1 \cap M_2$.
     2. Lakukan **erosi morfologi dengan kernel $3 \times 3$** pada $I$ untuk membuang piksel dekat tepi mask, menghasilkan $I_{\text{eroded}}$.
     3. **Edge case**: Jika $I_{\text{eroded}}$ kosong (tidak ada piksel tersisa, atau $I$ sendiri kosong), **pertahankan prediksi awal** ($M_1$, total **1 titik**).
     4. Jika $I_{\text{eroded}}$ tidak kosong, hitung jarak Euclidean dari setiap piksel di $I_{\text{eroded}}$ ke titik awal $p_1$, lalu pilih piksel dengan **jarak paling jauh dari $p_1$** sebagai titik positif kedua $p_2$.
     5. **Inferensi Tahap 2 (2 Titik)**: Jalankan ulang SAM 2 pada gambar yang sama dengan pasangan titik $[p_1, p_2]$ (keduanya label positif `1`) untuk mendapatkan mask akhir (total **2 titik**).

> [!NOTE]
> **Catatan Edge Case Saat Implementasi**:
> - Pastikan penanganan kasus $|M_1 \cup M_2| = 0$ (mask kosong $\rightarrow$ anggap $\text{IoU} = 1{,}0$ atau langsung pertahankan prediksi awal agar tidak *division by zero*).
> - Pada inferensi ke-2, simpan juga waktu eksekusi dan cek apakah `set_image()` (ekstraksi *image embedding*) hanya perlu dipanggil **sekali per gambar** sementara `predict()` dipanggil ulang untuk tiap prompt titik. Ini penting untuk analisis biaya komputasi yang jujur.

### C. Rumusan Tujuan & Hipotesis *(Siap Pakai / Disempurnakan di Tahap 1)*
- **Tujuan**: Menguji apakah penambahan satu titik positif otomatis dari area kesepakatan tererosi dua mask teratas SAM 2 (ketika $\text{IoU}(M_1, M_2) < 0{,}6$) dapat meningkatkan akurasi segmentasi (IoU terhadap mask acuan) dibanding prediksi 1 titik maupun titik ke-2 dari mask terbaik saja, dengan tambahan titik rata-rata yang minimal.
- **Hipotesis**: Pada objek dengan ambiguitas prompt 1-titik ($\text{IoU}(M_1, M_2) < 0{,}6$), pemilihan titik kedua dari area irisan dua mask teratas yang telah dierosi ($3 \times 3$) dan berjarak terjauh dari titik awal memberikan titik penjelas yang lebih aman berada di bagian inti objek, sehingga menghasilkan **IoU rata-rata lebih tinggi** dibanding metode 1-titik dan metode titik kedua dari mask terbaik saja, terutama pada kasus di mana kedua mask awal masih memuat sebagian badan objek yang benar. Sebaliknya, perbaikan ini diperkirakan tidak membantu apabila **kedua mask awal sama-sama salah** menempatkan area kesepakatan di luar objek acuan.

---

## 3. Desain Eksperimen & Protokol Google Colab

### A. Pengaturan Model & GPU Colab Gratis
- **Konfigurasi**: `configs/sam2/sam2_hiera_t.yaml`
- **Bobot**: `sam2_hiera_tiny.pt`
- **Masalah Umum Colab T4 & Solusinya**:
  - Notebook resmi SAM 2 memakai `torch.autocast(device_type="cuda", dtype=torch.bfloat16)`.
  - GPU gratis Colab paling sering adalah **NVIDIA T4** (arsitektur Turing) yang **tidak mendukung native BF16** atau dapat menimbulkan error/ketidakstabilan `autocast`.
  - Sesuai panduan resmi P04: jika `autocast` BF16 bermasalah pada GPU yang didapat, **nonaktifkan `autocast` BF16 dan jalankan dalam FP32**, tetap memakai bobot `sam2_hiera_tiny.pt`.
- **Detail Reproduksibilitas yang Wajib Dicatat di Bagian Metode**:
  - Commit hash repo `facebookresearch/sam2` saat `git clone`.
  - Versi `python`, `torch`, `torchvision`, `numpy`, `opencv-python`, `pycocotools`.
  - Nama file checkpoint (`sam2_hiera_tiny.pt`) & config (`sam2_hiera_t.yaml`).
  - Nama GPU Colab aktual (misal `Tesla T4 15GB`) dan mode presisi (`FP32`).

### B. Dataset COCO, Pembagian Split, & Titik Awal Deterministik
- **Sumber Data**: Subset objek dari **COCO** (misalnya `val2017` yang ringkas diunduh/diakses di Colab, lalu dipecah secara deterministik menjadi subset **Validasi** dan subset **Uji** yang terpisah tanpa irisan gambar/objek).
  - *Saran praktis agar cepat & adil*: pilih ukuran subset yang nyaman dijalankan di Colab gratis (misal **100–200 objek pada Validasi** untuk Tahap 2, dan **300–500 objek pada Uji** untuk Tahap 3, dengan filter mask non-iscrowd dan luas minimum tertentu agar erosi $3\times 3$ bermakna; laporkan kriteria filter secara eksplisit di Metode).
- **Titik Awal ($p_1$) yang Identik di Semua Metode**:
  - Gunakan mask acuan (*ground truth*) untuk menghasilkan **satu titik awal deterministik per objek** (misalnya piksel dengan nilai *Euclidean distance transform* terbesar di dalam mask acuan — titik paling tengah/aman di dalam objek — atau titik acak ber-seed tetap di dalam mask acuan).
  - **Simpan daftar sampel** (`image_id`, `ann_id`, `category_id`, `area`, `p1_x`, `p1_y`) ke dalam file `samples_val.json` dan `samples_test.json` di Google Drive / repo tim. Dengan begitu, ketiga pembanding dijamin menguji **objek dan titik awal yang 100% sama**.

### C. Tiga Pembanding Wajib (Modular / *Toggleable*)
Implementasikan dalam satu fungsi/kelas dengan flag konfigurasi (misal `mode="1pt" | "bestmask_2pt" | "consensus_2pt"` dan `iou_threshold=0.6`):

| Kode Metode | Aturan | Tujuan Pembandingan |
| :--- | :--- | :--- |
| **`baseline_1pt`** | Jalankan SAM 2 dengan 1 titik awal $p_1$, ambil mask skor tertinggi $M_1$. | Pembanding asli (*baseline* 1 titik). |
| **`ablation_bestmask_2pt`** | Jika $\text{IoU}(M_1, M_2) < 0{,}6$, pilih titik ke-2 dari **$M_1$ saja** (erosi $3\times 3$, titik terjauh dari $p_1$) lalu jalankan ulang SAM 2 dengan $[p_1, p_2]$. | Pembanding/ablasi untuk mengisolasi efek "irisan dua mask" vs sekadar "menambah titik ke-2 dari mask terbaik". |
| **`proposed_consensus_2pt`** | Jika $\text{IoU}(M_1, M_2) < 0{,}6$, pilih titik ke-2 dari **irisan $M_1 \cap M_2$** (erosi $3\times 3$, titik terjauh dari $p_1$) lalu jalankan ulang SAM 2 dengan $[p_1, p_2]$. | Metode usulan sesuai paket P04. |

### D. Metrik, Log per Sampel, & Analisis Wajib
Simpan hasil mentah setiap objek ke CSV (`results_test.csv`) agar semua analisis di bawah bisa dihitung langsung:
1. **IoU terhadap mask acuan** (mIoU keseluruhan, mIoU khusus sub-kelompok objek yang memicu $\text{IoU}(M_1, M_2) < 0{,}6$, dan distribusi selisih berpasangan $\Delta\text{IoU}$ per objek).
2. **Rata-rata jumlah titik per objek** (antara `1.00` hingga `2.00`) dan persentase objek yang memicu tahap kedua.
3. **Biaya komputasi**: waktu inferensi rata-rata per objek / total waktu evaluasi di GPU Colab yang sama (bandingkan apakah `set_image` di-reuse vs dihitung ulang).
4. **Analisis Kualitatif Wajib**:
   - **$\ge 1$ contoh berhasil**: visualisasi citra asli + $p_1$ + $M_1$ + $M_2$ + irisan tererosi + $p_2$ + hasil akhir vs *ground truth*.
   - **$\ge 1$ contoh gagal (khusus wajib P04)**: **kasus ketika kedua mask awal ($M_1$ dan $M_2$) sama-sama salah** (misal sama-sama menempel pada latar/sub-bagian yang keliru sehingga $p_2$ dari kesepakatan kedua mask justru memperkuat kesalahan).
5. **Pembahasan Literatur (Wajib P04)**:
   - Bandingkan aturan heuristik berbasis kesepakatan mask (`IoU < 0.6` + erosi irisan) dengan pendekatan berbasis **ketidakpastian** untuk anotasi interaktif pada **[BALD-SAM](https://arxiv.org/abs/2603.10828)** (kapan heuristik dua-mask lebih ringan/praktis tanpa *Bayesian sampling*, dan apa keterbatasannya saat model *overconfident* tapi salah).

---

## 4. Pembagian Kerja Tim (Disepakati — 3 Anggota)

Pembagian ini sudah disepakati tim (**Raditya** memegang naskah/repo/pipeline evaluasi COCO, **Gibran** memegang Google Colab & implementasi SAM 2, dan **Sulthon** memegang review paper/literatur & analisis) agar seimbang di seluruh 3 tahap dan memudahkan setiap anggota menjelaskan kontribusinya saat presentasi akhir:

| Tahap | **Raditya** (`245150207111054`)<br>*Lead Naskah, Repo & Pipeline COCO* | **Gibran** (`245150207111008`)<br>*Google Colab & Teknis SAM 2* | **Sulthon** (`245150207111103`)<br>*Review Paper, Literatur & Analisis* |
| :--- | :--- | :--- | :--- |
| **Tahap 1** *(1 Des)* | Menyiapkan template paper final + header identitas (`P04`, nama, NIM), menulis Tujuan, Hipotesis, & Ringkasan Rencana Uji, serta finalisasi PDF + submit. | Membuka Colab resmi SAM 2, menjalankan *smoke test* (`sam2_hiera_tiny.pt`, mode FP32 bila GPU T4), mencatat versi library/GPU/commit, & review teknis alur perbaikan. | Mereview paper asli **SAM 2** & pracetak **BALD-SAM**, menulis Latar Belakang Masalah, Urgensi, Keterbatasan SAM 2, serta menyusun Daftar Pustaka. |
| **Tahap 2** *(8 Des)* | Membangun pipeline subset COCO (split Val/Test deterministik + simpan `p1` ke JSON), integrasi laporan Tahap 2, & submit PDF + tautan repo. | Mengimplementasikan `baseline_1pt` & modul perbaikan *toggleable* (`proposed_consensus_2pt` + `ablation_bestmask_2pt`) di Colab. | Mengevaluasi hasil awal Validasi (IoU & rata-rata titik), verifikasi visual penempatan `p2`, & menyusun ringkasan literatur bagian Metode. |
| **Tahap 3** *(15 Des)* | Mengaudit/menjalankan uji final di Test Set (tabel perbandingan, selisih berpasangan, biaya komputasi) & menyusun Abstrak + Kesimpulan + submit akhir. | Merapikan kode akhir Colab/repo (perintah sekali jalan, toggle flag, versi pustaka) & verifikasi reproduksibilitas. | Membuat visualisasi contoh berhasil & contoh gagal (kedua mask awal salah), serta menulis Pembahasan (termasuk perbandingan BALD-SAM) & keterbatasan. |
| **Presentasi** | Menjelaskan desain eksperimen, split COCO, hasil uji kuantitatif, & kesimpulan hipotesis. | Mendemokan/menjelaskan alur kode SAM 2, pengaturan FP32 Colab, & modul perbaikan + ablasi. | Menjelaskan temuan literatur, analisis kualitatif (berhasil/gagal), & perbedaan dengan BALD-SAM. |

---

## 5. Roadmap Kerja 3 Minggu (27 Nov – 15 Des 2026)

| Sprint & Tenggat | Target Utama | Poin | Checklist Aksi |
| :--- | :--- | :-: | :--- |
| **Sprint 1**<br>27 Nov – 1 Des 2026<br>*(23.59 WIB)* | **Tahap 1 · Pendahuluan** | **15** | - [x] Cek daftar Kelas A & laporkan **P04** + anggota ke koordinator kelas.<br>- [ ] Jalankan 1 gambar & 1 titik di Colab (`sam2_hiera_tiny.pt`, FP32 bila perlu) dan simpan hasilnya.<br>- [ ] Tulis Pendahuluan sesuai rincian [TAHAP1_BREAKDOWN_PENDAHULUAN.md](./TAHAP1_BREAKDOWN_PENDAHULUAN.md) (masalah, urgensi, keterbatasan 1-titik, tujuan, hipotesis, ringkasan perbaikan, Daftar Pustaka).<br>- [ ] Kumpulkan draf Tahap 1 sebelum **Selasa, 1 Des 2026, 23.59 WIB**. |
| **Sprint 2**<br>2 – 8 Des 2026<br>*(23.59 WIB)* | **Tahap 2 · Metode & Hasil Awal** | **30** | - [ ] Siapkan subset COCO (Val & Test terpisah) + simpan titik awal `p1` deterministik.<br>- [ ] Jalankan `baseline_1pt` pada Validasi dan catat angka baseline.<br>- [ ] Terapkan modul perbaikan `proposed_consensus_2pt` + `ablation_bestmask_2pt` (*toggleable*).<br>- [ ] Tampilkan hasil baseline + 1 bukti prototipe berjalan pada Validasi di naskah sesuai [TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md](./TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md).<br>- [ ] Pastikan repo GitHub Public (atau ZIP) + perintah menjalankan kode tertulis di paper.<br>- [ ] Kumpulkan Tahap 2 sebelum **Selasa, 8 Des 2026, 23.59 WIB**. |
| **Sprint 3**<br>9 – 15 Des 2026<br>*(23.59 WIB)* | **Tahap 3 · Paper Lengkap & Kode Akhir** | **55** | - [ ] Jalankan evaluasi final pada Test Set untuk `baseline_1pt`, `ablation_bestmask_2pt`, dan `proposed_consensus_2pt`.<br>- [ ] Hitung IoU, rata-rata jumlah titik, selisih berpasangan, & biaya komputasi.<br>- [ ] Pilih & visualisasikan $\ge 1$ contoh berhasil dan $\ge 1$ contoh gagal (kedua mask awal salah).<br>- [ ] Tulis Pembahasan (perbandingan dengan BALD-SAM, keterbatasan) + Abstrak + Kesimpulan + kontribusi tiap anggota sesuai [TAHAP3_BREAKDOWN_PAPER_LENGKAP.md](./TAHAP3_BREAKDOWN_PAPER_LENGKAP.md).<br>- [ ] Kumpulkan paper lengkap, kode akhir, & petunjuk mengulang eksperimen sebelum **Selasa, 15 Des 2026, 23.59 WIB**. |

---

## 6. Strategi "Nilai Maksimal Dulu, Siap Publikasi Belakangan"

Agar fokus utama tetap aman mengejar **100 poin rubrik matkul** dalam 3 minggu, tetapi tidak perlu mengulang eksperimen dari nol jika hasilnya bagus untuk publikasi:
1. **Simpan log per-objek sejak hari pertama** (`results_val.csv` dan `results_test.csv` berisi `image_id`, `ann_id`, `category_id`, `area`, `iou_m1_m2`, `triggered_2pt`, `iou_baseline`, `iou_ablation`, `iou_proposed`, `time_ms`). Dengan log ini, uji statistik berpasangan (*paired t-test / Wilcoxon*) dan analisis per-ukuran objek bisa langsung dibuat kapan saja.
2. **Catat minimal 2 karya terdekat selain SAM 2** selama menulis Pembahasan (salah satunya sudah diberikan paket: **BALD-SAM**; tambahkan satu lagi studi segmentasi interaktif/refinement titik atau *uncertainty-based prompting*).
3. **Jaga kode tetap modular dan bersih**: pisahkan loader dataset dari logika predictor SAM 2, sehingga jika setelah UAS ingin menguji pada **dataset kedua** (misalnya LVIS, DAVIS frame, atau citra medis/satelit) untuk kebutuhan publikasi, cukup menambah loader dataset baru tanpa mengubah logika inti.
