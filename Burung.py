from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna
        
    def cetak_Burung(self):
        super().cetak()
        print("jenis \t\t\t:", self.jenis,
               "\nWarna \t\t\t:", self.warna)
print("\n ======= Jenis Burung =======")  
print("\n === Objek 1 ===")        
hantu = Burung("Hantu", "Daging hewan kecil", "pohon", "Bertelur", "Karnivora", "Putih")
hantu.cetak_Burung()  
print("\n === Objek 2 ===")
cendrawasih = Burung("Cendrawasih", "Serangga", "Hutan berdataran rendah", "Bertelur", "Omnivora", "Kuning"
                     "\n\t\t\t: Hijau" 
                     "\n\t\t\t: Cokelat" 
                     "\n\t\t\t: Kuning dan Putih")
cendrawasih.cetak_Burung()