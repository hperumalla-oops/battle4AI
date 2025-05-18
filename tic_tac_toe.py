def printBoard():
    print(board[1], '|', board[2], '|', board[3])
    print(board[4], '|', board[5], '|', board[6])
    print(board[7], '|', board[8], '|', board[9])

def spaceFree(pos): return board[pos] == ' '

def insert(letter, pos):
    if spaceFree(pos):
        board[pos] = letter
        printBoard()
        print("--------")
        if draw(): print("Draw!"); exit()
        if win(): print("Bot wins!" if letter == 'X' else "Player wins!"); exit()
    else:
        insert(letter, int(input("Invalid! Enter new pos: ")))

def win():
    for x in combos:
        if board[x[0]] == board[x[1]] == board[x[2]] != ' ': return True
    return False

def whoWon(mark):
    for x in combos:
        if board[x[0]] == board[x[1]] == board[x[2]] == mark: return True
    return False

def draw(): return all(board[k] != ' ' for k in board)

def playerMove(): insert(player, int(input("Enter pos for 'O': ")))

def compMove():
    best, move = -800, 0
    for k in board:
        if spaceFree(k):
            board[k] = bot
            s = minimax(False)
            board[k] = ' '
            if s > best: best, move = s, k
    insert(bot, move)

def minimax(maximizing):
    if whoWon(bot): return 1
    if whoWon(player): return -1
    if draw(): return 0
    if maximizing:
        best = -800
        for k in board:
            if spaceFree(k):
                board[k] = bot
                best = max(best, minimax(False))
                board[k] = ' '
        return best
    else:
        best = 800
        for k in board:
            if spaceFree(k):
                board[k] = player
                best = min(best, minimax(True))
                board[k] = ' '
        return best

board = {i: ' ' for i in range(1, 10)}
combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
player, bot = 'O', 'X'

printBoard()
print("--------")
print("Player goes first!\nPositions:\n1 2 3\n4 5 6\n7 8 9\n")

while not win():
    playerMove()
    if win(): break
    compMove()