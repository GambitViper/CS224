# 
# CS 224 Spring 2019 
# Programming Assignment 2 
# 
# For this assignment, you will write a Python version of the Mastermind game. 
# Mastermind is a two-player logic game and what passed for fun before the internet existed.
# 
# Author: Zachary Baklund 
# Date: March 13, 2019 
#
from sys import maxint
from copy import deepcopy
from random import randrange, choice

colors = ['B', 'W', 'R', 'G', 'P', 'O']

def create_new_game():
    # returns a valid game pattern.
    return [colors[randrange(0,len(colors))] for _ in range(4)]

def check_valid(inp):
    for c in colors:
        if c == inp:
            return False
    return True

def board_format(arr):
    bformat = ""
    for a in arr:
        bformat += " " + a
    bformat += " "
    return bformat

def get_guess():
    # returns a valid game pattern, indicating the user's guess.
    not_valid = True
    guess_pattern = []
    print("Colors :> {}".format(board_format(colors)))
    for i in range(4):
        inp = 0
        while not_valid:
            inp = raw_input("Enter peg {0}: ".format(i + 1))
            not_valid = check_valid(inp)
            if not_valid:
                print("Invalid peg - guess again")
        not_valid = True
        guess_pattern.append(inp)

    return guess_pattern


def evaluate_guess(guess_pattern, correct_pattern):
    # returns a sequence of pegs indicating correctness of the guess.
    remaining_pattern = []
    remaining_guess = []
    correctness = []

    # Check for correct color and correct place
    for i, guess in enumerate(guess_pattern):
        if guess == correct_pattern[i]:
            correctness.append('b')
        else:
            remaining_guess.append(guess)
            remaining_pattern.append(correct_pattern[i])

    # Check for correct color incorrect place
    for guess in remaining_guess:
        if guess in remaining_pattern:
            correctness.append('w')
            remaining_pattern.remove(guess)

    return correctness

def print_board(game_board):
    # prints the board display
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
    for turn in game_board:
        print("|{:<8s} : {:^10s}|".format(
            board_format(turn[0]), board_format(turn[1])
        ))
    print("~~~~~~~~~~~~~~~~~~~~~~~~\n")

def init_patterns():
    return [[colors[a], colors[b], colors[c], colors[d]]
            for a in range(6) for b in range(6) for c in range(6) for d in range(6)]

def computer_guess(computer_patterns):
    if len(computer_patterns) == 1296:
        return computer_patterns.pop(computer_patterns.index(['B','B','W','W']))
    else:
        selection = choice(computer_patterns)
        return computer_patterns.pop(computer_patterns.index(selection))

def begin_game(cpu = False):
    print("Welcome to MasterMind!\n")

    board = []
    correct_pattern = create_new_game()
    if cpu:
        computer_guesses = init_patterns()
        previous_guess = []

    print("Start by guessing from these colors:")

    count = 0
    won = False
    while not won:
        guess_pattern = []

        if cpu:
            guess_pattern = computer_guess(computer_guesses)
            previous_guess = guess_pattern
        else:
            guess_pattern = get_guess()

        pegs = evaluate_guess(guess_pattern, correct_pattern)

        if cpu:
            computer_guesses = filter(lambda g: evaluate_guess(previous_guess, g) == pegs, computer_guesses)
            
        addtoboard = []
        addtoboard.append(guess_pattern)
        addtoboard.append(pegs)
        # print("Debug: cor> {}\nDebug: {} + {}:\n{}".format(correct_pattern, guess_pattern, pegs, addtoboard))
        board.append(addtoboard)
        print_board(board)

        if guess_pattern == correct_pattern:
            won = True
            print("!-- You Won --!")
        elif cpu:
            print("...> I think there are {} possibilities left".format(len(computer_guesses)))

def main():
    begin_game(True)

if __name__ == '__main__':
    main()