from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun
           
    def cetak_Ular(self):
        super().cetak()
        print("Corak \t\t\t:", self.corak,
               "\nRacun \t\t\t:", self.racun)
print("\n ======= Jenis Ular =======")  
print("\n === Objek 1 ===")              
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik", "Tidak Berbisa")
anaconda.cetak_Ular()
print("\n === Objek 2 ===")
kobra = Ular("King Kobra", "Tikus dan ular lainnya", "Hutan", "Bertelur", "Lingkaran pada leher dan matanya", "Berbisa")
kobra.cetak_Ular()