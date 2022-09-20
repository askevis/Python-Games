row1 = [0, 0, 0]
row2 = [0, 0, 0]
row3 = [0, 0, 0]
triliza = [row1, row2, row3]

def chooseRow():
    choiceRow = 6
    while (choiceRow < 1 or choiceRow > 3):
     print("Player", player , end = '')
     choiceRow = int(input(" please enter number of row : "))
     if (choiceRow < 1 or choiceRow > 3) :
        print("Please insert a number from 1 to 3")
     if choiceRow == 1:
         row = row1
     elif choiceRow == 2:
         row = row2
     else:
         row = row3
     if row[0]!=0 and row[1]!=0 and row[2]!=0:
         print("Please choose another row , this row is full")
         choiceRow = 4
    return choiceRow

def chooseCol(row):
    choiceCol = 6
    while (choiceCol < 1 or choiceCol > 3):
        print("Player", player, end='')
        choiceCol = int(input(" please enter number of column : "))
        if (choiceCol < 1 or choiceCol > 3):
            print("Please insert a number from 1 to 3")
        if row == 1:
            row = row1
        elif row == 2:
            row = row2
        else:
            row = row3
        if row[choiceCol-1]!=0:                 #elegxos gia valid 8esh
         print("Please select a valid position")
         choiceCol = 4
    return choiceCol

def replace(row , col , player):
    if row == 1:
        row1[col - 1] = player
    elif row == 2:
        row2[col-1] = player
    else:
        row3[col-1] = player

def checkwin(row1 , row2 , row3 ):
    win = False
    if (row1[0] != 0 and row1[0]==row1[1] and row1[1]==row1[2]) :
        win = True
    if (row2[0] != 0 and row2[0] == row2[1] and row2[1] == row2[2]):
        win = True
    if (row3[0] != 0 and row3[0] == row3[1] and row3[1] == row3[2]):
        win = True
    if (row1[0] != 0 and row1[0] == row2[0] and row2[0] == row3[0]):
        win = True
    if (row1[1] != 0 and row1[1] == row2[1] and row2[1] == row3[1]):
        win = True
    if (row1[2] != 0 and row1[2] == row2[2] and row2[2] == row3[2]):
        win = True
    if (row1[0] != 0 and row1[0] == row2[1] and row2[1] == row3[2]):
        win = True
    if (row1[2] != 0 and row1[2] == row2[1] and row2[1] == row3[0]):
        win = True
    if win == True:
        print("Congratulations player " , player ," you win!" )
        return True
    else:
        return False

def checkdraw(end,row1,row2,row3):
    if (row1[0] != 0 and row1[1] != 0 and row1[2] != 0) and (row2[0] != 0 and row2[1] != 0 and row2[2] != 0) and (row3[0] != 0 and row3[1] != 0 and row3[2] != 0) and end==False:
        print("It's a draw! ")
        return True
    else:
        return False

def replay():
    valid = True
    while valid == True:
     repl = input("Would you like to play again? ")
     if repl == "Y" or repl == "y":
        return True
     elif repl == "N" or repl == "n":
        return False
     else:
         print("Please enter Y/y for Yes or N/n for No")

gameon = True
while (gameon==True):
 player = int(input("Please select if player 1 or 2 goes 1st : "))
 if player != 1 and player !=2:
     print("Invalid player!")
     continue
 print("\n", triliza[0], "\n", triliza[1], "\n", triliza[2])
 gameend = False
 draw = False
 while gameend == False and draw == False:
     a = chooseRow()
     b = chooseCol(a)
     replace(a,b,player)
     print("\n", triliza[0], "\n", triliza[1], "\n", triliza[2])
     gameend = checkwin(row1,row2,row3)
     draw = checkdraw(gameend,row1,row2,row3)
     if player == 1:
         player = 2
     elif player == 2:
         player = 1
 gameon = replay()
 if gameon == True:
     row1 = [0, 0, 0]
     row2 = [0, 0, 0]
     row3 = [0, 0, 0]
     triliza = [row1, row2, row3]
print("Thank you for playing! ")





