import json
with open('mahasiswa.json', 'r') as file:
    mahasiswa = json.load(file)
    
    jumlah = int(input("Masukan jumlah mahasiswa baru : "))
    
    for i in range(0,jumlah):
        nama = input("Masukan nama anda : ")
        listnama = []
        kosong = {}
        jum_hobi = int(input("Masukan jumlah hobi : "))
        listhobi = []
        for j in range(1,jum_hobi+1):
            hobi1 = input("Masukan Hobi ke-"+ str(j) +": ")
            listhobi.append(hobi1)
        prestasi = input("Masukan prestasi anda : ")
        listnama.append({"BioData":{"Hobi":listhobi,"Prestasi":prestasi}})
        mahasiswa[nama] = listnama
        print("=== Data Berhasil ditambahkan ===")
        print()

with open('mahasiswa.json', 'w') as file:
    json.dump(mahasiswa, file)
