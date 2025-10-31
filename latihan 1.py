
from random import random

n = int(input("Masukkan nilai N: "))

i = 1
while i <= n:
    nilai = random()
    if nilai < 0.5:
        print(f"data ke: {i} => {nilai}")
        i += 1

print("Selesai")


