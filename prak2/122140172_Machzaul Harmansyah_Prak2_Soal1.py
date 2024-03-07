class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    # Setter dan Getter untuk nama
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, new_nama):
        self.__nama = new_nama

    # Setter dan Getter untuk nim
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, new_nim):
        self.__nim = new_nim

    # Method 1: Menghitung IPK
    def hitung_ipk(self, nilai_sks, sks_tempuh):
        if sks_tempuh == 0:
            return 0
        return round(nilai_sks / sks_tempuh, 2)

    # Method 2: Mengecek Status Aktif
    def cek_status_aktif(self, semester_sekarang):
        if semester_sekarang <= self.angkatan + 4:
            return "Aktif"
        return "Tidak Aktif"

    # Method 3: Menampilkan Informasi Lengkap
    def info_lengkap(self):
        return f"""
        NIM: {self.nim}
        Nama: {self.nama}
        Angkatan: {self.angkatan}
        Status Mahasiswa: {'Aktif' if self.isMahasiswa else 'Tidak Aktif'}
        """


# Inisiasi object pertama
mahasiswa1 = Mahasiswa("123456789", "Budi", 2020)

mahasiswa2 = Mahasiswa("987654321", "Ani", 2021)

# Menampilkan informasi lengkap object pertama
print(mahasiswa1.info_lengkap())

# Mengubah nama object pertama
mahasiswa1.nama = "Cici"

# Menghitung IPK object pertama
ipk_mahasiswa1 = mahasiswa1.hitung_ipk(3.8, 20)

# Mengecek status aktif object kedua
status_mahasiswa2 = mahasiswa2.cek_status_aktif(6)

# Menampilkan informasi IPK dan status aktif
print(f"IPK {mahasiswa1.nama}: {ipk_mahasiswa1}")
print(f"{mahasiswa2.nama} - Semester {mahasiswa2.angkatan + 6}: {status_mahasiswa2}")
