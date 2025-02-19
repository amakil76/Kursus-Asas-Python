import random

# Simpan skor
skor_pemain = 0
skor_komputer = 0

while True:
    pilihan = ["batu", "gunting", "kertas"]
    pemain = input("Pilih batu, gunting, atau kertas (atau 'exit' untuk keluar): ").lower()

    if pemain == "exit":
        break  # Keluar dari permainan

    if pemain not in pilihan:
        print("Pilihan tidak sah! Sila cuba lagi.")
        continue

    komputer = random.choice(pilihan)
    print(f"Komputer memilih: {komputer}")

    if pemain == komputer:
        print("Seri!")
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("Anda menang! 🎉")
        skor_pemain += 1
    else:
        print("Anda kalah! 😢")
        skor_komputer += 1

    print(f"Skor: Anda {skor_pemain} - {skor_komputer} Komputer")

print("Terima kasih kerana bermain!")
