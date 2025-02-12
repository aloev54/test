from game.ship import Ship

class Board:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [['0' for _ in range(10)] for _ in range(10)]  # '1' - корабль, '0' - пустая клетка
        else:
            self.grid = grid
        self.hits = [[False for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.ship_count = 0

    def display_cell(self, row, col):
        if self.hits[row][col]:
            return 'X'
        return self.grid[row][col]

    def hidden_cell(self, row, col):
        if self.hits[row][col]:
            return 'X'
        return self.grid[row][col]

    def mark_hit(self, x, y):
        self.hits[x][y] = True
        return self.grid[x][y] == '1'
    
    def count_ships(self):
        visited = [[False for _ in range(10)] for _ in range(10)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, ship_cells):
            visited[row][col] = True
            ship_cells.append((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and not visited[nr][nc] and self.grid[nr][nc] == '1':
                    dfs(nr, nc, ship_cells)

        for row in range(10):
            for col in range(10):
                if self.grid[row][col] == '1' and not visited[row][col]:
                    ship_cells = []
                    dfs(row, col, ship_cells)
                    self.ships.append(Ship(ship_cells))
        self.ship_count = len(self.ships)
