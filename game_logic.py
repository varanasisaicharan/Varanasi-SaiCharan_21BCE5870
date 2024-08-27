class Game:
    def __init__(self):
        self.board = [['' for _ in range(5)] for _ in range(5)]
        self.players = {'A': [], 'B': []}
        self.current_turn = 'A'

    def setup_board(self, player, characters):
        if player == 'A':
            row = 0
        else:
            row = 4
        
        for i, char in enumerate(characters):
            self.board[row][i] = f"{player}-{char}"
            self.players[player].append((row, i))

    def move_character(self, player, char_name, move):
        if player != self.current_turn:
            return False, "Not your turn!"

        char_pos = None
        for pos in self.players[player]:
            if self.board[pos[0]][pos[1]].split('-')[1] == char_name:
                char_pos = pos
                break

        if not char_pos:
            return False, "Character not found!"

        # Determine new position based on move
        new_pos = self.calculate_new_position(char_pos, move)
        if not self.is_valid_position(new_pos):
            return False, "Invalid move!"

        # Check for capture
        opponent = 'B' if player == 'A' else 'A'
        if self.board[new_pos[0]][new_pos[1]]:
            if self.board[new_pos[0]][new_pos[1]].split('-')[0] == opponent:
                self.players[opponent].remove(new_pos)
            else:
                return False, "Cannot move onto a friendly character!"

        # Update board and position
        self.board[char_pos[0]][char_pos[1]] = ''
        self.board[new_pos[0]][new_pos[1]] = f"{player}-{char_name}"
        self.players[player].remove(char_pos)
        self.players[player].append(new_pos)

        # Switch turn
        self.current_turn = opponent

        # Check for game over
        if not self.players[opponent]:
            return True, "Game Over! Player {} wins!".format(player)

        return True, "Move successful!"

    def calculate_new_position(self, position, move):
        row, col = position
        if move == 'L':
            col -= 1
        elif move == 'R':
            col += 1
        elif move == 'F':
            row -= 1
        elif move == 'B':
            row += 1
        # Add logic for Hero2 diagonal and Hero1's two-step moves here
        return (row, col)

    def is_valid_position(self, position):
        row, col = position
        return 0 <= row < 5 and 0 <= col < 5

