#Nomor 1 - Fibonacci
def fi(M):
    A1, A2 = 0, 1
    L = []
    for i in range(M):
        L.append(A1)
        A1, A2 = A2, A1 + A2
    return L

M = int(input("Masukkan nilai yang ingin ditampilkan : "))
print(f"Bilangan Fibonacci = {fi(M)}")

#Nomor 2 - Luas Tabung
r = float(input("Masukkan jari-jari : "))
t = float(input("Masukkan tinggi : "))
p = 3.14

def vol(p, r, t):
    v = p * (r*r) * t
    return v

print(f"Volume tabung = {vol(p, r, t)} cm3")

#Nomor 3 - Rata-rata
def H(*angka):
    T = sum(angka)
    R = T / len(angka)
    return T, R

A = input("Masukkan beberapa angka (pisah dengan koma) : ")
L = [float(x) for x in A.split(",")]

T, R = H(*L)   # <-- pakai *L, bukan *angka
print(f"Total = {T}")
print(f"Rata-rata : {R}")