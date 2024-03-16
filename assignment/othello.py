# Georgios Giatsos, A.M. 3202

import random
import sys
def create_board(board):
    H = '  ---------------------------------'
    V = '  |   |   |   |   |   |   |   |   |'
    print('    1   2   3   4   5   6   7   8')
    print(H)
    for y in range(8):
        print(V)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(V)
        print(H)
 
def reset_board(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
            board[3][3] = '1'
            board[3][4] = '2'
            board[4][3] = '2'
            board[4][4] = '1'
 
def print_board():
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board
 

def reverse_count(board, box, firstx, firsty):
    if board[firstx][firsty] != ' ' or not correct_move(firstx, firsty):
        return False
    board[firstx][firsty] = box
    if box == '1':
        diffbox = '2'
    else:
        diffbox = '1'
 
    boxesToChange = []
    for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = firstx, firsty
        x += xdir
        y += ydir 
        if correct_move(x, y) and board[x][y] == diffbox:
            x += xdir
            y += ydir
            if not correct_move(x, y):
                continue
            while board[x][y] == diffbox:
                x += xdir
                y += ydir
                if not correct_move(x, y):
                    break
            if not correct_move(x, y):
                continue
            if board[x][y] == box:
                while True:
                    x -= xdir
                    y -= ydir
                    if x == firstx and y == firsty:
                        break
                    boxesToChange.append([x, y])
    board[firstx][firsty] = ' ' 
    if len(boxesToChange) == 0:
        return False
    return boxesToChange
 
 
def correct_move(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <=7



def add_checker(board, box, firstx, firsty):
    boxesToChange = reverse_count(board, box, firstx, firsty)
    if boxesToChange == False:
        return False
    board[firstx][firsty] = box
    for x, y in boxesToChange:
        board[x][y] = box
    return True


def compute_counts(board):
    copyboard = print_board()
    for x in range(8):
        for y in range(8):
            copyboard[x][y] = board[x][y]
    return copyboard



def human_play(board, playerbox):
     DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
     while True:
         print('Enter your move, or type exit to end the game.')
         move = input().lower()
         if move == 'exit':
             return 'exit'
         if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
             x = int(move[0]) - 1
             y = int(move[1]) - 1
             if reverse_count(board, playerbox, x, y) == False:
                 continue
             else:
                 break
         else:
             print('This is not a valid move. Type a x number (1-8) and then a y number (1-8).')
             print('For example, the combination 18 is the bottom left box in the corner.')
     return [x, y]



def human_play1(board, player1box):
     DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
     while True:
         print('Enter your move, or type exit to end the game.')
         move = input().lower()
         if move == 'exit':
             return 'exit'
         if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
             x = int(move[0]) - 1
             y = int(move[1]) - 1
             if reverse_count(board, player1box, x, y) == False:
                 continue
             else:
                 break
         else:
             print('This is not a right move. Type a x number (1-8), and then a y number (1-8).')
             print('For example, the combination 18 is the bottom left box in the corner.')
     return [x, y]



def human_play2(board, player2box):
     DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
     while True:
         print('Enter your move, or type exit to end the game.')
         move = input().lower()
         if move == 'exit':
             return 'exit'
         if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
             x = int(move[0]) - 1
             y = int(move[1]) - 1
             if reverse_count(board, player2box, x, y) == False:
                 continue
             else:
                 break
         else:
             print('This is not a right move. Type a x number (1-8), and then a y number (1-8).')
             print('For example, the combination 18 is the bottom left corner.')
     return [x, y]



def computer_play(board, computerbox):
    possibleMoves = valid_moves(board, computerbox)
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if Corner(x, y):
            return [x, y]
    bestScore = -1
    for x, y in possibleMoves:
        copyboard = compute_counts(board)
        add_checker(copyboard, computerbox, x, y)
        score = Score(copyboard)[computerbox]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove



def valid_moves(board, box):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if reverse_count(board, box, x, y) != False:
                validMoves.append([x, y])
    return validMoves



def Corner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)



def Score(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == '1':
                xscore += 1
            if board[x][y] == '2':
                oscore += 1
    return {'1':xscore, '2':oscore}



def Start():
    box = ''
    while not (box == '1' or box == '2'):
        print('Do you want to be player 1 or 2?')
        box = input().upper()
    if box == '1':
        return ['1', '2']
    else:
        return ['2', '1']



def Start1():
    choice = ''
    while not (choice == 'P' or choice == 'C'):
        print('Do you want to play against a Player or the Computer?')
        print('Type P for Player or C for Computer.')
        choice = input().upper()
    if choice == 'P': 
        return 'Player'
    else:
        return 'Computer'
        
            

def who_plays_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'



def who_plays_first1():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'



def print_score(playerbox, computerbox):
    scores = Score(mainBoard)
    print('You have %s points. The Computer has %s points.' % (scores[playerbox], scores[computerbox]))



def print_score1(player1box, player2box):
    scores = Score(mainBoard)
    print('Player1 has %s points. Player2 has %s points.' % (scores[player1box], scores[player2box]))



print('WELCOME TO OTHELLLO!')
while True:
    mainBoard = print_board()
    reset_board(mainBoard)
    choice = Start1()
    turn = who_plays_first()
    if choice == 'Player':
        player1box, player2box = Start()
        turn = who_plays_first1()
        print('' + turn +  ' plays first')
        while True:
            player1box = '1'
            player2box = '2'
            if turn == 'Player1':
                create_board(mainBoard)
                print_score1(player1box, player2box)
                print('It\'s Player1\'s turn')
                move = human_play1(mainBoard, player1box)
                if move == 'exit':
                    print('THANKS FOR PLAYING!')
                    sys.exit()
                else:
                    add_checker(mainBoard, player1box, move[0], move[1])
                if valid_moves(mainBoard, player2box) == []:
                    break
                else:
                    turn = 'Player2'
            else:
                create_board(mainBoard)
                print_score1(player1box, player2box)
                print('It\'s Player2\'s turn')
                move = human_play2(mainBoard, player2box)
                if move == 'exit':
                    print('THANKS FOR PLAYING!')
                    sys.exit()
                else:
                    add_checker(mainBoard, player2box, move[0], move[1])
                if valid_moves(mainBoard, player1box) == []:
                    break
                else:
                    turn = 'Player1'

        create_board(mainBoard)
        scores = Score(mainBoard)
        print('1 scored %s points. 2 scored %s points.' % (scores['1'], scores['2']))
        if scores[player1box] > scores[player2box]:
            print('CONGRATULATIONS! Player1 defeated Player2 by %s points!' % (scores[player1box] - scores[player2box]))
        elif scores[player1box] < scores[player2box]:
            print('CONGRATULATIONS!. Player2 defeated Player1 by %s points.' % (scores[player2box] - scores[player1box]))
        else:
            print('TIE!')
            break
        
    elif choice == 'Computer':
        playerbox, computerbox = Start()
        turn == who_plays_first()
        print('The ' + turn + ' plays first.')
        while True:
            if turn == 'Player':
                create_board(mainBoard)
                print_score(playerbox, computerbox)
                move = human_play(mainBoard, playerbox)
                if move == 'exit':
                    print('THANKS FOR PLAYING!')
                    sys.exit()
                else:
                    add_checker(mainBoard, playerbox, move[0], move[1])
                if valid_moves(mainBoard, computerbox) == []:
                    break
                else:
                    turn = 'Computer'
            else:
                create_board(mainBoard)
                print_score(playerbox, computerbox)
                input('Press enter to see the Computer\'s move.')
                x, y = computer_play(mainBoard, computerbox)
                add_checker(mainBoard, computerbox, x, y)
                if valid_moves(mainBoard, playerbox) == []:
                    break
                else:
                    turn = 'Player'
    
        create_board(mainBoard)
        scores = Score(mainBoard)
        print('1 scores %s points. 2 scored %s points.' % (scores['1'], scores['2']))
        if scores[playerbox] > scores[computerbox]:
            print('CONGRATULATIONS! You defeated the Computer by %s points!' % (scores[playerbox] - scores[computerbox]))
        elif scores[playerbox] < scores[computerbox]:
            print('The Computer wins. You lost by %s points.' % (scores[computerbox] - scores[playerbox]))
        else:
            print('TIE!')
            break

    else:
        break




