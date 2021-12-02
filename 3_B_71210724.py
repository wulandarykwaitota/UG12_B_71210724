rows = input("Input : ")
columns = 2 * len(rows) - 2
text = ''

print("Output :")

for index_row in range(0, len(rows) - 1):

    for index_column in range(0, columns):
        print(' ', end='')

    columns -= 2

    for index_column in range(0, index_row + 1):
        print(f'{rows[index_column]} ', end='')

    print('')

columns = -1

for index_row in range(len(rows) - 1, -1, -1):
    for index_column in range(columns, -1, -1):
        print(' ', end='')

    columns += 2

    for index_column in range(0, index_row + 1):
        print(f'{rows[index_column]} ', end='')

    print('')
