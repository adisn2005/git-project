B = int(input("Masukkan angka : "))

def hasil(z):
    if B % 2 == 0:
        print(f"Bilangan adalah genap")
    
    else:
        print(f"Bilangan adalah ganjil")

hasil(B)

print(f"{20*"="}")

def hasil(b = 10):
    if b % 2 == 0:
        print(f"Bilangan adalah genap")
    
    else:
        print(f"Bilangan adalah ganjil")

jumlah = int(input("Masukkan jumlah pengecekan angka : "))
for i in range(jumlah):
    a = int(input(f"Masukkan angka ke {i+1} : "))
    c = hasil(a)

print("Angka default")
hasil(B)

print(f"{20*"="}")

def func(*angka):
    for i in angka:
        if i % 2 == 0:
            print(f"{i} adalah bilangan genap")
        else:
            print(f"{i} adalah bilangan ganjil")

angkalist = input("Masukkan angka (pisah dengan spasi): ")
L = []

for j in angkalist.split():
    L.append(int(j)) 

func(*L)