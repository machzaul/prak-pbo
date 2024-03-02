jarijari = float(input("jari-jari : "))
luas = 0
keliling = 0
if jarijari <= 0:
    print("jari-jari lingkaran tidak boleh negative")
else:
    luas = 3.14 * jarijari * jarijari
    keliling = 2 * 3.14 * jarijari
    print("luas :", luas)
    print("keliling :", keliling)