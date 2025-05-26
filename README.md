# Project_Struktur_Data_Kelompok-9
Tugas UAS Struktur Data - Membuat Peta dan GPS Sederhana

Tujuan dari tugas ini adalah membuat representasi **graph** peta dengan 10 kota sebagai *vertex* dan 30 jalur sebagai *edge*, serta menerapkan algoritma **Dijkstra** dan **TSP (Traveling Salesman Problem).**

Setiap mode transportasi memiliki graph (peta) sendiri dengan bobot berbeda yang merepresentasikan **waktu tempuh** antar kota.

### **📋 Instruksi Tugas:**

### **1. Representasi Grafik:**

1. Implementasikan struktur data graph dalam bahasa Python.
2. Buat 1 graph
3. Tiap graph harus memiliki:
    - **10 vertex** (nama kota bisa bebas).
    - **30 edge** yang mewakili jalan antar kota.
    - Bobot berupa **perkiraan waktu tempuh** dalam kilometer.
4. Pastikan semua graph **terhubung** (*connected graph*).
5. Jelaskan dan gambarkan ketiga graph di laporan (gambar manual/digital).

---

### **2. Algoritma Shortest Path dan TSP:**

### **A. Dijkstra (untuk ketiga graph):**

1. Terapkan algoritma **Dijkstra** untuk menemukan rute tercepat dari **kota sumber ke kota tujuan**, untuk masing-masing mode transportasi.
2. Minta pengguna untuk memilih:
    - **Kota asal dan kota tujuan**
3. Tampilkan:
    - **Jalur tercepat**
    - **Total jarak ditempuh**
4. Jelaskan cara kerja algoritma Dijkstra di laporan.

### **B. Traveling Salesman Problem:**

1. Terapkan algoritma **TSP sederhana** (brute-force) untuk masing-masing graph.
2. Temukan urutan perjalanan paling efisien yang mengunjungi semua kota **sekali**.
3. Tampilkan:
    - **Rute TSP terbaik**
    - **Total jarak tempuh**
4. Jelaskan Algoritma dan cara kerja TSP di laporan.
