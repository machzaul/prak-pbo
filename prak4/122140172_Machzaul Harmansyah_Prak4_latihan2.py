class bentuk :
    def __init__(self):
        pass
    def hitungLuas(self):
        pass


class Persegi(bentuk) :
    def __init__(self, sisi):
        self.sisi = sisi
    def hitungLuas(self):
        return self.sisi * self.sisi

class Lingkaran(bentuk) :
    def __init__(self, sisi):
        self.sisi = sisi
    def hitungLuas(self):
        return self.sisi * self.sisi * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def hitungLuas(self):
    luas()

persegi = Persegi(5)

lingkaran = Lingkaran(3)

print(f"luas persegi :{persegi.hitungLuas()}")
print(f"luas lingkaran :{lingkaran.hitungLuas()}")