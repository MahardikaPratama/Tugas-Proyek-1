import os
import fileinput
import sys
#Modul untuk mmenampilkan menu
def tampilMenu():
    print("Menu")
    print("1. Tambah Kontak")
    print("2. Tampilkan Semua Kontak")
    print("3. Hapus Kontak")
    print("4. Update Kontak")
    print("5. Cari Kontak")
    print("6. Keluar Program")


#function boolean untuk mencari data dalam file
def searchData(nama, nomor):
    with open("Kontak.txt", "r") as file:    
        for line in file:
            simpan = line.split(" ")
            if simpan[0] == nama or simpan[1][:-1] == nomor:
                return True, simpan
        return False, None
        

#funtion boolean untuk cek data agar tidak sama
def cekData(nama, nomor):
    sama, simpan = searchData(nama, nomor)
    if sama == True:
        print("Nama atau nomor telah digunakan sebelumnya, silahkan masukkan data lain")
        return True
    else:
        return False

#Modul untuk menambah kontak
def tambahKontak():
    cek = True
    while cek == True:
        nama = input("Nama : ")
        nomor = input("Nomor : ")
        cek = cekData(nama, nomor)
    
    with open("Kontak.txt", "a") as file:
        file.write(nama + " " + nomor + "\n")
    print("Berhasil Menambakan Nomor")

#modul untuk menampilkan kontak
def tampilKontak():
    file_path = "D:\Python/Kontak.txt"
    if(not(os.path.getsize(file_path) == 0)):
        print("No".ljust(3,' ')+"Nama".ljust(10,' ')+"Nomor")
        no = 1
        with open("Kontak.txt", "r") as file:           
            for line in file:
                simpan = line.split(" ")
                print(str(no) + ". "+simpan[0].ljust(10,' ')+simpan[1][:-1])
                no = no + 1
        
    
    
#modul untuk mencari kontak
def cariKontak():
    ketemu = False
    file_path = "D:\Python/Kontak.txt"
    if(not(os.path.getsize(file_path) == 0)):       
        print("Cari berdasarkan : ")
        print("1. Nama")
        print("2. Nomor")
        pilih = int(input("Masukkan pilihan anda : "))
        match pilih: 
            case 1:
                nama = input("Masukkan nama kontak yang dicari : ")
                nomor = 0
                hasil = searchData(nama, nomor)
                ketemu = hasil[0]
                if ketemu == True:
                    print("Nama : "+ hasil[1][0])
                    print("Nomor: "+ hasil[1][1])
                elif ketemu == False:
                    print("Nama tidak ada di kontak")
            case 2:
                nomor = input("Masukkan nomor kontak yang dicari : ")
                nama = 0
                hasil = searchData(nama, nomor)
                ketemu = hasil[0]
                if ketemu == True:
                    print("Nama : "+ hasil[1][0])
                    print("Nomor: "+ hasil[1][1])
                elif ketemu == False:
                    print("Nomor tidak ada di kontak")
            case other:
                print("Masukkan tidak valid")

#modul untuk menghapus kontak
def hapusKontak():
    file_path = "D:\Python/Kontak.txt"
    if(not(os.path.getsize(file_path) == 0)):
        tampilKontak()
        option = int(input("Pilih kontak yang akan dihapus : "))
        
        with open("Kontak.txt", "r") as file:
            data = file.readlines()
        
        os.remove("Kontak.txt")
        with open("Kontak.txt", "a") as file:
            for i in range(len(data)):
                if (i + 1) != option:
                    file.write(data[i])
        print("Kontak berhasil dihapus")
    else:
        print("Data Masih Kosong")
        
        
#modul untuk mengedit nomor kontak
def editKontak():
    file_path = "D:\Python/Kontak.txt"
    if(not(os.path.getsize(file_path) == 0)):
        nama = input("Masukkan nama kontak yang akan diubah nomornya : ")
        ketemu = searchData(nama, "temp")
        if ketemu[0] == True :
            with open("Kontak.txt", "r") as file:
                data = file.readlines()
            
            with open("Kontak.txt", "w") as file:
                for line in data:
                    if line.startswith(nama):
                        nomor = input("Masukkan nomor telepon baru: ")    
                        line = nama + " " + nomor + "\n"
                    file.write(line)
            print("Nomor kontak berhasil diubah")
        else:
            print("Data tidak ada di kontak")
    else:
        print("Data masih kosong")

#Main Program
opsi = 0
while opsi != 6:
    tampilMenu()
    try:
        opsi = int(input("Masukkan pilihan anda : "))
        if opsi == 1:
            tambahKontak()
        elif opsi == 2:
            tampilKontak()
        elif opsi == 3:
            hapusKontak()
        elif opsi == 4:
            editKontak()
        elif opsi == 5:
            cariKontak()
        elif opsi == 6:
            print("Keluar Program")
            sys.exit()
        else:
            print("Masukkan tidak valid")
    except ValueError:
        print("Inputan harus berupa angka")
