# nama : machzaul harmansyah
# nim  : 122140172
# kelas: RB

import pygame
import sys

# Pewarisan
class TicTacToe:
    def __init__(self):
        self.papan = [[' ' for _ in range(3)] for _ in range(3)]
        self.pemain_sekarang = 'X'

    # Enkapsulasi
    def gambar_papan(self, layar):
        layar.fill((255, 255, 255))
        for i in range(1, 3):
            pygame.draw.line(layar, (0, 0, 0), (0, i * 200), (600, i * 200), 2)
            pygame.draw.line(layar, (0, 0, 0), (i * 200, 0), (i * 200, 600), 2)

        for baris in range(3):
            for kolom in range(3):
                if self.papan[baris][kolom] == 'X':
                    pygame.draw.line(layar, (0, 0, 255), (kolom * 200 + 50, baris * 200 + 50),
                                     (kolom * 200 + 150, baris * 200 + 150), 5)
                    pygame.draw.line(layar, (0, 0, 255), (kolom * 200 + 50, baris * 200 + 150),
                                     (kolom * 200 + 150, baris * 200 + 50), 5)
                elif self.papan[baris][kolom] == 'O':
                    pygame.draw.circle(layar, (255, 0, 0), (kolom * 200 + 100, baris * 200 + 100), 70, 5)

    def gerak(self, baris, kolom):
        if self.papan[baris][kolom] == ' ':
            self.papan[baris][kolom] = self.pemain_sekarang
            self.pemain_sekarang = 'O' if self.pemain_sekarang == 'X' else 'X'

    def periksa_pemenang(self):
        # Periksa baris dan kolom
        for i in range(3):
            if self.papan[i][0] == self.papan[i][1] == self.papan[i][2] != ' ':
                return self.papan[i][0]
            if self.papan[0][i] == self.papan[1][i] == self.papan[2][i] != ' ':
                return self.papan[0][i]
        
        # Periksa diagonal
        if self.papan[0][0] == self.papan[1][1] == self.papan[2][2] != ' ':
            return self.papan[0][0]
        if self.papan[0][2] == self.papan[1][1] == self.papan[2][0] != ' ':
            return self.papan[0][2]

        # Periksa seri
        if all(self.papan[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'seri'

        return None


# Polimorfisme
class Permainan(TicTacToe):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.layar = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Tic Tac Toe')

    def jalankan(self):
        berjalan = True
        while berjalan:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    berjalan = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    baris, kolom = y // 200, x // 200
                    self.gerak(baris, kolom)

            self.gambar_papan(self.layar)
            pygame.display.flip()

            pemenang = self.periksa_pemenang()
            if pemenang:
                pygame.time.delay(1000)
                if pemenang == 'seri':
                    print("Seri!")
                else:
                    print(f"{pemenang} menang!")
                berjalan = False

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    permainan = Permainan()
    permainan.jalankan()
