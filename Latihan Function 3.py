def hitung_selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
   
    waktu_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    waktu_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    if waktu_selesai <= waktu_mulai:
        print("\nWaktu selesai harus lebih besar dari waktu mulai!")
        return None

    selisih = waktu_selesai - waktu_mulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60

    return jam, menit, detik


print("=== Hitung Selisih Waktu ===")

jm = int(input("Jam mulai   : "))
mm = int(input("Menit mulai : "))
dm = int(input("Detik mulai : "))

js = int(input("Jam selesai   : "))
ms = int(input("Menit selesai : "))
ds = int(input("Detik selesai : "))

hasil = hitung_selisih(jm, mm, dm, js, ms, ds)

jam, menit, detik = hasil
print(f"\nSelisih waktu: {jam} jam - {menit} menit - {detik} detik")