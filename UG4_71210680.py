import json
with open('mahasiswa.json', 'r') as file:
    mahasiswa = json.load(file)

jumlah = int(input("Masukan jumlah mahasiswa baru : "))
for i in range(jumlah):
    nama = input("Masukan nama anda : ")
    jum_hobi = int(input("Masukan jumlah hobi : "))
    for j in range(1,jum_hobi+1):
        hobi1 = input("Masukan Hobi "+ str(j) +": ")
    prestasi = input("Masukan prestasi anda : ")
    print("=== Data Berhasil ditambahkan ===")

with open('mahasiswa.json', 'a') as file:
    json.dump(mahasiswa, file)