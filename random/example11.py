#Pilih secara rawak dan ulang sebanyak X kali
import random

aktiviti = ["membaca", "bermain bola", "berenang", "melukis", "berbasikal"]
for i in range(3):  # Pilih 3 kali
    print("Cadangan aktiviti: ", str(i+1) , random.choice(aktiviti))
