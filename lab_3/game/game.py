from game.player import Player
from game.save import load_board, save_game

def start_new_game():
    player1 = Player("Player 1", load_board("source/newgame_player_1.cfg"))
    player2 = Player("Player 2", load_board("source/newgame_player_2.cfg"))

    player1.board.ships = count_ships(player1.board)
    player1.board.ship_count = len(player1.board.ships)
    
    player2.board.ships = count_ships(player2.board)
    player2.board.ship_count = len(player2.board.ships)

    print("Game started! Player 1 goes first.")
    run_game(player1, player2, 1, "Player 1")

def run_game(player1, player2, turn, current_player):
    active_player, opponent = (player1, player2) if current_player == "Player 1" else (player2, player1)

    while True:
        print(f"{active_player.name}, your turn:")
        display_boards(active_player.board, opponent.board)

        input_coords = input("Enter coordinates (e.g., a1) or 'exit' to save: ").strip()

        if input_coords.lower() == "exit":
            save_game(player1, player2, turn, active_player.name)
            print("Game saved. Goodbye!")
            break

        try:
            x, y = parse_coordinates(input_coords)
        except ValueError as e:
            print(e)
            continue

        if opponent.board.hits[x][y]:
            print("You've already shot here. Try again.")
            continue

        hit = make_move(active_player, opponent, x, y)
        if hit:
            print("Hit!")
            if opponent.board.ship_count == 0:
                print(f"Congratulations, {active_player.name} wins!")
                break
        else:
            print("Miss! Turn passes to the next player.")
            active_player, opponent = opponent, active_player
            turn += 1

def display_boards(own_board, enemy_board):
    print("|     Your Board:     |       |     Enemy Board:    |")
    print("   A B C D E F G H I J           A B C D E F G H I J")
    for i in range(10):
        print(f"{i+1:2} ", end="")
        print(" ".join(own_board.display_cell(i, j) for j in range(10)), end="")
        print(f"        {i+1:2} ", end="")
        print(" ".join(enemy_board.hidden_cell(i, j) for j in range(10)))

def parse_coordinates(input_str):
    if len(input_str) < 2 or len(input_str) > 3:
        raise ValueError("Invalid input format. Use format like 'a1'.")

    col = ord(input_str[0].lower()) - ord('a')
    if not (0 <= col < 10):
        raise ValueError("Invalid column. Use letters A-J.")

    try:
        row = int(input_str[1:]) - 1
    except ValueError:
        raise ValueError("Invalid row. Use numbers 1-10.")

    if not (0 <= row < 10):
        raise ValueError("Invalid row. Use numbers 1-10.")

    return row, col

def count_ships(board):
    visited = [[False] * 10 for _ in range(10)]
    ships = []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(row, col, ship_cells):
        visited[row][col] = True
        ship_cells.append((row, col))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 10 and 0 <= nc < 10 and not visited[nr][nc] and board.grid[nr][nc] == '1':
                dfs(nr, nc, ship_cells)

    for row in range(10):
        for col in range(10):
            if board.grid[row][col] == '1' and not visited[row][col]:
                ship_cells = []
                dfs(row, col, ship_cells)
                ships.append(ship_cells)

    return ships

def make_move(player, opponent, x, y):
    opponent.board.hits[x][y] = True
    if opponent.board.grid[x][y] == "1":
        # Check if a ship is sunk (placeholder logic)
        opponent.board.ship_count -= 1  # Adjust according to your logic
        return True
    return False
