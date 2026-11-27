# Breakdown Progres Tahap 3 — Paper Lengkap & Kode Akhir (Paket P04 · SAM 2)

> **Dokumen Acuan**: [README.md](./README.md) · [BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md) · [TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md](./TAHAP2_BREAKDOWN_METODE_HASIL_AWAL.md)  
> **Laman Tugas Resmi**: [Panduan Proyek Akhir Deep Learning S1 Kelas A](https://brone.ub.ac.id/mod/page/view.php?id=246059)

---

## 1. Ringkasan Administratif & Target Nilai (Tahap 3)

| Komponen | Ketentuan Resmi Tahap 3 |
| :--- | :--- |
| **Dibuka** | Selasa, 24 November 2026, 00.00 WIB |
| **Tenggat Pengumpulan** | **Selasa, 15 Desember 2026, 23.59 WIB** *(Minggu 3 / Final)* |
| **Bobot Nilai** | **55 poin** *(15 poin Implementasi Akhir + 25 poin Bukti & Analisis + 15 poin Dokumentasi & Presentasi)* |
| **Rubrik Penilaian Tahap 3** | • **Implementasi akhir (15 poin)**: *"Implementasi sesuai paket, dapat dijalankan, dan dapat dibandingkan dengan metode asli."*<br>• **Bukti dan analisis (25 poin)**: *"Data uji terpisah, pembanding adil, uji komponen, serta analisis biaya dan kegagalan."*<br>• **Dokumentasi dan presentasi (15 poin)**: *"Langkah reproduksi jelas dan setiap anggota memahami kontribusinya."* |
| **Format Berkas** | **1 file PDF paper lengkap** + **kode akhir** lewat tautan repositori yang dapat diakses dosen di dalam paper *(atau 1 file ZIP)* + **petunjuk lengkap untuk mengulang eksperimen**. |
| **Mekanisme Unggah** | Diunggah oleh **1 perwakilan tim** |
| **Identitas Wajib di Paper** | Judul paper, kode paket (`P04`), nama lengkap & NIM seluruh anggota (`245150207111054`, `245150207111008`, `245150207111103`), serta **kontribusi setiap anggota**. |

---

## 2. Breakdown Struktur Wajib Paper Lengkap (7 Bagian + Kontribusi)

Berbeda dengan Tahap 1 dan 2, pada Tahap 3 naskah harus sudah berbentuk **paper ilmiah utuh**:

| Urutan Bagian | Isi Wajib (Khusus P04 · SAM 2) | Penanggung Jawab Utama |
| :-: | :--- | :--- |
| **0. Header & Abstrak** | • Judul paper, kode paket `P04`, nama & NIM semua anggota.<br>• **Abstrak**: ringkasan masalah ambiguitas 1-titik SAM 2, metode kesepakatan dua mask (`IoU < 0,6` + erosi $3\times 3$), hasil kuantitatif utama pada data uji COCO, dan kesimpulan singkat. | **Raditya** |
| **1. Pendahuluan** | • Versi final dari Tahap 1 (pastikan istilah, angka ambang, dan tujuan selaras dengan isi Metode dan Hasil final). | **Sulthon** & **Raditya** |
| **2. Metode** | • Versi final dari Tahap 2 (metode asli SAM 2, perbaikan modular, split Validasi vs Uji COCO, penentuan `p1` deterministik, metrik, commit, versi library, checkpoint `sam2_hiera_tiny.pt`, GPU Colab & FP32).<br>• Sertakan **petunjuk mengulang eksperimen** yang jelas (langkah dari clone repo sampai menghasilkan tabel uji). | **Gibran** & **Raditya** |
| **3. Hasil** | • **Tabel hasil data uji (`samples_test.json`)** membandingkan tiga metode pada objek dan titik awal `p1` yang sama:<br>&nbsp;&nbsp;1) **Metode asli**: `baseline_1pt`<br>&nbsp;&nbsp;2) **Pembanding sederhana / ablasi**: `ablation_bestmask_2pt` *(titik ke-2 dari mask terbaik saja)*<br>&nbsp;&nbsp;3) **Metode usulan**: `proposed_consensus_2pt` *(titik ke-2 dari irisan dua mask setelah erosi $3\times 3$)*<br>• Laporkan **IoU terhadap mask acuan** (keseluruhan + khusus kelompok terpicu `IoU < 0,6`), **rata-rata jumlah titik per objek**, **selisih berpasangan ($\Delta\text{IoU}$ per objek)**, serta **waktu inferensi**. | **Raditya** |
| **4. Pembahasan** | • **Analisis Kinerja**: apakah metode usulan unggul atas 1-titik dan titik ke-2 dari mask terbaik? Bagaimana jika hasil belum/sudah membaik? *(Catatan panduan: hasil yang belum menunjukkan perbaikan tetap dinilai dari kualitas pengujian dan analisis).*<br>• **Biaya Komputasi**: tambahan waktu tahap kedua (dibandingkan dengan pemakaian ulang *image embedding* `set_image()`).<br>• **Contoh Berhasil ($\ge 1$)**: visualisasi lengkap dari `p1` hingga mask akhir melampaui baseline.<br>• **Contoh Gagal ($\ge 1$ — Wajib P04)**: **kasus ketika kedua mask awal ($M_1$ dan $M_2$) sama-sama salah** sehingga irisan keduanya tetap mengarahkan `p2` ke wilayah keliru.<br>• **Keterbatasan & Perbandingan Literatur**: jelaskan perbedaan aturan heuristik kesepakatan mask ini dengan pendekatan berbasis ketidakpastian untuk anotasi interaktif pada **[BALD-SAM](https://arxiv.org/abs/2603.10828)**. | **Sulthon** |
| **5. Kesimpulan** | • **Jawab hipotesis secara eksplisit** (apakah hipotesis $H_1$ terkonfirmasi, terkonfirmasi sebagian pada subkelompok tertentu, atau ditolak pada data uji).<br>• Ringkas implikasi praktis dan arah perbaikan lanjutan. | **Raditya** |
| **6. Kontribusi Setiap Anggota & Daftar Pustaka** | • **Kontribusi setiap anggota** ditulis eksplisit (Raditya, Gibran, Sulthon — sesuaikan dengan kontribusi aktual di repo & paper).<br>• **Daftar Pustaka** lengkap dan konsisten untuk seluruh sitasi di naskah (SAM 2, SAM, COCO, BALD-SAM, dll.). | **Semua** *(kompilasi oleh Raditya)* |

---

## 3. Syarat Kode Akhir & Reproduksibilitas (15 Poin)

Berbeda dari Tahap 2 yang hanya meminta *"perintah untuk menjalankan kode"*, Tahap 3 menuntut **"petunjuk untuk mengulang eksperimen"** secara lengkap:
1. **Repo GitHub Public (atau ZIP)** bersih dan terstruktur (`README.md`, `src/`, `notebooks/`, `configs/`, `results/`).
2. **`README.md` Final** memuat langkah *end-to-end*:
   - Clone repo & instalasi dependensi (`sam2` commit hash + library versi tercatat).
   - Cara unduh checkpoint `sam2_hiera_tiny.pt` dan subset COCO `val2017` (atau mount Drive).
   - Perintah untuk mereproduksi:
     - `baseline_1pt`
     - `ablation_bestmask_2pt`
     - `proposed_consensus_2pt`
   - Cara menghasilkan tabel hasil (`results_test.csv`) dan gambar visualisasi berhasil/gagal.
3. **Kode Modular**: Flag/parameter untuk mengaktifkan & mematikan perbaikan serta mengubah mode pembanding terlihat jelas di kode.

---

## 4. Pembagian Kerja & Timeline Minggu 3 (9 – 15 Des 2026)

| Rentang Waktu | **Raditya** (`245150207111054`)<br>*Lead Naskah, Repo & Pipeline COCO* | **Gibran** (`245150207111008`)<br>*Google Colab & Teknis SAM 2* | **Sulthon** (`245150207111103`)<br>*Review Paper, Literatur & Analisis* |
| :--- | :--- | :--- | :--- |
| **9 – 11 Des**<br>*(Rabu–Jumat)* | Jalankan evaluasi final di **Data Uji (`samples_test.json`)** untuk ketiga metode (`baseline_1pt`, `ablation_bestmask_2pt`, `proposed_consensus_2pt`) & simpan `results_test.csv`. | Lengkapi benchmark waktu inferensi (*overhead* tahap 2, reuse `set_image`), rapikan kode modular & buat petunjuk reproduksi di `README.md`. | Dari `results_test.csv`, seleksi kandidat **contoh berhasil** terbaik & **contoh gagal (kedua mask awal salah)**; mulai draf **Pembahasan** (termasuk perbandingan BALD-SAM). |
| **12 – 13 Des**<br>*(Sabtu–Minggu)* | Olah tabel final data uji, hitung $\Delta\text{IoU}$ per objek, dan tulis **Abstrak**, **Hasil**, **Kesimpulan**, & **Kontribusi Anggota**. | Uji ulang *clean run* notebook/skrip dari awal di Colab (memastikan tidak ada sel rusak/hardcoded path lokal) dan finalisasi bagian **Metode** + perintah reproduksi. | Selesaikan gambar visualisasi panel berhasil & gagal beresolusi rapi, lengkapi analisis keterbatasan & finalisasi **Pembahasan** + **Daftar Pustaka**. |
| **14 Des**<br>*(Senin)* | Gabungkan naskah lengkap 7 bagian, lakukan review silang & **latihan presentasi singkat** bertiga (pastikan tiap anggota paham isi seluruh paper). | Final tag/commit kode di GitHub (`Public`), cek ulang seluruh link di PDF mengarah ke commit final. | Finalisasi proofread tata bahasa, sitasi, nomor gambar/tabel, & konsistensi angka di teks vs tabel. |
| **15 Des**<br>*(Selasa < 23.59 WIB)* | Ekspor **PDF final** (QC lengkap), unggah ke Brone jauh sebelum 23.59 WIB. | — | — |

---

## 5. Checklist Quality Control (QC) Sebelum Unggah Tahap 3 & Presentasi

- [ ] Naskah memuat **7 bagian wajib**: Abstrak, Pendahuluan, Metode, Hasil, Pembahasan, Kesimpulan, Daftar Pustaka.
- [ ] Identitas lengkap tercantum: Judul paper, kode paket `P04`, nama & NIM seluruh anggota, dan **kontribusi setiap anggota**.
- [ ] Tabel data uji membandingkan **3 metode adil** (`baseline_1pt`, `ablation_bestmask_2pt`, `proposed_consensus_2pt`) pada objek & titik awal `p1` yang sama, dengan metrik **IoU** dan **rata-rata jumlah titik**.
- [ ] Pembahasan mencakup: **kinerja**, **biaya komputasi**, **$\ge 1$ contoh berhasil**, **$\ge 1$ contoh gagal (kedua mask awal salah)**, **keterbatasan**, dan perbedaan dengan **BALD-SAM**.
- [ ] Kesimpulan **menjawab hipotesis** secara tegas berdasarkan angka data uji.
- [ ] **Tautan repositori Public** (atau ZIP) + **petunjuk mengulang eksperimen** tercantum jelas dan sudah diuji jalan ulang (*clean run*).
- [ ] **Persiapan Presentasi**: Raditya, Gibran, dan Sulthon masing-masing siap menjelaskan kontribusinya dan menjawab pertanyaan tentang keputusan eksperimen (misal alasan FP32, ambang `0.6`, erosi `3×3`, split COCO, dan temuan kegagalan).
