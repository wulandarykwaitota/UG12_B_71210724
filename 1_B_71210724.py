bilangan = int(input("Masukkan banyak bilangan : "))
total = 0
daftar_bilangan = []

print('Total =', end= ' ')

for index in range(1, bilangan+1):

    if index == bilangan:
        if index % 7 == 0:
            print(f'{index % 7}')
        else:
            print(f'{bilangan}')
    elif index % 7 == 0:
        print(f'{index % 7} +', end=' ')
    elif (index + 1) % 3 == 0:
        print(f'{index} -', end=' ')
    else:
        print(f'{index} +', end=' ')

    if index % 7 == 0:
        total = total + 0
    elif index % 3 == 0:
        total = total + (index * -1)
    else:
        total = total + index

print(f'Hasil perhitungan diatas ialah {total}')
