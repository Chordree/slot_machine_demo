import random
ROWS = 3
COLS = 3

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

symbol_dict = {'A': 2,
               'B': 4,
               'C': 6,
               'D': 8
               }

win_value_multiplyer = {'A': 5,
                        'B': 4,
                        'C': 3,
                        'D': 2
                        }

def check_winnings(cols, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = cols[0][line]
        for col in cols:
            check = col[line]
            if symbol != check:        # try reversing this if condition and see what happens
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_spin(a, b, c):
    all_symbols = []
    for k, v in symbol_dict.items():
        for _ in range(v):
            all_symbols.append(k)
    columns = []
    for _ in range(b):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(a):
            display = random.choice(current_symbol)
            current_symbol.remove(display)
            column.append(display)
        columns.append(column)
    return columns

# this function below transposes the results and prints them in lines
def display_draws(para):
    for e in range(len(para[0])):
        for i, cl in enumerate(para):
            if i != len(para) - 1:
                print(cl[e] + ' | ',end='') # check if this does the transposition accurately
            else:
                print(cl[e])



def deposit():
    while True:
        amount = input('enter amount to deposit: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 5:
                break
            else:
                print('amount must be greater than $5')
        else:
            print('pls enter a valid amount')

    return amount

def get_lines():
    while True:
        lines = input('enter number of lines to stake on: ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('enter a number btw (1-'+str(MAX_LINES)+')')
                # print(f'enter a num btw (1 - {MAX_LINES})') this can also execute the code above
        else:
            print('pls enter a number')
    return lines

def stake():
    while True:
        bet = input('enter amount to bet on each line: $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'amount must be between  ${MIN_BET} - ${MAX_BET} ')
        else:
            print('pls enter a valid amount to bet ')

    return bet

def game_on(balance):
    accumulator = get_lines()

    while True:
        use = stake()
        total_bet = use * accumulator
        if total_bet > balance:
            print(f'you do not have enough money to place this total bet of ${total_bet} ')
            print(f'your bal is ${balance} ')
        else:
            # print(f'you are betting ${use} on {accumulator} lines \nTotal bet is ${total_bet}')
            break
    print(f'you are betting ${use} on {accumulator} lines \nTotal bet is ${total_bet}')
    print('bet placed successfully')

    slot = get_slot_spin(ROWS, COLS, symbol_dict)
    print(slot)  # try printing this matrix with line on its own ..i.e print it not as a list
    display_draws(slot)  # this just transposes the slot results and prints the lines
    winns, win_lines = check_winnings(slot, accumulator, use, win_value_multiplyer)
    print(f'you won ${winns}')
    print(f'you won on', *win_lines)
    return winns - total_bet


def main():
    balance = deposit()
    balance += game_on(balance)
    while True:
        print(f'your current balance is {balance}')
        play_on = input('enter any key to play again or enter "q" to quit: ')
        if play_on == 'q':
            break
        balance += game_on(balance)

    print(f'you left with {balance}')

# TODO: going back to reduce number of lines if total bet is less than balance but lower than minimum bet


main()

