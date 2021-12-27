
#RANGKUMAN PYTHON 3.1

#1. STRING	

#|k |o |t |a |  |b |e |k |a | s| i |
#0  1  2  3  4  5  6  7  8  9  10  11
text = "kota bekasi"
a= text[2:7] 	#("artinya memilih string  2 sampai 5 ="ta bek") -1 terhitung dari belakang

#2. List
    angka1 =[10,20,30,40,50,60,70]
    angka2 = [1,4,7,5,7,3]

    # memilih arsiran list
    data1 = angka1[2:5] # ("memilih baris ke2 sampai 5= 30,40,50")
    data2 = angka1 [3:] # ("memilih baris ke 3 sampai akhir")
    data3 = angka1 [:5] # ("memilih dari awal sampai ke baris 5")
    
    # menambahkan bukan menjumlahkan data pada 2 variabel list
    data_all=angka1+angka2  #hasilnya adalah [10,20,30,40,50,60,70,1,4,7,5,7,3]

    # Mengubah konten/isi list
    angka1[3]=90        # nilai angka1 40 menjadi 90
    ubah_angka=angka1[:] # jika nilai ingin ubah_angka di ubah , angka1 (data utama)tidak akan diubah 
    ubah_angka[1]=101  # jadi yang di ubah hanya nilai ubah_angka aja tanpa mengubah nilai angka1
    ubah_angka[2:4]=[23,24] # mengubah nilai list lebih dari 1

    #mengambil nilai dari list di dalam list
                                        angka1               angka2
                                   0  1  2  3  4  5  6    0 1 2 3 4 5
    x= [angka1,angka2]  #hasil = [[10,20,30,40,50,60,70],[1,4,7,5,7,3]]
    y=x[0][3]           #hasil = 40 (angka1 masuk baris ke 0 nilai baris ke3)

    #methode pada list mengisi,mengurangi dll
    angka1.append(80)   # hasil = [10,20,30,40,50,60,70,80] nilai 80 di tambahkan di belakang baris

    # fungtion pada list
    banyak_angka = len(angka1) # hasil= 8 ,menampilkan banyaknya jumlah anggota list dari 10-80 =8

3. IF ELSE

    nilai = 80

    if nilai == 80:
        print("nilai anda adalah =",nilai) # menggunakan ==

    if nilai is 80:
        print("nilai anda adalah =",nilai) # menggunakan is

    if nilai is not 80:
        print("nilai anda adalah =",nilai) # menggunakan is not

    # NESTING IF (IF DI DALAM IF) #
    if nilai >= 50:
        if nilai <=100: # jika if pertama tidak memenuhi syarat maka if ke2 tidak akam di jalankan
            print ("SELAMAT ANDA LULUS DENGAN NILAI =",nilai) 

    
    # ELIF # ELSE
    if 90 <= nilai >= 100:
        print("anda lulus dengan predikat A dengan nilai =",nilai)
    elif 80 <= nilai >= 90:
        print("anda lulus dengan predikat B dengan nilai =",nilai) # elif akan memberikan parameter tambahan dari if
    elif 70 <= nilai >= 80:
        print("anda lulus dengan predikat c dengan nilai =",nilai) 
    elif 60 <= nilai >= 70:
        print("anda lulus dengan predikat D dengan nilai =",nilai)
    else:
        print("anda tidak lulus")                                  # else akan memberikan nilai parameter selain if dan elif

    # IF DENGAN LIST natural language
    Buah=["mangga","apel","jeruk","manggis","pisang"]    # if dan if not https://terpadumayestik:t3rp4dum4y3st1k!!@soadki.jakarta.go.id/rest/gov/dki/platno/ws/plat?plat=b2457kui
    inputnamabuah = input("masukan nama Buah =")
    if inputnamabuah in Buah:
        print("nama yang anda masukan telah terdaftar")
    if not inputnamabuah in Buah:
        print("nama yang anda masukan tidak ada terdaftar")
        Buah.append(inputnamabuah)
        print ("Buah yang anda daftarkan adalah =",inputnamabuah)



