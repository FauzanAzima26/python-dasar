tinggi = int(input("Masukkan tinggi persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

for i in range(tinggi):
    for j in range(lebar):
        print("*", end=" ")
    print()