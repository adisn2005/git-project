print("Login dengan 3 kali kesempatan Admin")

def login():
    kesempatan = 3
    for i in range(kesempatan):
        user = "Daspro123"
        pw = input("Masukkan password : ")
        
        if user == "Daspro123" and pw == "Latihan":
            print("Login berhasil! Selamat datang, Daspro123!")
            break
        
        else:
            kesempatan -= 1
            print(f"Username atau Password salah! Sisa {kesempatan} kesempatan lagi!")
    else:
        print("Kesempatan habis! Mengeluarkan user dari laman login...")

login()