import time
class Siswa:
    def __init__(self, nama, nis):
        """
        Constructor untuk kelas Siswa.

        Args:
            nama (str): Nama siswa.
            nis (str): Nomor Induk Siswa.
        """
        self.nama = nama
        self.nis = nis
        print(f"Siswa baru {self.nama} ({self.nis}) telah dibuat!")

    def __del__(self):
        """
        Destructor untuk kelas Siswa.
        """
        print(f"Siswa {self.nama} ({self.nis}) telah dihapus!")

    # Decorator untuk menghitung waktu eksekusi
    def waktu_eksekusi(func):
        def wrapper(self, *args, **kwargs):
            """
            Decorator untuk menghitung waktu eksekusi method.

            Args:
                self: Instance dari kelas Siswa.
                *args: Argumen yang dilewatkan ke method.
                **kwargs: Keyword arguments yang dilewatkan ke method.

            Returns:
                Hasil dari method yang dibungkus.
            """
            start_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            print(f"Waktu eksekusi {func.__name__}: {end_time - start_time} detik")
            return result
        return wrapper

    # Method untuk belajar
    @waktu_eksekusi
    def belajar(self, materi):
        """
        Method untuk belajar suatu materi.

        Args:
            materi (str): Materi yang dipelajari.
        """
        print(f"Siswa {self.nama} sedang belajar {materi}")

    # Method untuk mengikuti ujian
    @waktu_eksekusi
    def ujian(self, mata_pelajaran):
        """
        Method untuk mengikuti ujian suatu mata pelajaran.

        Args:
            mata_pelajaran (str): Mata pelajaran yang diujikan.
        """
        print(f"Siswa {self.nama} sedang mengikuti ujian {mata_pelajaran}")


# Inisiasi object
siswa1 = Siswa("Budi", "123456789")
siswa2 = Siswa("Ani", "987654321")

# Memanggil method belajar dan ujian
siswa1.belajar("Matematika")
siswa2.ujian("Bahasa Indonesia")

# Hapus object
del siswa1
del siswa2
