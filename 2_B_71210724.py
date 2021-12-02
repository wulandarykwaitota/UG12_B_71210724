dict = {}

while True:
    name = input("Masukkan nama : ")

    if name == 'stop' or name == 'STOP':
        break

    else:
        chair_number = input(f"Masukkan nomor kursi {name} : ")

        if dict:
            for item in list(dict.keys()):
                if chair_number == item:
                    print("Mohon maaf kursi tersebut telah terisi")
                else:
                    dict[chair_number] = name
        else:
            dict[chair_number] = name

print("List kursi yang telah terisi: ")

for key, value in dict.items():
    print(f"Kursi nomor {key} telah diisi oleh {value}")
