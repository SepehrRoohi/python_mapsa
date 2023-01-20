import random
CELLS = [
    (0,0),(1,0),(2,0),(3,0),
    (0,1),(1,1),(2,1),(3,1),
    (0,2),(1,2),(2,2),(3,2),
    (0,3),(1,3),(2,3),(3,3)
]

def get_location():
    return random.sample(CELLS, 3)



def get_moves(player):
    moves = ['up','down','right','left']
    x, y = player
    
    if x == 0:
        moves.remove('left')
    if x == 3:
        moves.remove("right")
    if y == 0:
        moves.remove("up")
    if y == 3:
        moves.remove("down")
    
    return moves

def move_player(player, move):
    x, y = player

    if move == 'up':
        y -= 1
    if move == 'down':
        y += 1
    if move == 'left':
        x -= 1
    if move == 'right':
        x += 1

    return x, y

def draw_map(player):
    print('_'*4)
    title = '|{}'
    for cell in CELLS:
        x, y = cell
        if x < 3:
            endline = ''
            if cell == player:
                output = title.format('X')
            else:
                

        else:
            endline = '\n'
player, dragon, door = get_location()

while True:
    valid_moves = get_moves(player)
    print(f'you are in room {player}')
    print(f'you can move in: {valid_moves}')
    move = input('please enter your move: ').casefold()
    if move in valid_moves:
        player = move_player(player, move)
        if player == dragon:
            print('you win the game!')
        if player == door:
            print('you lose the game!')
    else:
        print('please enter a valid move')
