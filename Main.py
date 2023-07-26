'''
Tic Tac Toe
Repo owner: Md. Fahim Bin Amin
Description: A console based Tic Tac Toe game
-------------------------------------------------------------
'''

import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        # Initialize an empty 3x3 board with dashes '-'
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        # Randomly choose which player goes first (0 for 'O', 1 for 'X')
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        # Mark the spot on the board with the player's symbol
        self.board[row][col] = player

    def has_player_won(self, player):
        # Check if the player has won in rows, columns, or diagonals
        n = len(self.board)
        for i in range(n):
            # Check rows
            if all(self.board[i][j] == player for j in range(n)):
                return True

            # Check columns
            if all(self.board[j][i] == player for j in range(n)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(n)):
            return True
        if all(self.board[i][n - i - 1] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        # Check if the board is completely filled with symbols
        return all(self.board[i][j] != '-' for i in range(3) for j in range(3))

    def swap_player_turn(self, player):
        # Swap player turn between 'X' and 'O'
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        # Display the current state of the board
        for row in self.board:
            print(' '.join(row))
        print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'Player {player} turn')

                # Get user input for row and column to fix the spot
                row, col = list(map(int, input('Enter row & column numbers to fix spot: ').split()))
                print()

                # Convert to 0-based index for internal board representation
                row -= 1
                col -= 1

                # Check if the spot is valid and not already taken
                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '-':
                    self.fix_spot(row, col, player)

                    # Check if the current player has won
                    if self.has_player_won(player):
                        print(f'Player {player} wins the game!')
                        game_over = True
                    elif self.is_board_filled():
                        print('Match Draw!')
                        game_over = True
                    else:
                        player = self.swap_player_turn(player)
                else:
                    print('Invalid spot. Try again!')

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
