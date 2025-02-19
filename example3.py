#Pilih beberapa item secara rawak
import random

warna = ["merah", "biru", "hijau", "kuning", "hitam"]
pilihan = random.sample(warna, 2)  # Pilih 2 item tanpa pengulangan
print("Warna yang dipilih:", pilihan)
