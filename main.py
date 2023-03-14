import random
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def clearBoard(board):
    for pos in range(9):
        board[pos] = ' '

def InsertBoard(sign, position):
    board[position] = sign


def IsEmpty(position):
    return board[position] == ' '

def printBoard(board):
    print(f""" 
     {board[0]} | {board[1]} | {board[2]}
    -----------     
     {board[3]} | {board[4]} | {board[5]} 
    -----------  
     {board[6]} | {board[7]} | {board[8]} 
    """)


def spaceIsFree(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def isWinner(board,sign):
    if ((board[0] == sign and board[1] == sign and board[2] == sign) or
            (board[3] == sign and board[4] == sign and board[5] == sign) or
            (board[6] == sign and board[7] == sign and board[8] == sign) or
            (board[0] == sign and board[3] == sign and board[6] == sign) or
            (board[1] == sign and board[4] == sign and board[7] == sign) or
            (board[2] == sign and board[5] == sign and board[8] == sign) or
            (board[0] == sign and board[4] == sign and board[8] == sign) or
            (board[2] == sign and board[4] == sign and board[6] == sign) ):
        return True
    else:
        return False


def player1Move():
    q = True
    while q:
        move = int(input("Select a position (1-9):")) - 1
        if 0 <= move <= 8:
            if spaceIsFree(board,move):
                q = False
                InsertBoard('X', position=move)
            else:
                print("This position is not empty!")
        else:
            print("Please type a number within in range!")

def player2Move():
    q = True
    while q:
        move = int(input("Select a position (1-9):")) - 1
        if 0 <= move <= 8:
            if spaceIsFree(board, move):
                q = False
                InsertBoard('O', position=move)
            else:
                print("This position is not empty!")
        else:
            print("Please type a number within in range!")


def aiMove():
    EmptyPlaces = []

    for num in range(9):
        if board[num] == ' ':
            EmptyPlaces.append(num)

    for let in ['O', 'X']:
        for i in EmptyPlaces:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    if not playerFirst:
        corners = []
        for i in EmptyPlaces:
            if i in [0, 2, 6, 8]:
                corners.append(i)
        if len(corners) > 0:
            move = random.choice(corners)
            return move

    if playerFirst == True and board[4] == ' ':
        if 4 in EmptyPlaces:
            move = 4
            return move

    # select corner if corners is empty
    corners = []
    for i in EmptyPlaces:
        if i in [0, 2, 6, 8]:
            corners.append(i)

    # select center if center is empty
    if 4 in EmptyPlaces:
        move = 4
        return move

    if len(corners) > 0:
        move = random.choice(corners)
        return move


    # select edge if edges is empty

    edges = []
    for i in EmptyPlaces:
        if i in [1, 3, 5, 7]:
            edges.append(i)

    if len(edges) > 0:
        move = random.choice(edges)
        return move



def isBoardFull(board):
    for n in board:
        if n == ' ':
            return False
    return True

def isBoardEmpty(board):
    x=0
    for n in board:
        if n == ' ':
            x=x+1
    if x == 9:
        return True
    else:
        return False


print("Welcome to TicTacTeo game.")

run = True
while run:
    gamemode = input("Player vs Player(a)\nPlayer vs Computer(b)").lower()
    if gamemode == 'a':
        turn = random.randint(0, 1)

        while not isBoardFull(board):
            if turn % 2 == 0:  # player1
                if not isWinner(board, 'O'):
                    print("\nPlayer1 move.")
                    player1Move()
                    printBoard(board)
                else:
                    print("\nPlayer2 win.")
                    break

            if turn % 2 == 1:  # player2
                if not isWinner(board, 'X'):
                    print("\nPlayer2 move.")
                    player2Move()
                    printBoard(board)
                else:
                    print("\nPlayer1 win.")
                    break
            turn = turn + 1
            if isBoardFull(board):
                print("\nGame is a tie.")
        clearBoard(board)

    elif gamemode == 'b':
        turn = random.randint(0, 1)
        if turn % 2 == 0:
            playerFirst = True
        else:
            playerFirst = False

        while not isBoardFull(board):
            if turn % 2 == 0:  # player
                if not isWinner(board, 'O'):
                    player1Move()
                    printBoard(board)
                else:
                    print("Computer win.")
                    break

            if turn % 2 == 1:
                if not isWinner(board, 'X'):  # ai
                    move = aiMove()
                    if isBoardFull(board):
                        print("Game is a tie. No more empty space.")
                    else:
                        InsertBoard('O', move)
                        printBoard(board)
                else:
                    print("You win")
                    break
            turn = turn + 1
            if isBoardFull(board):
                print("Game is a tie.")
        clearBoard(board)

    else:
        print("Invalid option.")
