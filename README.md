Overview
The ChessVar class provides a basic implementation of a chess game. It supports essential functionalities for managing the chessboard, tracking game state, and handling player turns. The class is designed to offer a foundation for implementing chess logic and can be extended with additional features such as legal piece movement and capturing.

The class also introduces "fairy pieces"—custom non-standard pieces—that players can bring into the game under certain conditions.

Features
Chessboard Initialization: Automatically sets up an 8x8 chessboard with standard pieces.
Turn Management: Tracks and switches turns between the white and black players.
Game State Tracking: Monitors the state of the game, determining when a player has won.
Fairy Pieces: Special pieces that can be introduced into the game after certain conditions are met.

Chess Board Representation
The chessboard is an 8x8 grid, with standard Unicode chess symbols representing each piece.
The board is initialized with the following:
White pieces are represented by ♔, ♕, ♖, ♗, ♘, ♙, and custom fairy pieces F and H.
Black pieces are represented by ♚, ♛, ♜, ♝, ♞, ♟︎, and fairy pieces f and h.