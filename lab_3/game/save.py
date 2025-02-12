import os

from game.board import Board
from game.ship import Ship
from game.player import Player

def save_game(player1, player2, turn, current_player):
    print("Сохранение игры...")

    # Сохраняем доски игроков
    save_board_to_file("source/lastgame_player_1.cfg", player1.board)
    save_board_to_file("source/lastgame_player_2.cfg", player2.board)

    # Сохраняем текущий ход и игрока
    try:
        with open("source/lastgame.cfg", "w") as file:
            file.write(f"{turn}\n{current_player}\n")
        print("Игра сохранена!")
    except IOError as e:
        print(f"Ошибка сохранения состояния игры: {e}")

def save_board_to_file(filename, board):
    try:
        with open(filename, "w") as file:
            for row in board.grid:
                file.write("".join(row) + "\n")
            for ship in board.ships:
                if isinstance(ship, Ship):
                    ship_coords = " ".join([f"{cell[0]},{cell[1]}" for cell in ship.cells])
                else:
                    ship_coords = " ".join([f"{cell[0]},{cell[1]}" for cell in ship])
                file.write(ship_coords + "\n")
    except IOError as e:
        print(f"Ошибка при сохранении в файл {filename}: {e}")

def load_game():
    try:
        with open("source/lastgame.cfg", "r") as file:
            lines = file.readlines()
            turn = int(lines[0].strip())
            current_player = lines[1].strip()
    except (IOError, ValueError, IndexError) as e:
        raise RuntimeError(f"Ошибка чтения файла lastgame.cfg: {e}")

    if not os.path.exists("source/lastgame_player_1.cfg"):
        raise RuntimeError("Файл lastgame_player_1.cfg не найден")
    if not os.path.exists("source/lastgame_player_2.cfg"):
        raise RuntimeError("Файл lastgame_player_2.cfg не найден")

    player1_board = load_board("source/lastgame_player_1.cfg")
    player2_board = load_board("source/lastgame_player_2.cfg")

    player1 = Player(name="Player 1", board=player1_board)
    player2 = Player(name="Player 2", board=player2_board)

    return player1, player2, turn, current_player

def load_board(filename):
    board = Board()
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            # Читаем сетку поля
            for i in range(10):
                line = lines[i].strip()
                board.grid[i] = list(line)

            # Читаем координаты кораблей
            for line in lines[10:]:
                ship = Ship()
                coords = line.strip().split(" ")
                for coord in coords:
                    r, c = map(int, coord.split(","))
                    ship.cells.append((r, c))
                board.ships.append(ship)
    except (IOError, ValueError, IndexError) as e:
        print(f"Ошибка при загрузке файла {filename}: {e}")

    board.ship_count = len(board.ships)
    return board
