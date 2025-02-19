#Pilih beberapa item secara rawak dari senarai
import random

makanan = ["nasi lemak", "roti canai", "mee goreng", "satay", "laksa"]
pilihan = random.sample(makanan, 2)  # Pilih 2 makanan tanpa pengulangan
print("Makanan yang dipilih:", pilihan)
