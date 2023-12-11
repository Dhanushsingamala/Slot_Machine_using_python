# Slot Machine Game

This is a simple console-based slot machine game implemented in Python. The game allows players to make bets, spin the slot machine, and win money based on the resulting symbols and lines.

## Features

- Dynamic slot machine with configurable symbols and frequencies.
- User-friendly CLI for depositing money, selecting lines, and placing bets.
- Calculates winnings based on the spin result and displays the outcome.

## How to Play

1. Run the `main.py` script using a Python interpreter.
2. Enter the initial deposit amount when prompted.
3. Follow the on-screen instructions to select the number of lines and place bets.
4. Press Enter to spin the slot machine.
5. View the outcome and check if you've won on any lines.
6. Repeat the process or type 'q' to quit the game.

## Configuration

You can customize the game by adjusting the constant variables, such as `MAX_LINES`, `MAX_BET`, `MIN_BET`, `ROWS`, `COLS`, `symbols_and_frequencies`, and `symbols_and_values` in the script.

'''python
# Example Configuration
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_and_frequencies = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbols_and_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
} '''
