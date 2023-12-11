import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Define the frequency of appearance for each symbol
symbols_and_frequencies = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

# Define the corresponding Multiplier values for each symbol
symbols_and_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}

# Function to check winnings based on the spin result
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        Symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if Symbol != symbol_to_check:
                break
        else:
            winnings += values[Symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

# Function to start a slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function to print the slot machine result
def print_slot_machine(columns):
    # Transposing a matrix and printing the values (columns <-->rows)
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()

# Function to get the initial deposit amount
def deposit():
    while True:
        amount = input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number greater than 0")

    return amount

# Function to get the number of lines to bet on
def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}) ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter the number of lines in the given range")
        else:
            print(f"Please enter a valid input")
    return lines

# Function to get the bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}₹ and {MAX_BET}₹.")
        else:
            print("Please enter a valid number greater than 0")

    return amount

# Function to perform a spin and calculate winnings
def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to bet, your current balance is {balance}")
        else:
            break
    print(f"You are betting ₹{bet} on {lines} lines. Total bet is equal to ₹{total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_and_frequencies)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_and_values)
    print(f"You won ₹{winnings}.") 
    if winnings:
        print("You won on lines:", *winning_lines)
    else:
        print("You lost, try again!")

    return winnings - total_bet

# Main function to run the slot machine game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        answer = input("Press Enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)    

    print(f"You left with ₹{balance} ")

main()
