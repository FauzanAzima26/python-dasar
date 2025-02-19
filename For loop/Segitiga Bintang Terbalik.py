input = int(input("Masukkan angka: "))
for i in range(input):
    for j in range(input-i):
        print("*", end=" ")
    print()