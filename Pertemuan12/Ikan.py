from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, jenis_kulit):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.jenis_kulit = jenis_kulit
           
    def cetak_Ikan(self):
        super().cetak()
        print("Corak \t\t\t:", self.corak,
               "\nJenis_kulit \t\t:", self.jenis_kulit)
print("\n ======= Jenis Ikan =======")  
print("\n === Objek 1 ===")              
koi = Ikan("Koi", "Cacing", "Perairan Tawar", "Bertelur", "Hitam merah dan putih", "Bersisik")
koi.cetak_Ikan()
print("\n === Objek 2 ===")
nemo = Ikan("Nemo", "Planton dan Alga", "Laut", "Bertelur", "Jingga dan Hitam", "Bersisik")
nemo.cetak_Ikan()