class Hewan :
    def __init__(self,nama,jenis):
        self.nama = nama
        self.jenis = jenis
    
    def bersuara(self):
        pass
    
    def makan(self):
        pass
    
    def minum(self):
        pass

class Kucing(Hewan):
    def __init__(self,nama,jenis):
        super(Kucing,self).__init__(nama,jenis)

    def bersuara(self):
        print("kucing "+self.nama+" bersuara meong!")
    
    def makan(self):
        print("kucing "+self.nama+" sedang makan tulang")
    
    def minum(self):
        print("kucing "+self.nama+" sedang minum air")

class Anjing(Hewan):
    def __init__(self,nama,jenis):
        super(Anjing,self).__init__(nama,jenis)

    def bersuara(self):
        print("Anjing "+self.nama+" bersuara Guk guk!")

    def makan(self):
        print ("anjing "+self.nama+" sedang makan tulang")
    
    def minum(self):
        print ("anjing "+self.nama+" sedang minum air")

hewan1 = Kucing("Kiki","betina")
hewan2 = Anjing("ichi","jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()
hewan2.bersuara()
hewan2.makan()
