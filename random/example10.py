#Pilih item secara rawak & buang dari senarai
import random

haiwan = ["kucing", "anjing", "burung", "ikan", "arnab"]
pilihan = random.choice(haiwan)  # Pilih satu secara rawak
haiwan.remove(pilihan)  # Buang item yang dipilih dari senarai
print("Haiwan dipilih:", pilihan)
print("Senarai haiwan sekarang:", haiwan)
