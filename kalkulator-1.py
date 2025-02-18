print("pilih salah satu jenis operasi berikut:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = int(input("Masukkan pilihan operasi (1/2/3/4): "))

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))

if pilihan == 1:
    hasil = angka_1 + angka_2
    print("Hasil penjumlahan:", hasil)
elif pilihan == 2:
    hasil = angka_1 - angka_2
    print("Hasil pengurangan:", hasil)
elif pilihan == 3:
    hasil = angka_1 * angka_2
    print("Hasil perkalian:", hasil)
elif pilihan == 4:
    if angka_2 == 0:
        print("Pembagian oleh nol tidak dapat dilakukan.")
    else:
        hasil = angka_1 / angka_2
        print("Hasil pembagian:", hasil)
else:
    print("Pilihan tidak valid.")



