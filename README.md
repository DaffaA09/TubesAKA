# TubesAKA

# Implementasi Linear Search Iteratif

Pendekatan iteratif melakukan pencarian dengan menggunakan perulangan untuk memeriksa setiap elemen durasi lagu secara berurutan, dimulai dari elemen pertama hingga elemen terakhir. Proses pencarian akan berhenti ketika durasi lagu yang dicari ditemukan atau seluruh data telah diperiksa.

Contoh Implementasi (Iteratif)

```def linear_search_iterative(arr, target):
    for x in arr:
        if x == target:
            return True
    return False
```

# Implementasi Linear Search Rekursif

Pendekatan rekursif melakukan pencarian dengan memanggil fungsi secara berulang. Pada setiap pemanggilan, fungsi akan memeriksa satu elemen data berdasarkan indeks tertentu, lalu melanjutkan pencarian ke indeks berikutnya hingga durasi lagu ditemukan atau indeks mencapai akhir array.

Contoh Implementasi (Rekursif)
```def linear_search_recursive(arr, target, index=0):
    if index == len(arr):
        return False
    if arr[index] == target:
        return True
    return linear_search_recursive(arr, target, index + 1)

```
