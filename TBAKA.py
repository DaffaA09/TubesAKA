import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)


# Linear Search Rekursif
def linear_search_recursive(arr, target, index=0):
    if index == len(arr):
        return False
    if arr[index] == target:
        return True
    return linear_search_recursive(arr, target, index + 1)


# Linear Search Iteratif
def linear_search_iterative(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

# Penyimpan hasil
n_values = []
recursive_times = []
iterative_times = []


# Cetak tabel sederhana (ms)
def print_table():
    print("\n+----+------------------------+------------------------+")
    print("| n  | Recursive Time (ms)   | Iterative Time (ms)   |")
    print("+----+------------------------+------------------------+")

    for i in range(len(n_values)):
        print(
            f"| {str(n_values[i]).ljust(2)} "
            f"| {format(recursive_times[i], '.6f').ljust(22)} "
            f"| {format(iterative_times[i], '.6f').ljust(22)} |"
        )

    print("+----+------------------------+------------------------+")



# Grafik (ms)

def show_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o')
    plt.title('Performance Comparison\nLinear Search Durasi Lagu')
    plt.xlabel('Jumlah Lagu (n)')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Program Utama

print("=== PERBANDINGAN SEARCHING DURASI LAGU ===")

while True:
    try:
        n = int(input("\nMasukkan jumlah lagu (n) atau -1 untuk keluar: "))

        if n == -1:
            print("Input selesai.")
            break

        if n <= 0:
            print("Masukkan nilai n yang positif!")
            continue

        n_values.append(n)

        # Data durasi lagu: 110, 120, 130, ...
        durasi_lagu = [(i + 11) * 10 for i in range(n)]

        # Cari durasi terakhir
        target = durasi_lagu[-1]

        # ---- Rekursif ----
        start = time.time()
        linear_search_recursive(durasi_lagu, target)
        recursive_times.append((time.time() - start) * 1000)  # ms

        # ---- Iteratif ----
        start = time.time()
        linear_search_iterative(durasi_lagu, target)
        iterative_times.append((time.time() - start) * 1000)  # ms

        # Tampilkan tabel setiap input
        print_table()

    except ValueError:
        print("Masukkan nilai n yang valid!")

# TAMPILKAN GRAFIK SEKALI
if n_values:
    show_graph()
