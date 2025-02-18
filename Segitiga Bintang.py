input = int(input("Masukkan angka: "))
for i in range(input):
    for j in range(i+1):
        print("*", end=" ")
    print()