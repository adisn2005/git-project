G = 10

def globalFunction():
    print(f"G = {G}")

globalFunction()
print(G)

print(f"{20*"="}")

def localFunction():
    L = 5
    print(f"L = {L}")

localFunction()

print(f"{20*"="}")

def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print (f"Luas segitiga: {luas}")

luas_segitiga(4, 6)

print(f"{20*"="}")

def nama(nama):
    print(f"Halo, nama saya {nama}")

nama("Adi")
nama("Surya")

print(f"{20*"="}")

def funcArgs(*angka):
    print(f"Angka terakhir yang dimasukkan yaitu : {angka[-1]}")

funcArgs(1, 2, 3, 4, 5)

print(f"{20*"="}")

def funcArgs(*angka):
    print(f"Angka yang dimasukkan yaitu : {angka[:]}")

funcArgs(1, 2, 3, 4, 5)

print(f"{20*"="}")

def nama(buah):
    for i in buah:
        print(i)

buah = []
I = str(input("Masukkan nama buah : "))
buah.append(I)

nama(buah)