import numpy as np

# Membuat matriks koefisien
A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [3, 2, 4]
])

# Membuat matriks konstanta
b = np.array([7, 13, 19])

# Menghitung solusi SPL
hasil = np.linalg.solve(A, b)

# Menampilkan hasil
print("Hasil Penyelesaian SPL 3 Variabel")
print("--------------------------------")
print("Nilai x =", hasil[0])
print("Nilai y =", hasil[1])
print("Nilai z =", hasil[2])

# Verifikasi hasil
cek = np.dot(A, hasil)

print("\nHasil Verifikasi:", cek)
print("Konstanta Awal  :", b)
