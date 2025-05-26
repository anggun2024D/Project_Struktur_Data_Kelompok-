# Project_Struktur_Data_Kelompok-9
Tugas UAS Struktur Data - Membuat Peta dan GPS Sederhana

Repositori ini merupakan hasil tugas akhir mata kuliah **Struktur Data** yang mengimplementasikan struktur data **graph** berbobot tidak berarah untuk membangun **peta dan sistem GPS sederhana** antar kota di Inggris. Program ditulis menggunakan bahasa **Python** dan dilengkapi dengan visualisasi graf menggunakan pustaka `networkx` dan `matplotlib`.

---

## ✨ Fitur Utama

- ✅ Representasi **graph** dengan 10 vertex (kota) dan 30 edge (jalur)
- ✅ Implementasi algoritma **Dijkstra** untuk mencari rute tercepat antar dua kota
- ✅ Simulasi algoritma **TSP (Traveling Salesman Problem)** dengan brute-force
- ✅ Input interaktif dari pengguna (kota asal & tujuan)
- ✅ Visualisasi grafis dengan highlight pada jalur terpendek

---

## 🗂️ Struktur File

|   File / Folder   |                     Deskripsi                  |
|-------------------|------------------------------------------------|
| `peta_inggris.py` | File utama program Python                      |
| `README.md`       | Dokumentasi repositori                         |

---

## ▶️ Cara Menjalankan Program

1. Pastikan kamu sudah menginstall **Python 3.x**  
2. Install pustaka yang dibutuhkan:
   ```bash
   pip install networkx matplotlib
   
3. Jalankan program:
python main.py

4. Masukkan kota asal dan tujuan sesuai daftar yang tersedia.
   Masukkan kota asal     : Oxford
   Masukkan kota tujuan   : Edinburgh

5. Program akan menampilkan: Jalur tercepat (Dijkstra), Total jarak tempuh, Rute optimal TSP (mengunjungi semua kota sekali), dan Visualisasi graf
