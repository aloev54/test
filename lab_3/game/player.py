class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def make_move(self, x, y, opponent):
        if x < 0 or x >= 10 or y < 0 or y >= 10:
            print("Координаты за пределами поля. Попробуйте снова.")
            return False

        if opponent.board.hits[x][y]:
            print("Вы уже стреляли в эту клетку. Попробуйте снова.")
            return False

        if opponent.board.mark_hit(x, y):
            for ship in opponent.board.ships:
                if ship.mark_hit(x, y):
                    if ship.is_sunk:
                        print(f"Корабль противника уничтожен! Осталось кораблей: {opponent.board.ship_count - 1}")
                        opponent.board.ship_count -= 1
                    break
            return True

        print("Мимо! Ход переходит другому игроку.")
        return False