4. #FOR looping
    # FOR
    Buah=["mangga","apel","jeruk","manggis","pisang"]

    for B in Buah:
        print(B)        # print anggota dari list
        print (len(B))  # print anggota dari list dan panjang / banyak karakternya)
    
    #FOR range
    angka=25
    for i in range(0,10,2): #print angka 0 sampai 10 kelipatan 2
        print (i)
        if angka is i:
            print ("angka ditemukan= ",angka)
    else:
        print ("angka tidak ditemukan") # pemberian else sejajar dengan for bukan dengan if\

    #BREAK
    for i in range(1,10):
        print(i)
        if i is 6:
            break # pada saat break maka loop stop bahkan else di lewat (langsung keluar for loop)
    else:
        print("akhir dari loop")

    #continue
    for i in range(1,10):
        print(i)
        if i == 6:
            continue # pada saat continue maka loop di lanjutkan sampai akhir hanya info saja
            print("cek loop")# akan di lewati karna setelah continue akan naik ke for lagi
        
    else:
        print("akhir dari loop")
    print ("ini di luar loop")

    # pass
    for i in range(1,10):
        print(i)
        if i is 6:
            pass # hanya untuk dummy aja pengisi kekosongan
    else:
        print("akhir dari loop")
    print("ini di luar loop")

# WHILE (akan di proses loop jika belum mendapat nilai false)
#break,continue,pass sama seperti di for
    angka = 0
    while angka < 5 :
        print(angka) # akan looping terus / terminate jika true
        angka = angka + 1 # untuk memberi nilai angka sampai menemukan true(stop while)
    print ("ini di luar while")

#fungsi

def tes1():
    print ("ini tes fungsi pertama") # tes fungsi sederhana

def tes2():
    tes1()
    print("ini adalah tes ke2") # fungsi di dalam fungsi(memanggil fungsi 1 di dalam fungsi2)

def harga_buah(kg):         # input argument pada fungsi & return(agar nilai dapat di gunakan kembali)
    harga=15000
    total = kg*harga
    return total            # return bisa list,string atau yg lain mis: return [total,no_id,2345,password]
    print(total)

def mahasiswa(nim,nama_mahasiswa="user",jurusan="it"):# input argumen default & yg kosong harus di taruh di depan
    print ("NIM =",nim)
    print("nama mahasiswa :",nama_mahasiswa )
    print ("JURUSAN :",jurusan)

tes1()
tes2()
harga_buah(3)
mahasiswa(nim="0003",nama_mahasiswa="iwan")


# fungsi dengan lamda

kali = lambda argumen1: print(argumen1) # kali(nama fungsi) agumen1(nama fungsi): print("program yang ingin di jalankan")

kali("tes inputan argumen fungsi dengan lamda")

tambah = lambda x,y: x*y 
print (tambah(3,4))     # lebih simple untuk print dan menjalankan fungsi



# SCOPE GLOBAL DAN LOCAL

nama_barang = "baju"

def ubah_barang(nama_item):
    global nama_barang  # global nama barang akan bisa di ubah di luar fungsi ini
    nama_barang=nama_item
    print("mengubah nama barang menjadi =",nama_item)

ubah_barang("celana")
print("nama barang menjadi",nama_barang)


# iterable list

list1=["jagung","cabai","kol"]
print(list1)
list1.append("kacang") # append untuk menambah angota list di akhirr baris
print(list1)
list1.extend("jahe") # extend menambah anggota list diakhir baris & memisahkan perkarakter
print(list1)
list1.insert(3,"kol") # inseert untuk menambah anggota list di index ke3
print(list1)
hitung_anggota=list1.count("kol") # count menghitung jumlah kol dalam list
print(hitung_anggota) 
list1.remove("kol")      #remove menghapus pada baris yang terdepan
print(list1)
list1.reverse()     #reverse membalik dari urutan 1 ke akhir atau urutan akhir jadi ke1

list2=list1         # variabel baru di taruh di depan,
#list2=list1.copy() # agar list 1 tidak di ubah (akan membuat list baru tanpa mengganggu list utama)
list2.append("bawang") # jika list2 di ubah maka isi dari list1 utama akan keubah juga
print(list2)

# STACKING / TUMPUKAN  (data yang akan di ambil adalah yang paling akhir)

no_antrian=[1,2,3,4,5]
print("no antrian awal",no_antrian)
no_antrian.append(6)
print("no antrian setelah di tambah",6)
print(no_antrian)
no_antrian.pop(3)   # akan di kurangi dari index ke3 yaitu angka 4 (jika di kosongkan akan ambil angka terakhir)
print(no_antrian)

# QEUEU / ANTRIAN (akan mengurangi data yang paling depan)

from collections import deque
from typing import TYPE_CHECKING, Type

