#Developed by Jordan A Kellogg with Pxl Perfect Digital Solutions.


#define board space and example board spaces for user reference
boards = ["   ", "|", "   ", "|", "   ", "\n-----------\n", "   ", "|", "   ", "|", "   ", "\n-----------\n", "   ", "|", "   ", "|", "   "]
boardsEx = [" 0 ", "|", " 2 ", "|", " 4 \n", "-----------\n", " 6 ", "|", " 8 ", "|", " 10 \n", "-----------\n", " 12", "| ", "14", "| ", "16\n"]
players = ("X", "O") 


#function that takes in a user choice on the board, checks if number is eligible, and returns user number, 
def playerChoice():
    isValid = False
    eligibleSpace = [0, 2, 4, 6, 8, 10, 12, 14, 16]
    success = False
    while success != True:
        #ensure user inputs valid int and loop until conidtion is met
        try:
            userSpace = int(input("Please choose an available space: "))
            while isValid != True:
                if userSpace not in eligibleSpace:
                    print("Invalid. Please an available space from numbers ranging 0, 2, 4, 6, 8, 10, 12, 14, 16")
                    userSpace = int(input("Please choose an available space: "))
                    continue
                else:
                    return userSpace
        except ValueError:
            print("Please enter a valid number ranging from 0, 2, 4, 6, 8, 10, 12, 14, and 16")
            continue 
#function that checks if all spaces have been filled and returns True or False
def isBoardFull(board):
    if "   " not in board:
        return True
    else:
        return False

#Function that runs thru if/else tree to determine if X's or O's have valid win and returns True
def isThereAWinner(board):
    if board[0] == " X " and board[2] == " X " and board[4] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[0] == " X " and board[8] == " X " and board[16] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[0] == " X " and board[6] == " X " and board[12] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[2] == " X " and board[8] == " X " and board[14] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[4] == " X " and board[10] == " X " and board[16] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[4] == " X " and board[8] == " X " and board[12] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[6] == " X " and board[8] == " X " and board[10] == " X ":
        print("\n We have a winner! X's win!")
        return True
    elif board[12] == " X " and board[14] == " X " and board[16] == " X ":
        print("\n We have a winner! X's win!")
        return True
    if board[0] == " O " and board[2] == " O " and board[4] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[0] == " O " and board[8] == " O " and board[16] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[0] == " O " and board[6] == " O " and board[12] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[2] == " O " and board[8] == " O " and board[14] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[4] == " O " and board[10] == " O " and board[16] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[4] == " O " and board[8] == " O " and board[12] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[6] == " O " and board[8] == " O " and board[10] == " O ":
        print("\n We have a winner! O's win!")
        return True
    elif board[12] == " O " and board[14] == " O " and board[16] == " O ":
        print("\n We have a winner! O's win!")
        return True
    else:
        return False 
#function that checks if the selected space is available, 
def isSpaceAvailable(space, playerMarker):
    if boards[space] == " X " or boards[space] == " O ":
        print("Sorry that space is not avaible, choose again\n")
        return False
    elif boards[space] == "   ":
        boards[space] = " {} ".format(playerMarker)
        return True
    
#function that determines which player goes, and uses isSpaceAvailable in while loop to ensure open space choosen
def playerSpot(whichPlayer):
    isOpen = False
    while isOpen != True:
        if isSpaceAvailable(playerChoice(), whichPlayer) == True:
            isOpen = True
       
        else:
            continue
#simple function to print the board
def printBoard(board):
    print("".join(board))

#main game function
def currentGame():
    gameOn = False
    #run through game until a winner is determined or board is full
    while gameOn != True:
        print("X's turn")
        #Player X selects space and has selection printed on board
        playerSpot(players[0])
        printBoard(boards)
        
        if isBoardFull(boards) == True:
            print("\nThe Board is full, game over")
            break
        if isThereAWinner(boards) == True:
            break
        print("O's turn")
        #Player O selects space and has selection printed on board
        playerSpot(players[1])
        printBoard(boards)
        if isBoardFull(boards) == True:
            print("\nThe Board is full, game over")
            break
        if isThereAWinner(boards) == True:
            break
        else:
            continue
#funtion to determine if players would like to go again    
def goAgain():
    isValid = False
    success = False
    while success != True:
        try:
            decision = input("\nGame over! Would you like to play again? (Type Y or N): ")
            while isValid != True:
                if decision.upper() == "N":
                    return False
                elif decision.upper() == "Y":
                    return True
                else:
                    print("Invalid, please type 'Y' for yes, or 'N' for no.")
        except ValueError:
            print("Invalid. Please type 'Y' for yes, or 'N' for no.")

    
print("\n")
print("\n")
print("".join(boardsEx))
print("\nHere are the example space choices\n")


#set variable to verify if game is still running
going = True
while going != False:
    currentGame()
    if goAgain() == True:
        #reset board for new game
        boards = ["   ", "|", "   ", "|", "   ", "\n-----------\n", "   ", "|", "   ", "|", "   ", "\n-----------\n", "   ", "|", "   ", "|", "   "]
        continue
    else:
        print("The game has ended")
        break
        



        
