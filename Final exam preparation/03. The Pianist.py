number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    pieces_args = input().split('|')
    piece = pieces_args[0]
    composer = pieces_args[1]
    key = pieces_args[2]

    pieces[piece] = {'composer': composer, 'key': key}

data = input()

while data != 'Stop':
    command_args = data.split('|')
    command = command_args[0]
    piece = command_args[1]

    if command == 'Add':
        composer = command_args[2]
        key = command_args[3]
        if piece not in pieces:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif command == 'Remove':
        if piece not in pieces:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            print(f'Successfully removed {piece}!')
            pieces.pop(piece)
    elif command == 'ChangeKey':
        new_key = command_args[2]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece]['population'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    data = input()

for piece, value in pieces.items():
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
