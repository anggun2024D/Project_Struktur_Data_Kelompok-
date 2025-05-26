
import matplotlib.pyplot as plt
import networkx as nx


# Kelas Peta untuk merepresentasikan peta dengan kota dan jarak antar kota
class Peta:
    # Metode init (inisiasi)
    def __init__(self):
        self.daftarKota = {}
    
    # Metode tambahKota untuk menambah kota
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {} 
    
    # Metode printKota untuk menampilkan kota
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")
    
    # Metode tambahJalan untuk menambah jarak
    def tambahJalan(self, kota1, kota2, jarak):
        #jika kota1 dan kota2 ada di dalam daftarKota maka ditambahkan jaraknya
        if kota1 in self.daftarKota and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    # Metode hapusKota untuk menghapus kota yang di dalam list daftar kota
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
    
    # Metode hapusJalan untuk menghapus jarak yang udah ada di dalam list daftar kota
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

    # Metode rute tempuh untuk menampilkan jarak tempuh dari kota1 ke kota2
    def ruteTempuh(self, kota1, kota2):
        #jika kota1 dan kota2 didalam daftarKota maka menampilkan jaraknya  
        if kota1 in self.daftarKota and kota2 in self.daftarKota: 
            #jika tidak ada yang menghubungkan kota1 ke kota2
            if kota2 in self.daftarKota[kota1]:
                #maka akan muncul harus memasukkan sesuai daftar kota
                print(f"Jarak dari {kota1} ke {kota2} adalah {self.daftarKota[kota1][kota2]} km") 
            else :
                print("kamu harus melewati beberapa kota")
        #jika user menempuh antar kota yang tidak sesuai dengan daftar kota 
        else :
            print ("kamu harus memasukkan sesuai daftar kota")

# Inisialisasi Peta
PetaInggris = ["London", "Oxford", "Cambridge", "Bristol", "Bath", 
               "Birmingham", "Liverpool", "Manchester", "York", "Edinburgh"]

# Membuat instance dari kelas Peta
England = Peta() 
for kota in PetaInggris:
    England.tambahKota(kota)

import heapq

# Fungsi Dijkstra
def dijkstra(graph, start, end): 
    queue = [(0, start, [])]
    visited = set()
    while queue: 
        (cost, node, path) = heapq.heappop(queue)
        if node in visited: 
            continue
        path = path + [node]
        if node == end: 
            return cost, path
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return float("inf"), []

# Menambahkan semua jarak antar kota
England.tambahJalan("London", "Oxford", 96)
England.tambahJalan("London", "Cambridge", 101)
England.tambahJalan("London", "Bristol", 190)
England.tambahJalan("London", "Bath", 185)
England.tambahJalan("London", "Birmingham", 205)
England.tambahJalan("London", "Liverpool", 350)
England.tambahJalan("London", "Manchester", 335)
England.tambahJalan("London", "York", 330)
England.tambahJalan("London", "Edinburgh", 660)
England.tambahJalan("Oxford", "Cambridge", 140)
England.tambahJalan("Oxford", "Bristol", 130)
England.tambahJalan("Oxford", "Bath", 120)
England.tambahJalan("Oxford", "Birmingham", 110)
England.tambahJalan("Oxford", "Liverpool", 250)
England.tambahJalan("Oxford", "Manchester", 235)
England.tambahJalan("Oxford", "York", 230)
England.tambahJalan("Oxford", "Edinburgh", 550)
England.tambahJalan("Cambridge", "Birmingham", 190)
England.tambahJalan("Cambridge", "Liverpool", 305)
England.tambahJalan("Cambridge", "Manchester", 290)
England.tambahJalan("Cambridge", "York", 225)
England.tambahJalan("Cambridge", "Edinburgh", 550)
England.tambahJalan("Bristol", "Bath", 20)
England.tambahJalan("Bristol", "Birmingham", 135)
England.tambahJalan("Bristol", "Manchester", 260)
England.tambahJalan("Bath", "Birmingham", 125)
England.tambahJalan("Birmingham", "Liverpool", 160)
England.tambahJalan("Birmingham", "Manchester", 140)
England.tambahJalan("Birmingham", "York", 170)
England.tambahJalan("Manchester", "York", 105)
England.tambahJalan("York", "Edinburgh", 330)

# Cetak daftar kota
print("\nDAFTAR KOTA:")
England.printKota()

from itertools import permutations

print("\n=== HASIL TSP (Traveling Salesman Problem) ===")

# Fungsi untuk menyelesaikan Traveling Salesman Problem (TSP)
def tsp(graph):
    shortest_distance = float('inf')
    shortest_path = []
    cities = list(graph.keys())

    for path in permutations(cities):
        total_distance = 0
        valid_path = True
        for i in range(len(path) - 1):
            if path[i+1] in graph[path[i]]:
                total_distance += graph[path[i]][path[i+1]]
            else:
                valid_path = False
                break

        # Tambahkan jarak kembali ke kota awal
        if valid_path and path[0] in graph[path[-1]]:
            total_distance += graph[path[-1]][path[0]]
        else:
            valid_path = False
        
        # Simpan path jika jarak total lebih pendek
        if valid_path and total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path + (path[0],) 

    return shortest_path, shortest_distance

# # Menjalankan TSP pada daftar kota
# shortest_path, shortest_distance = tsp(England.daftarKota)

# # Menampilkan hasil TSP
# print("Rute TSP terbaik:")
# print(" ➝ ".join(shortest_path))
# print(f"Total jarak TSP: {shortest_distance} km")

# Input pengguna
print("\nTemukan Rute Tercepat")
lokasi = input("Masukkan kota asal     : ").title()
tujuan = input("Masukkan kota tujuan   : ").title()

# Validasi input
if lokasi not in England.daftarKota or tujuan not in England.daftarKota:
    print("Kota tidak ditemukan dalam daftar!")
else:
    total_cost, route = dijkstra(England.daftarKota, lokasi, tujuan)
    if total_cost == float("inf"):
        print("Tidak ditemukan rute antara kota tersebut.")
    else:
        print(f"\nRute tercepat dari {lokasi} ke {tujuan}:")
        print(" ➝ ".join(route))
        print(f"Total jarak: {total_cost} km")

    # Visualisasi
    G = nx.Graph()
    for u in England.daftarKota:
        for v in England.daftarKota[u]:
            G.add_edge(u, v, weight=England.daftarKota[u][v])

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='LightYellow', node_size=3000, font_size=14, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    
    # Highlight path
    if total_cost != float("inf"):
        path_edges = list(zip(route, route[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='LightGreen', width=4)

    plt.title("Visualisasi Graf Perjalanan")
    plt.axis('off')
    plt.show()
