import random

from game.board import Board


def load_board(filepath):
    with open(filepath, 'r') as f:
        return Board([list(line.strip()) for line in f])

def format_coordinates(row, col):
    return f"({chr(col + 65)}, {row + 1})"


class Bot:
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.shots = set()

    def make_move(self, opponent):
        # Try to find damaged but not sunk ship
        for ship in opponent.board.ships:
            if not ship.is_sunk:
                for x, y in ship.cells:
                    if opponent.board.hits[x][y]:
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if self.is_valid_move(nx, ny):
                                self.shots.add((nx, ny))
                                hit = opponent.board.grid[nx][ny] == '1'
                                opponent.board.hits[nx][ny] = True
                                return nx, ny, hit

        # If no damaged ship, shoot randomly
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if self.is_valid_move(x, y):
                self.shots.add((x, y))
                hit = opponent.board.grid[x][y] == '1'
                opponent.board.hits[x][y] = True
                return x, y, hit



    def is_valid_move(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10 and (x, y) not in self.shots


def bot_test_game():
    board1 = load_board("source/newgame_player_1.cfg")
    board2 = load_board("source/newgame_player_2.cfg")

    board1.count_ships()
    board2.count_ships()

    bot1 = Bot("Bot 1", board1)
    bot2 = Bot("Bot 2", board2)

    turn = 1
    active_bot, opponent_bot = bot1, bot2

    print(f"Начало игры: {bot1.name} с {board1.ship_count} кораблями, {bot2.name} с {board2.ship_count} кораблями")

    while board1.ship_count != 0 or board2.ship_count != 0:
        print(f"\nХод {turn}. Ходит: {active_bot.name}")

        x, y, hit = active_bot.make_move(opponent_bot)
        coords = format_coordinates(x, y)
        print(f"{active_bot.name} стреляет в {coords}: {'Попадание' if hit else 'Мимо'}")

        if hit:
            for ship in opponent_bot.board.ships:
                if ship.mark_hit(x, y) and ship.is_sunk:
                    print(f"Корабль {opponent_bot.name} уничтожен!")
                    opponent_bot.board.ship_count -= 1

        if opponent_bot.board.ship_count == 0:
            print(f"{active_bot.name} победил!")
            break

        if not hit:
            active_bot, opponent_bot = opponent_bot, active_bot
            turn += 1

        print(board1.ship_count, board2.ship_count)

    print("=== Игра завершена ===")

if __name__ == "__main__":
    bot_test_game()
