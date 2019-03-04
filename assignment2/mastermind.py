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
from copy import deepcopy
from random import randrange

colors = ['B', 'W', 'R', 'G', 'P', 'O']
board = []
correct_pattern = []

def create_new_game():
    # returns a valid game pattern.
    return [colors[randrange(0,len(colors))] for r in range(4)]

def check_valid(inp):
    for c in colors:
        if c == inp:
            return False
    return True

def pre_print(arr):
    preprint = ""
    for a in arr:
        preprint = preprint + " " + a
    preprint = preprint + " "
    return preprint

def get_guess():
    # returns a valid game pattern, indicating the user's guess.
    not_valid = True
    guess_pattern = []
    print(pre_print(colors))
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
            pre_print(turn[0]), pre_print(turn[1])
        ))
    print("~~~~~~~~~~~~~~~~~~~~~~~~\n")

def begin_game():
    print("Welcome to MasterMind!\n")
    correct_pattern = create_new_game()
    print("Start by guessing from these colors:")
    count = 0
    won = False
    while count < 7 and not won:
        guess_pattern = get_guess()
        pegs = evaluate_guess(guess_pattern, correct_pattern)
        addtoboard = []
        addtoboard.append(guess_pattern)
        addtoboard.append(pegs)
        print("Debug: cor> {}\nDebug: {} + {}:\n{}".format(correct_pattern, guess_pattern, pegs, addtoboard))
        board.append(addtoboard)
        print_board(board)
        if guess_pattern == correct_pattern:
            won = True
            print("!-- You Won --!")

def main():
    begin_game()

if __name__ == '__main__':
    main()