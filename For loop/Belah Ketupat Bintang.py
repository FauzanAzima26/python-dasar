input = int(input("Masukkan angka: "))

for i in range(input):
    for j in range(input-i):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print()
for i in range(1, input):
    for j in range(i+1):
        print(" ", end="")
    for k in range(input-i):
        print("* ", end="")
    print()