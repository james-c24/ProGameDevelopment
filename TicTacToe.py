c1,c2,c3,c4,c5,c6,c7,c8,c9 = 1,2,3,4,5,6,7,8,9
grid = [[c1,c2,c3],[c4,c5,c6],[c7,c8,c9]]
game_over = False
winner = ""
turns = 0

print("Player X will go first, followed by Player O. Write moves by first writing the row number, then column number to form a two-digit number.")

def check_winner():
    global turns
    if c1 == c2 == c3:
        winner = c1
        game_over = True
    elif c4 == c5 == c6:
        winner = c4
        game_over = True
    elif c7 == c8 == c9:
        winner = c7
        game_over = True
    elif c1 == c4 == c7:
        winner = c1
        game_over = True
    elif c2 == c5 == c8:
        winner = c2
        game_over = True
    elif c3 == c5 == c9:
        winner = c3
        game_over = True
    elif c1 == c5 == c9:
        winner = c1
        game_over = True
    elif c3 == c5 == c7:
        winner = c3
        game_over = True
    else:
        turns += 1

while game_over == False or turns > 9:
    x_turn = input("Player X, make your move: ")
    row = int(x_turn[0]) - 1
    column = int(x_turn[1]) - 1
    grid[row][column] = "X"
    check_winner()

    o_turn = input("Player O, make your move: ")
    row = int(o_turn[0]) - 1
    column = int(o_turn[1]) - 1
    grid[row][column] = "O"
    check_winner()

if game_over == True:
    print("{} is the winner!".format(winner))
else:
    print("The game ends in a draw.")
