# Program menghitung jumlah bilangan 1 sampai n
# Input: bilangan bulat positif
# Proses: menjumlahkan 1 sampai n menggunakan for
# Output: jumlah bilangan

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")