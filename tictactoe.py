top_row = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
player_one = input("Enter player one's name\n")
player_two = input("Enter player two's name\n")
#
turn = True
moves = 0
win = False

while moves <9:
    if turn == True:
        print(f"{player_one} : Enter a number to select it\n")
        for i in range (len(top_row)):
            for j in range(len(top_row[i])):
                print(top_row[i][j], end=" | ")
            print("\n__  __  __", end="")
            print("\n")
        selection = input()
        for i in range(0,3):
            for position, item in enumerate(top_row[i]):
                if item == selection:
                    top_row[i][position] = "x"

        turn = False
    else:
        print(f"{player_two} : Enter a number to select it\n")
        for i in range(len(top_row)):
            for j in range(len(top_row[i])):
                print(top_row[i][j], end=" | ")
            print("\n__  __  __", end="")
            print("\n")
        selection = input()
        for i in range(0, 3):
            for position, item in enumerate(top_row[i]):
                if item == selection:
                    top_row[i][position] = "o"
        turn = True
    if (top_row[0][0] == top_row[0][1] == top_row[0][2] == "x" or top_row[0][0] == top_row[1][0] == top_row[2][0] == "x"
        or top_row[0][0] == top_row[1][1] == top_row[2][2] == "x" or top_row[0][2] == top_row[1][2] == top_row[2][2] == "x"
        or top_row[1][0] == top_row[1][1] == top_row[1][2] == "x" or top_row[2][0] == top_row[2][1] == top_row[2][2] == "x"
        or top_row[0][1] == top_row[1][1] == top_row[2][1] == "x" or top_row[0][2] == top_row[1][1] == top_row[2][0] == "x"):
        print(f"{player_one} wins\n")
        win = True
        break
    elif (top_row[0][0] == top_row[0][1] == top_row[0][2] == "o" or top_row[0][0] == top_row[1][0] == top_row[2][0] == "o"
        or top_row[0][0] == top_row[1][1] == top_row[2][2] == "o" or top_row[0][2] == top_row[1][2] == top_row[2][2] == "o"
        or top_row[1][0] == top_row[1][1] == top_row[1][2] == "o" or top_row[2][0] == top_row[2][1] == top_row[2][2] == "o"
        or top_row[0][1] == top_row[1][1] == top_row[2][1] == "o" or top_row[0][2] == top_row[1][1] == top_row[2][0] == "o"):
        print(f"{player_two} wins\n")
        win = True
        break
    else:
        moves += 1
for i in range(len(top_row)):
    for j in range(len(top_row[i])):
        print(top_row[i][j], end=" | ")
    print("\n__  __  __", end="")
    print("\n")
if win == False:
    print("Draw")
if (top_row[0][0], top_row[0][1], top_row[0][2] == "x" or top_row[0][0], top_row[1][0], top_row[2][0] == "x"
        or top_row[0][0], top_row[1][1], top_row[2][2] == "x" or top_row[0][2], top_row[1][2], top_row[2][2] == "x"
        or top_row[1][0], top_row[1][1], top_row[1][2] == "x"or top_row[2][0], top_row[2][1], top_row[2][2] == "x"
        or top_row[0][1], top_row[1][1], top_row[2][1] == "x" or top_row[0][2], top_row[1][1], top_row[2][0] == "x"):
    print("")