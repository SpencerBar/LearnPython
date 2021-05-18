theBoard = {'t1': ' ', 't2': ' ', 't3': ' ',
            'm1': ' ', 'm2': ' ', 'm3': ' ',         
            'b1': ' ', 'b2': ' ', 'b3': ' '}

def printBoard(board):
    print(board['t1'] + '|' + board['t2'] + '|' + board['t3'])
    print('-+-+-')
    print(board['m1'] + '|' + board['m2'] + '|' + board['m3'])
    print('-+-+-')
    print(board['b1'] + '|' + board['b2'] + '|' + board['b3'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)