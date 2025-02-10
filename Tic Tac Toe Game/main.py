from tabulate import tabulate
import random, string
import time

print("""Table format:
   1 2 3
A
B
C
Input format: A1, A2...""")
print("\n\n")
letter_to_number = {'A': 0, 'B': 1, 'C': 2}
count = 0
table = [[' ' for _ in range(3)] for __ in range(3)]

def restart():
    print("Incorrect choice!")
    time.sleep(1)
    print('\n' * 100)

def get_coord(choice):
    if len(choice) != 2:
        restart()
    else:
        coord = list(choice)
        if coord[0] not in letter_to_number:
            restart()
        elif int(coord[1]) - 1 not in range(0, 3):
            restart()
        else:
            coord[0] = letter_to_number[coord[0]]
            coord[1] = int(coord[1]) - 1
            if table[coord[0]][coord[1]] != ' ':
                restart()
            else:
                return coord

def check_game():
    for row in table:
        if len(set(row)) == 1 and row[0] != ' ':
            print(f"{row[0]} won!")
            return True
    for ind in range(len(table[0])):
        column = [row[ind] for row in table]
        if len(set(column)) == 1 and column[0] != ' ':
            print(f"{column[0]} won!")
            return True
    diagonal1 = []
    for ind in range(len(table[0])):
        diagonal1.append(table[ind][ind])
    if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
        print(f"{diagonal1[0]} won!")
        return True
    diagonal2 = []
    diagonal_count = 0
    for ind in range(len(table[0])-1, -1, -1):
        diagonal2.append(table[diagonal_count][ind])
        diagonal_count += 1
    if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
        print(f"{diagonal2[0]} won!")
        return True

    draw = False
    for row in table:
        if ' ' not in row:
            draw = True
        else:
            draw = False
            break
    if draw:
        print("This is a draw!")
        return True
    return False

while True:
    print(tabulate(table, tablefmt='grid'))
    if check_game():
        break
    if count % 2 == 0:
        pick = input("X's turn! Choice > ").upper()
        cell = get_coord(pick)
        if cell is None:
            continue
        table[cell[0]][cell[1]] = 'X'
    else:
        pick = input("Y's turn! Choice > ").upper()
        cell = get_coord(pick)
        if cell is None:
            continue
        table[cell[0]][cell[1]] = 'Y'
    count += 1
    print("\n"*100)