import random

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
}

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
            winning_lines.append(line+1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
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


def print_slot_machine(columns):
    #transposing a matrix and printing the values 
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if  i!=len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()    



def deposit():
    while True:
        amount = input("what would You like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a valid number Greater than 0")

    return amount



def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}) ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"please enter num of lines in given Range")
        else:
            print(f"please enter valid input")
    return lines


def get_bet():
    while True:
        amount = input("what would You like to bet? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}₹ and {MAX_BET}₹.")
        else:
            print("please enter a valid number Greater than 0")

    return amount


def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you don't have enough money to bet , your current balance is {balance}")
        else:
            break
    print(f"you are betting ₹{bet} on {lines} lines. Total bet is equal to ₹{total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_and_frequencies
                                  )
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_and_values)
    print(f"you won ₹{winnings}.") 
    if winnings:
        print(f"you won on lines: ",*winning_lines)
    else:
        print("you lost , Try again !")

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ₹{balance}")
        answer = input("press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)    

    print(f"you left with ₹{balance} ")

main()