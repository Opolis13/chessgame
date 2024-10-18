class ChessVar():
    """
    Class representing a basic implementation of a chess game.
    It provides functionalities for managing the chessboard, tracking game state, and handling player turns.
    The class includes attributes for storing the current board configuration, player turns, game state, and captured pieces.
    It supports methods for initializing the board, retrieving the game state, printing the board, switching player turns, and converting chess square notation to coordinates.
    The class also serves as a foundational structure for implementing chess game logic and can be extended to include more advanced features such as piece movement and capturing.
    """

    def __init__(self):
        self._board = self.board_init()
        self._turn = "WHITE"  # Initialize turn to start with White
        self._game_state = "UNFINISHED"

        # store which pieces have been lost in the game
        self._white_lost_pieces = []
        self._black_lost_pieces = []

        # list to store the fairy pieces
        self._white_fairy_pieces = ["F", "H"]
        self._black_fairy_pieces = ["f", "h"]

    # list to store the unicode chess pieces
    white_piece = ["♚", "♛", "♜", "♝", "♞", "♟︎", "F", "H"]
    black_piece = ["♔", "♕", "♖", "♗", "♘", "♙", "f", "h"]
    white_major = ["♚", "♛", "♜", "♝", "♞", "F", "H"]
    black_major = ["♔", "♕", "♖", "♗", "♘", "f", "h"]
    kings = ["♔", "♚"]

    def board_init(self):
        """
        Methods to initialize the visual board
        """
        board = [["" for row in range(8)] for column in range(8)]

        # setting up pawns for black and white
        for col in range(8):
            board[1][col] = "♙"
            board[2][col] = "."
            board[3][col] = "."
            board[4][col] = "."
            board[5][col] = "."
            board[6][col] = "♟︎"

        # adding the major pieces to the board
        board[0] = ["♖", "♘", "♗", "♔", "♕", "♗", "♘", "♖"]
        board[7] = ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]
        return board

    def get_game_state(self):
        """
        Get the current game state as a string if it is in progress or a player has won.
        """

        if self._black_king_lost == True:
            return "WHITE WINS"
        if self._white_king_lost == True:
            return "BLACK WINS"
        else:
            return "UNFINISHED"

    def king_status(self):
        if "♚" in self._white_lost_pieces:
            self._game_state = "BLACK_WON"
        if "♔" in self._black_lost_pieces:
            self._game_state = "WHITE_WON"

    def get_board(self):
        """
        Print a visual representation of the board to the console.
        """

        board_state = "  a b c d e f g h\n"  # Add column labels
        for index, row in enumerate(self._board):
            board_state += f"{8 - index} "  # Add row numbers in reverse order
            board_state += " ".join(row) + "\n"
        print(board_state)

    def get_turn(self):
        """
        Return which players turn it currently is
        """

        return self._turn

    def get_white_lost_pieces(self):
        """
        return the major pieces white has lost
        """
        return self._white_lost_pieces

    def get_black_lost_pieces(self):
        """
        return the major pieces black has lost
        """
        return self._black_lost_pieces

    def get_rem_white_fairy(self):
        """
        return the remaining fairy pieces for white
        """
        return self._white_fairy_pieces

    def get_rem_black_fairy(self):
        """
        return the remaining fairy pieces for black
        """
        return self._black_fairy_pieces

    def switch_turn(self):
        """
        Switch players turn
        """

        self._turn = "BLACK" if self._turn == "WHITE" else "WHITE"

    def enter_fairy_piece(self, piece, location):
        """
        Enter the fairy piece into the board
        """
        row, col = self.square_to_coords(location)
        # Check if the player has lost a major piece (queen, rook, bishop, knight)
        if (self._turn == "WHITE" and len(self._white_lost_pieces) >= 1) or (self._turn == "BLACK" and len(self._black_lost_pieces) >= 1):
            # Check if the target location is within the home ranks
            if (self._turn == "WHITE" and row >= 6) or (self._turn == "BLACK" and row <= 1):

                # Check if piece has entered previously
                if self._turn == "WHITE" and piece in self._white_fairy_pieces or self._turn == "BLACK" and piece in self._black_fairy_pieces:
                    # Check if the target location is empty
                    if self._board[row][col] == ".":
                        # Place the fairy piece on the target location
                        self._board[row][col] = piece
                        # Remove piece from fairy piece list
                        if self._turn == "WHITE":
                            self._white_fairy_pieces.remove(piece)
                        else:
                            self._black_fairy_pieces.remove(piece)
                        # Switch turn
                        self.switch_turn()
                        return True

        if (self._turn == "WHITE" and len(self._white_lost_pieces) >= 2) or (self._turn == "BLACK" and len(self._black_lost_pieces) >= 2):
            # Check if the target location is within the home ranks
            if (self._turn == "WHITE" and row >= 6) or (self._turn == "BLACK" and row <= 1):
                # Check if piece has entered previously
                if self._turn == "WHITE" and piece in self._white_fairy_pieces or self._turn == "BLACK" and piece in self._black_fairy_pieces:
                    # Check if the target location is empty
                    if self._board[row][col] == ".":
                        # Place the fairy piece on the target location
                        self._board[row][col] = piece
                        # Remove piece from fairy piece list
                        if self._turn == "WHITE":
                            self._white_fairy_pieces.remove(piece)
                        else:
                            self._black_fairy_pieces.remove(piece)
                        # Switch turn
                        self.switch_turn()
                        return True
        print("Fairy piece cannot enter this location\n")
        return False

    def pawn_move(self, start_row, start_col, end_row, end_col):
        """Checks the validity of a pawn move based on its movement and capture rules. Parameters:
        start_row: The starting row of the pawn.
        start_col: The starting column of the pawn.
        end_row: The ending row of the pawn.
        end_col: The ending column of the pawn.
        Returns True if the move is valid and updates the board, False otherwise.
        """

        piece = self._board[start_row][start_col]

        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            # Check if piece is moving within the limits of the board
            print("Invalid move: Out of bounds\n")
            return False

        if abs(start_row - end_row) == 0:
            # Check if the player is moving the piece or not
            print("Invalid move: You have to move your piece\n")
            return False

        if start_col == end_col:
            if abs(start_row - end_row) == 1:   # The pawn is moving one space forward
                # if there is a piece in the way return false
                if self._board[end_row][end_col] != ".":
                    print("Invalid move: You are trying to capture your piece\n")
                    return False

                self._board[end_row][end_col] = piece
                self._board[start_row][start_col] = "."
                self.switch_turn()
                return True

            elif abs(start_row - end_row) == 2:  # The pawn is moving two spaces forward
                # Check if the intermediate squares are empty
                if self._board[end_row][end_col] != "." or self._board[end_row - 1][end_col] != ".":
                    print("Invalid move: There are pieces in the way\n")
                    return False

                # Verify this is the pawn's first move and can move two squares
                if piece == "♟︎" and start_row == 6 and self._board[start_row - 2][start_col] == ".":
                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    return True
                elif piece == "♙" and start_row == 1 and self._board[start_row + 2][start_col] == ".":
                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    return True
                else:
                    print(
                        "Invalid move: Pawns can only move two squares on their first move\n")
                    return False

            else:
                return False

        elif abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1:
            if self._board[end_row][end_col] != ".":
                if (self._turn == "WHITE" and self._board[end_row][end_col] in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] in self.black_piece):
                    # check to see if piece is capturing own piece

                    print("Invalid move: You are trying to capture your piece\n")
                    return False

                captured_piece = self._board[end_row][end_col]
                if captured_piece in self.black_major:
                    self._black_lost_pieces.append(captured_piece)
                elif captured_piece in self.white_major:
                    self._white_lost_pieces.append(captured_piece)

                self._board[end_row][end_col] = piece
                self._board[start_row][start_col] = "."
                self.switch_turn()
                self.king_status()
                return True
            else:
                print("Invalid move: Pawns can only capture diagonally\n")
                return False
        else:
            print("Invalid move: Pawns can only move forward or capture diagonally\n")
            return False

    def knight_move(self, start_row, start_col, end_row, end_col):
        """Checks the validity of a knight move based on its movement and capture rules. Parameters:
        start_row: The starting row of the knight.
        start_col: The starting column of the knight.
        end_row: The ending row of the knight.
        end_col: The ending column of the knight.
        Returns True if the move is valid and updates the board, False otherwise.
        """

        piece = self._board[start_row][start_col]

        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        if abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1 or abs(start_col - end_col) == 1 and abs(start_row - end_row) == 2:
            if (self._turn == "WHITE" and self._board[end_row][end_col] in self.white_piece) or \
                    (self._turn == "BLACK" and self._board[end_row][end_col] in self.black_piece):
                # check to see if piece is capturing own piece
                print("Invalid move: You are trying to capture your piece\n")
                return False

            captured_piece = self._board[end_row][end_col]
            if captured_piece in self.black_major:
                self._black_lost_pieces.append(captured_piece)
            elif captured_piece in self.white_major:
                self._white_lost_pieces.append(captured_piece)
            self._board[end_row][end_col] = piece
            self._board[start_row][start_col] = "."
            self.switch_turn()
            self.king_status()
            return True

        else:
            print("Invalid move: Knights can only move in L-shape\n")
            return False

    def bishop_move(self, start_row, start_col, end_row, end_col):
        """
        Checks the validity of a bishop move based on its movement and capture rules. Parameters:
        start_row: The starting row of the bishop.
        start_col: The starting column of the bishop.
        end_row: The ending row of the bishop.
        end_col: The ending column of the bishop.
        Returns True if the move is valid and updates the board, False otherwise.
        """

        piece = self._board[start_row][start_col]

        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            # Check if piece is moving out of bounds
            print("Invalid move: Out of bounds\n")
            return False

        if abs(start_row - end_row) == abs(start_col - end_col):
            # Check if there are pieces in between the start and end positions
            row_direction = 1 if end_row > start_row else -1
            col_direction = 1 if end_col > start_col else -1

            current_row, current_col = start_row + row_direction, start_col + col_direction
            while current_row != end_row and current_col != end_col:
                if self._board[current_row][current_col] != ".":
                    print("Invalid move: There are pieces in the way\n")
                    return False
                current_row += row_direction
                current_col += col_direction

            if (self._turn == "WHITE" and self._board[end_row][end_col] in self.white_piece) or \
                    (self._turn == "BLACK" and self._board[end_row][end_col] in self.black_piece):
                # check to see if piece is capturing own piece
                print("Invalid move: You are trying to capture your piece\n")
                return False

            captured_piece = self._board[end_row][end_col]
            if captured_piece in self.black_major:
                self._black_lost_pieces.append(captured_piece)
            elif captured_piece in self.white_major:
                self._white_lost_pieces.append(captured_piece)

            self._board[end_row][end_col] = piece
            self._board[start_row][start_col] = "."
            self.switch_turn()
            self.king_status()
            return True

        else:
            print("Invalid move: Bishops can only move diagonally")

    def rook_move(self, start_row, start_col, end_row, end_col):
        """
        Checks the validity of a rook move based on its movement and capture rules. Parameters:

        start_row: The starting row of the rook.
        start_col: The starting column of the rook.
        end_row: The ending row of the rook.
        end_col: The ending column of the rook.
        Returns True if the move is valid and updates the board, False otherwise.
        """
        piece = self._board[start_row][start_col]

        # Bounds checking
        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        # Moving along ranks or files
        if abs(start_row - end_row) != 0 and abs(start_col - end_col) != 0:
            print("Invalid move: Rooks can only move along ranks or files\n")
            return False

        # Moving horizontally
        if start_row == end_row:
            direction = 1 if end_col > start_col else -1
            current_col = start_col + direction
            while current_col != end_col:
                if self._board[start_row][current_col] != ".":
                    print("Invalid move: There are pieces in the way\n")
                    return False
                current_col += direction

        # Moving vertically
        elif start_col == end_col:
            direction = 1 if end_row > start_row else -1
            current_row = start_row + direction
            while current_row != end_row:
                if self._board[current_row][start_col] != ".":
                    print("Invalid move: There are pieces in the way\n")
                    return False
                current_row += direction

        # Capture logic
        if (self._turn == "WHITE" and self._board[end_row][end_col] in self.white_piece) or \
                (self._turn == "BLACK" and self._board[end_row][end_col] in self.black_piece):
            print("Invalid move: You are trying to capture your piece\n")
            return False

        captured_piece = self._board[end_row][end_col]
        if captured_piece in self.black_major:
            self._black_lost_pieces.append(captured_piece)
        elif captured_piece in self.white_major:
            self._white_lost_pieces.append(captured_piece)

        self._board[end_row][end_col] = piece
        self._board[start_row][start_col] = "."
        self.switch_turn()
        self.king_status()
        return True

    def queen_move(self, start_row, start_col, end_row, end_col):
        """
            Checks the validity of a queens move based on its movement and capture rules. Parameters:

            start_row: The starting row of the queen.
            start_col: The starting column of the queen.
            end_row: The ending row of the queen.
            end_col: The ending column of the queen.
            Returns True if the move is valid and updates the board, False otherwise.
        """
        piece = self._board[start_row][start_col]

        # Bounds checking
        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        # Movement rules for queen
        if abs(start_row - end_row) == abs(start_col - end_col) or start_row == end_row or start_col == end_col:

            if abs(start_row - end_row) == abs(start_col - end_col):
                # Check if there are pieces in between the start and end positions
                row_direction = 1 if end_row > start_row else -1
                col_direction = 1 if end_col > start_col else -1

                current_row, current_col = start_row + row_direction, start_col + col_direction
                while current_row != end_row and current_col != end_col:
                    if self._board[current_row][current_col] != ".":
                        print("Invalid move: There are pieces in the way\n")
                        return False
                    current_row += row_direction
                    current_col += col_direction

            # Moving horizontally
            elif start_row == end_row:
                direction = 1 if end_col > start_col else -1
                current_col = start_col + direction
                while current_col != end_col:
                    if self._board[start_row][current_col] != ".":
                        print("Invalid move: There are pieces in the way\n")
                        return False
                    current_col += direction

            # Moving vertically
            elif start_col == end_col:
                direction = 1 if end_row > start_row else -1
                current_row = start_row + direction
                while current_row != end_row:
                    if self._board[current_row][start_col] != ".":
                        print("Invalid move: There are pieces in the way\n")
                        return False
                    current_row += direction

            # Capture logic
            if (self._turn == "WHITE" and self._board[end_row][end_col] in self.white_piece) or \
                    (self._turn == "BLACK" and self._board[end_row][end_col] in self.black_piece):
                print("Invalid move: You are trying to capture your piece\n")
                return False

            # Update board
            # if major piece append to lost pieces
            captured_piece = self._board[end_row][end_col]
            if captured_piece in self.black_major:
                self._black_lost_pieces.append(captured_piece)
            elif captured_piece in self.white_major:
                self._white_lost_pieces.append(captured_piece)

            self._board[end_row][end_col] = piece
            self._board[start_row][start_col] = "."
            self.switch_turn()
            self.king_status()
            return True
        else:
            print(
                "Invalid move: Queens can only move diagonally, horizontally or vertically\n")
            return False

    def king_move(self, start_row, start_col, end_row, end_col):
        """
        Checks the validity of a king move based on its movement and capture rules. Parameters:

        start_row: The starting row of the king.
        start_col: The starting column of the king.
        end_row: The ending row of the king.
        end_col: The ending column of the king.
        Returns True if the move is valid and updates the board, False otherwise.
        """
        piece = self._board[start_row][start_col]

        # Bounds checking
        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        if abs(start_row - end_row) == 0:
            # Check if the player is moving the piece or not
            print("Invalid move: You have to move your piece\n")
            return False

            # Check if the move is within the allowed range for the king
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            # Check if the
            if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                    (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                # Update board
                # if major piece append to lost pieces
                captured_piece = self._board[end_row][end_col]
                if captured_piece in self.black_major:
                    self._black_lost_pieces.append(captured_piece)
                elif captured_piece in self.white_major:
                    self._white_lost_pieces.append(captured_piece)

                self._board[end_row][end_col] = piece
                self._board[start_row][start_col] = "."
                self.switch_turn()
                self.king_status()
                return True
            else:
                print("Invalid move: You cannot capture your own piece\n")
                return False
        else:
            print("Invalid move: Kings can only move one square in any direction\n")
            return False

    def falcon_move(self, start_row, start_col, end_row, end_col):
        """
        Checks the validity of a falcon move based on its movement and capture rules. Parameters:


        start_row: The starting row of the falcon.
        start_col: The starting column of the falcon.
        end_row: The ending row of the falcon.
        end_col: The ending column of the falcon.
        Returns True if the move is valid and updates the board, False otherwise.
        """
        piece = self._board[start_row][start_col]

        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        if piece in self.white_piece and self._turn == "WHITE":
            # Falcon movement for white pieces
            if end_row > start_row and end_col == start_col:  # Moving vertically
                for row in range(start_row - 1, end_row, -1):
                    if self._board[row][start_col] != ".":
                        print("Invalid move: There are pieces in the way\n")
                        return False

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You cannot capture your own piece\n")
                    return False

            elif abs(start_row - end_row) == abs(start_col - end_col) and start_row > end_row:
                if abs(start_row - end_row) == abs(start_col - end_col):
                    # Check if there are pieces in between the start and end positions
                    row_direction = 1 if end_row > start_row else -1
                    col_direction = 1 if end_col > start_col else -1

                    current_row, current_col = start_row + row_direction, start_col + col_direction
                    while current_row != end_row and current_col != end_col:
                        if self._board[current_row][current_col] != ".":
                            print("Invalid move: There are pieces in the way\n")
                            return False
                        current_row += row_direction
                        current_col += col_direction

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You are trying to capture your piece\n")
                    return False

        elif piece in self.black_piece and self._turn == "BLACK":
            # Falcon movement for black pieces
            if end_row < start_row and end_col == start_col:  # Moving backwards vertically
                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You cannot capture your own piece\n")
                    return False

            elif abs(start_row - end_row) == abs(start_col - end_col) and start_row < end_row:
                if abs(start_row - end_row) == abs(start_col - end_col):
                    # Check if there are pieces in between the start and end positions
                    row_direction = 1 if end_row > start_row else -1
                    col_direction = 1 if end_col > start_col else -1

                    current_row, current_col = start_row + row_direction, start_col + col_direction
                    while current_row != end_row and current_col != end_col:
                        if self._board[current_row][current_col] != ".":
                            print("Invalid move: There are pieces in the way\n")
                            return False
                        current_row += row_direction
                        current_col += col_direction

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You are trying to capture your piece\n")
                    return False

        print("Invalid move: Falcon can only move forward like a Bishop or backward like a rook\n")
        return False

    def hunter_move(self, start_row, start_col, end_row, end_col):
        """
        Checks the validity of a hunter move based on its movement and capture rules. Parameters:

        start_row: The starting row of the hunter.
        start_col: The starting column of the hunter.
        end_row: The ending row of the hunter.
        end_col: The ending column of the hunter.
        Returns True if the move is valid and updates the board, False otherwise.
        """
        piece = self._board[start_row][start_col]

        if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
            print("Invalid move: Out of bounds\n")
            return False

        if piece in self.white_piece and self._turn == "WHITE":
            # Hunter movement for white pieces
            if end_row < start_row and end_col == start_col:  # Moving vertically
                for row in range(start_row - 1, end_row, -1):
                    if self._board[row][start_col] != ".":
                        print("Invalid move: There are pieces in the way\n")
                        return False

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You cannot capture your own piece\n")
                    return False

            elif abs(start_row - end_row) == abs(start_col - end_col) and start_row < end_row:
                if abs(start_row - end_row) == abs(start_col - end_col):
                    # Check if there are pieces in between the start and end positions
                    row_direction = 1 if end_row > start_row else -1
                    col_direction = 1 if end_col > start_col else -1

                    current_row, current_col = start_row + row_direction, start_col + col_direction
                    while current_row != end_row and current_col != end_col:
                        if self._board[current_row][current_col] != ".":
                            print("Invalid move: There are pieces in the way\n")
                            return False
                        current_row += row_direction
                        current_col += col_direction

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You are trying to capture your piece\n")
                    return False

        elif piece in self.black_piece and self._turn == "BLACK":
            # Hunter movement for black pieces
            if end_row > start_row and end_col == start_col:  # Moving forward vertically
                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You cannot capture your own piece\n")
                    return False

            elif abs(start_row - end_row) == abs(start_col - end_col) and start_row > end_row:
                if abs(start_row - end_row) == abs(start_col - end_col):
                    # Check if there are pieces in between the start and end positions
                    row_direction = 1 if end_row > start_row else -1
                    col_direction = 1 if end_col > start_col else -1

                    current_row, current_col = start_row + row_direction, start_col + col_direction
                    while current_row != end_row and current_col != end_col:
                        if self._board[current_row][current_col] != ".":
                            print("Invalid move: There are pieces in the way\n")
                            return False
                        current_row += row_direction
                        current_col += col_direction

                if (self._turn == "WHITE" and self._board[end_row][end_col] not in self.white_piece) or \
                        (self._turn == "BLACK" and self._board[end_row][end_col] not in self.black_piece):
                    # Update board
                    # if major piece append to lost pieces
                    captured_piece = self._board[end_row][end_col]
                    if captured_piece in self.black_major:
                        self._black_lost_pieces.append(captured_piece)
                    elif captured_piece in self.white_major:
                        self._white_lost_pieces.append(captured_piece)

                    self._board[end_row][end_col] = piece
                    self._board[start_row][start_col] = "."
                    self.switch_turn()
                    self.king_status()
                    return True
                else:
                    print("Invalid move: You are trying to capture your piece\n")
                    return False

        print("Invalid move: Hunter can only move forward like a rook or backward like a bishop\n")
        return False

    def make_move(self, start, end):
        """
        Choose a square holding a piece using algebraic notation and choose where to move it
        """

        start_row, start_col = self.square_to_coords(start)
        end_row, end_col = self.square_to_coords(end)
        piece = self._board[start_row][start_col]
        if self._game_state != "UNFINISHED":
            print(self.get_game_state())

        if piece == ".":
            print("There is no piece on this square\n")
            return False

        if self._turn == "WHITE" and piece in self.black_piece:
            print("Invalid move: This is not your piece\n")
            return False

        elif self._turn == "BLACK" and piece in self.white_piece:
            print("Invalid move: This is not your piece\n")
            return False

        elif piece in self.white_piece and self._turn == "WHITE":
            if piece == "♟︎":
                self.pawn_move(start_row, start_col, end_row, end_col)

            elif piece == "♞":
                self.knight_move(start_row, start_col, end_row, end_col)

            elif piece == "♝":
                self.bishop_move(start_row, start_col, end_row, end_col)

            elif piece == "♜":
                self.rook_move(start_row, start_col, end_row, end_col)

            elif piece == "♛":
                self.queen_move(start_row, start_col, end_row, end_col)

            elif piece == "♚":
                self.king_move(start_row, start_col, end_row, end_col)

            elif piece == "F":
                self.falcon_move(start_row, start_col, end_row, end_col)

            elif piece == "H":
                self.hunter_move(start_row, start_col, end_row, end_col)

            else:
                print("Invalid move\n")
                return False

        elif piece in self.black_piece and self._turn == "BLACK":
            if piece == "♙":
                self.pawn_move(start_row, start_col, end_row, end_col)

            elif piece == "♘":
                self.knight_move(start_row, start_col, end_row, end_col)

            elif piece == "♗":
                self.bishop_move(start_row, start_col, end_row, end_col)

            elif piece == "♖":
                self.rook_move(start_row, start_col, end_row, end_col)

            elif piece == "♕":
                self.queen_move(start_row, start_col, end_row, end_col)

            elif piece == "♔":
                self.king_move(start_row, start_col, end_row, end_col)

            elif piece == "f":
                self.falcon_move(start_row, start_col, end_row, end_col)

            elif piece == "h":
                self.hunter_move(start_row, start_col, end_row, end_col)

            else:
                print("Invalid move\n")
                return False

    def update_game_state(self):
        """
        Update game state based on the current board state
        """

        pass

    def square_to_coords(self, square):
        """
        Convert chess square notation (e.g., 'a1') to coordinates (row, column)
        """
        col = ord(square[0]) - ord('a')
        row = 8 - int(square[1])
        return row, col


def main():
    chess = ChessVar()
    chess.board_init()
    chess.get_board()

    # test for full chess game

    # TEST FOR PAWN MOVEMENT / CAPTURE

    # DOUBLE MOVE TEST AND PIECE CAPTURE TEST
    # chess.make_move("e2", "e4")  # valid move test (pawn)
    # chess.get_board()
    # chess.make_move("d7", "d5")  # valid move test (pawn)
    # chess.get_board()
    # chess.make_move("e4", "d5")  # valid move test (pawn)
    # chess.get_board()
    # chess.make_move("c7", "c6")
    # chess.get_board()
    # chess.make_move("d5", "c6")
    # chess.get_board()
    # chess.make_move("b7", "c6")
    # chess.get_board()

    # SINGLE MOVE AND ATTEMPT TO CAPTURE OWN PIECE TEST
    # chess.make_move("e2", "e3")
    # chess.get_board()
    # chess.make_move("e7", "e5")
    # chess.get_board()
    # chess.make_move("d2", "e3")

    # TEST FOR KNIGHT MOVEMENT / CAPTURE

    # BASIC MOVEMENT AND CAPTURE TEST
    # chess.make_move("b1", "c3")
    # chess.get_board()
    # chess.make_move("b8", "c6")
    # chess.get_board()
    # chess.make_move("c3", "b5")
    # chess.get_board()
    # chess.make_move("a7", "a6")
    # chess.get_board()
    # chess.make_move("b5", "d6")
    # chess.get_board()
    # chess.make_move("e7", "d6")
    # chess.get_board()
    # chess.make_move("h2", "h3")
    # chess.get_board()

    # CHECK IF PIECES CAN ESCAPE THE BOARD
    # chess.make_move("g1", "h3")
    # chess.get_board()
    # chess.make_move("g7", "g5")
    # chess.get_board()
    # chess.make_move("h3", "i5")
    # chess.get_board()

    # TEST FOR BISHOP MOVEMENT / CAPTURE
    # chess.make_move("g2", "g3")
    # chess.get_board()
    # chess.make_move("g7", "g6")
    # chess.get_board()
    # chess.make_move("f1", "h3")
    # chess.get_board()

    # TEST FOR QUEEN MOVEMENT / CAPTURE
    # chess.make_move("e2", "e4")
    # chess.make_move("d7", "d5")
    # chess.make_move("e1", "e3")
    # chess.make_move("e8", "a4")
    # chess.make_move("e3", "a7")
    # chess.make_move("a4", "a7")
    # chess.get_board()
    # print(chess.get_turn())

    # # TEST FOR KING MOVEMENT/ CAPTURE
    # chess.make_move("e2", "e4")
    # chess.make_move("d7", "d5")
    # chess.make_move("d1", "e2")
    # chess.make_move("d5", "e4")
    # chess.make_move("e2", "e3")
    # chess.make_move("d8", "d7")
    # chess.make_move("e3", "e4")
    # chess.get_board()

    # TEST FOR ROOK MOVEMENT / CAPTURE
    # chess.make_move("h2", "h4")
    # chess.make_move("g7", "g6")
    # chess.make_move("h1", "h3")
    # chess.make_move("g6", "g5")
    # chess.make_move("h3", "a3")
    # chess.make_move("g5", "h4")
    # chess.make_move("a3", "a7")
    # chess.get_board()
    # print(chess.get_turn())

    # # TEST GRAVEYARD FOR LOST PIECES AND ENTERING FAIRY PIECES
    # chess.make_move("d2", "d4")
    # chess.make_move("g8", "f6")
    # chess.make_move("e1", "a5")
    # chess.make_move("b8", "c6")
    # chess.make_move("a5", "a7")
    # chess.make_move("f6", "e4")
    # chess.make_move("a7", "a8")
    # chess.make_move("e4", "d2")
    # chess.make_move("a8", "c8")
    # chess.enter_fairy_piece("f", "a7")
    # chess.make_move("c1", "d2")
    # chess.enter_fairy_piece("h", "a8")
    # chess.make_move("c8", "a8")
    # chess.get_board()
    # print(chess.get_turn())
    # print(chess.get_black_lost_pieces())
    # print(chess.get_white_lost_pieces())

    # TEST FOR HUNTER MOVEMENT / CAPTURE
    # chess.make_move("d2", "d4")
    # chess.make_move("f7", "f6")
    # chess.make_move("e1", "a5")
    # chess.make_move("e8", "h5")
    # chess.make_move("a5", "a7")
    # chess.make_move("h5", "h2")
    # chess.make_move("a7", "a8")
    # chess.make_move("h2", "h1")
    # chess.make_move("a8", "b8")
    # chess.enter_fairy_piece("h", "a7")
    # chess.enter_fairy_piece("H", "h2")
    # chess.make_move("a7", "a4")
    # chess.make_move("h2", "h7")
    # chess.make_move("a4", "a3")
    # chess.make_move("h7", "g6")
    # chess.make_move("f6", "f5")
    # chess.make_move("g6", "f5")
    # chess.make_move("a3", "d6")
    # chess.make_move("f5", "f8")
    # chess.make_move("b7", "b6")
    # chess.make_move("f8", "e7")
    # chess.get_board()
    # print(chess.get_turn())
    # print(chess.get_black_lost_pieces())
    # print(chess.get_white_lost_pieces())

    # TEST FOR FALCON MOVEMENT / CAPTURE AND SECOND CAPTURE
    # chess.make_move("d2", "d4")
    # chess.make_move("f7", "f6")
    # chess.make_move("e1", "a5")
    # chess.make_move("e8", "h5")
    # chess.make_move("a5", "a7")
    # chess.make_move("h5", "h2")
    # chess.make_move("a7", "a8")
    # chess.make_move("h2", "h1")
    # chess.make_move("a8", "b8")
    # chess.enter_fairy_piece("f", "a7")
    # chess.enter_fairy_piece("F", "h2")
    # chess.make_move("a7", "d4")
    # chess.make_move("g2", "g3")
    # chess.make_move("d4", "d6")
    # chess.make_move("h2", "h1")
    # chess.make_move("d6", "g3")
    # chess.get_board()
    # print(chess.get_turn())
    # print(chess.get_black_lost_pieces())
    # print(chess.get_white_lost_pieces())


if __name__ == "__main__":
    main()
