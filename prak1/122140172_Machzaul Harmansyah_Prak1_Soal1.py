batas_bawah = int(input("batas bawah : "))
batas_atas = int(input("batas atas : "))
hasil = 0
if batas_atas <= 0 or batas_bawah <= 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah nol")
else:
    for i in range(batas_bawah,batas_atas):
        if i % 2 != 0:
            print(i)
            hasil += i

    print("Total : ",hasil)