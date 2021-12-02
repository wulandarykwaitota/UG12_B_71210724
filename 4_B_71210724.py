rows = int(input('Input : '))
columns = 2 * rows - 2

print('Output :')

for index_row in range(0, rows):
    for index_column in range(0, columns):
        print(' ', end='')

    columns -= 2

    for index_column in range(0, index_row + 1):
        if index_column == (index_column - 1) or index_row == (rows + 1) or index_column == index_row:
            print('* ', end='')
        elif index_column == (index_column - 1) or index_row == (rows - 1):
            print('* ', end='')
        elif index_column == 0:
            print('* ', end='')
        else:
            print(' ', end=' ')

    print('')