no_antrian=deque([1,2,3,4,5,6])
print("no antrian awal",no_antrian)
no_antrian.append(7)
print("no antrian setelah di tambah",7)
print(no_antrian)
data_out=no_antrian.popleft()  # akan di kurangi dari index ke0 yaitu angka 1 (jika di kosongkan akan ambil angka 1)
print("antrian setlah di kurangi =",data_out)
print(no_antrian)

# TUPLE  ()10 x lebih cepat dari list datanya tidak bisa di tambah atau di ubah,berguna untuk type data yang tidak bisa di ubah misal : id,noktp,no card
from typing import Type
import sys
import timeit

contoh_list=[1,2,3,4,5]
print(type(contoh_list)) # melihat jenis type data variable LIST
contoh_tuple=(1,2,3,4,5,6,7,8)
print(type(contoh_tuple)) # melihat jenis type data variable TUPPLE
print(dir(contoh_tuple))  # melihat atribut jenis type data, tupple hanya punya count (memfilter/ meliahat banyak anggota yang sama namanya) & index(posisi dari anggota)
print("besar data list dari =",contoh_list," adalah =",sys.getsizeof(contoh_list))  # melihat besar data pada proses memory
print("besar data tuple dari =",contoh_tuple," adalah =",sys.getsizeof(contoh_tuple)) # melihat besar data pada proses memory tuple lebih ringan
print("kecepatan proses data list =",timeit.timeit(stmt=str(contoh_list),number=1000000)) # cek kecepatan proses data list
print("kecepatan proses data tuple =",timeit.timeit(stmt=str(contoh_list),number=1000000)) # cek kecepatan proses data tuple

#dictionary = {"keys":value,"key": "value"} perbedaan dengan set adalah dictionary berpasangan

member={"ID":1002,
        "Nama" : "Jaguar",
        "Pekerjaan": "Pejabat",
        "Status":"aktif",
        "Area":"Jakarta Barat"}

member1={"ID":1003,
        "Nama" : "Iwan",
        "Pekerjaan": "Teknisi",
        "Status":"non aktif",
        "Area":"Jakarta Timur"}
member_list={1002:member,1003:member1} # membuat variable list

print (member_list[1003]) # akan menampilkan memberlist dengan key:1003

print(member["Pekerjaan"]) #akan mengambil value pekerjaan ("pejabat")
print(member.keys()) # akan menampilkan seluruh keys("Nama","Pekerjaan","Status","Area")
print(member.values()) # akan menampilkan seluruh value("1002","Jaguar","Pejabat","aktif","jakarta Barat")
print(member.items()) # Print seluruh keys : values


# Teknik Looping

nama_buah = ["jeruk",
            "apel",
            "mangga",
            "durian"]
iterasi = 0             # ditambahkan 1 pada saat looping
for i in nama_buah:     # create variable i di dalam komponen nama_buah
    print ("no",iterasi,"nama_buah",i) # menambahkan no_urut pada setiap komponen
    iterasi +=1
   #####cara enumerate###

toko_buah = ["Abadi",
            "jaya makmur",
            "fresh fruit",
            "Induk Buah",
            "Toko sejahtera"]
for aa,bb in enumerate (toko_buah): # membuat penomoran berurut
    print (aa,"=",bb) 

    #######zip#####                         # membuat pasangan berurutan dari 2 VARIABEL,
for toko,buah in zip(toko_buah,nama_buah):  #tapi jumlah item harus sama banyak jika tidak ada pasangannya tidak akan di tampilkan
    print(toko, " menjual = ",buah)

    ## sort type data dictionary
kumpulan_menu={"makanan =":"nasi goreng",
                "minuman =": "jus alpukat",
                "cemilan =":"kerupuk"}

for menu in kumpulan_menu.keys(): # menampilkan keys dari dictionary jika kumpulan_menu.values menampilkan isi
    print (menu)

for menunya,jenis_pesanan in kumpulan_menu.items(): # menampilkan 2 buah isi dictinonary
    print (menunya,jenis_pesanan)


    ## REVERSE urutan terbalik

for z in reversed(range(1,10,1)): # membuat urutan angka dengan range dari 9 ke 1
    print(z)


# MODUL
# buat file bernama data.py di simpan 1 folder dengan tesaje.py
import data
print (data.data_makanan) # memanggil list data

data.tambah_menu_makanan() # memanggil fungsi untuk menambahkan menu

import matematika as math # sample import rename math
math.tambah(2,5)  # memanggil fungsi matematika rename math input iterable

from matematika import kurang, tambah # impor spesifik fungsi yang ada di dalam modul * ambil semua
kurang(6,3)                 #(kemudahan tinggal panggil nama fungsi)








    


    