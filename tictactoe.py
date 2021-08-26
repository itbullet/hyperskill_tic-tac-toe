def game_state_analysis(_user_input):
    tictactoe_matrix = [list(_user_input[i:i + 3]) for i in range(0, len(_user_input), 3)]
    tictactoe_matrix_columns = [[_user_input[j] for j in range(i, len(_user_input), 3)] for i in range(3)]
    x_win, o_win, empty_cell = 0, 0, 0
    diagonal1, diagonal2 = [], []
# checking rows
    for row in tictactoe_matrix:
        if row.count("X") == 3:
            x_win = 1
        elif row.count("O") == 3:
            o_win = 1
        elif row.count("_"):
            empty_cell = 1
# checking columns
    for row in tictactoe_matrix_columns:
        if row.count("X") == 3:
            x_win = 1
        elif row.count("O") == 3:
            o_win = 1
        elif row.count("_"):
            empty_cell = 1
# checking diagonals
    for i, elem in enumerate(tictactoe_matrix):
        diagonal1.append(elem[i])
        diagonal2.append(elem[-(i+1)])

    if diagonal1.count("X") == 3 or diagonal2.count("X") == 3:
        x_win = 1
    elif diagonal1.count("O") == 3 or diagonal2.count("O") == 3:
        o_win = 1

    if x_win and not o_win:
        return f"X wins"
    elif o_win and not x_win:
        return f"O wins"
    elif not x_win and not o_win and not empty_cell:
        return f"Draw"


def user_coordinates():
    try:
        _user_coord_row, _user_coord_column = input("Enter the coordinates: ").split()
        return int(_user_coord_row), int(_user_coord_column)
    except ValueError:
        print("You should enter numbers!")


def draw_field(_user_input):
    print("---------")
    for i, elem in enumerate(_user_input):
        if not i % 3:
            print(f"| {elem}", end="")
        elif (i+1) % 3:
            print(f" {elem}", end="")
        else:
            print(f" {elem} |")
    print("---------")
    if game_state_analysis(_user_input):
        print(game_state_analysis(_user_input))
        return 0
    else:
        return 1


def cell_analysis(cell):
    if cell == "_":
        _state = 0
    else:
        print("This cell is occupied! Choose another one!")
        _state = 1
    return _state


def order(_player):
    if _player == "O":
        _player = "X"
    else:
        _player = "O"
    return _player


user_input = "_________"
draw_field(user_input)
game_state = 1
_range = [1, 2, 3]
player = "O"
while game_state:
    try:
        user_coordinates_row, user_coordinates_column = input("Enter the coordinates: ").split()
        user_coordinates_row = int(user_coordinates_row)
        user_coordinates_column = int(user_coordinates_column)
    except ValueError:
        print("You should enter numbers!")
        continue

    if user_coordinates_row not in _range or user_coordinates_column not in _range:
        print("Coordinates should be from 1 to 3!")
        continue

    user_input = list(user_input)
    if user_coordinates_row == 1:
        cell_state = cell_analysis(user_input[user_coordinates_column - 1])
        if not cell_state:
            player = order(player)
            user_input[user_coordinates_column - 1] = player
        else:
            continue
    else:
        cell_state = cell_analysis(user_input[(user_coordinates_row - 1) * 3 + user_coordinates_column - 1])
        if not cell_state:
            player = order(player)
            user_input[(user_coordinates_row - 1) * 3 + user_coordinates_column - 1] = player
        else:
            continue

    game_state = draw_field("".join(user_input))
