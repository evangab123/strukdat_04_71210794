import json

with open('mahasiswa.json','r') as file:
    data = json.load(file)
    n = int(input("Masukan jumlah mahasiswa baru : "))
    for i in range(0,n): 
        nama = input("Masukan nama anda : ") 
        count = 1
        n_hobi = int(input('Masukan jumlah hobi : '))
        hobi_list =list()
        for j in range(0,n_hobi):
            hobi = input('masukan hobi ke-'+str(count)+' : ')
            count += 1
            hobi_list.append(hobi)  
        prestasi = input("Masukan prestasi Anda : ")
        data = {nama:[]}
        biodata = list()
        biodata.append({'Hobi': hobi_list})
        biodata.append({'Prestasi':prestasi})
        data[nama].append({'Biodata':biodata})
        print("=== Data berhasil ditambahkan ===\n")      

with open('mahasiswa.json','a') as file:
     data = json.dump(data,file)   
