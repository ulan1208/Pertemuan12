from Animal import *

class Harimau(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.jenis = jenis
           
    def cetak_Harimau(self):
        super().cetak()
        print("Corak \t\t\t:", self.corak,
               "\nJenis \t\t\t:", self.jenis)
print("\n ======= Jenis Harimau =======")  
print("\n === Objek 1 ===")              
harimau = Harimau("Harimau Putih", "Daging", "Hutan", "Melahirkan", "Hitam dan putih", "Benggala")
harimau.cetak_Harimau()
print("\n === Objek 2 ===")
harimau = Harimau("Harimau Biasa", "Daging", "Hutan", "Melahirkan", "Oranye Putih dan Hitam", "Siberia")
harimau.cetak_Harimau()