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

def get_guess():
    # returns a valid game pattern, indicating the user's guess.
    not_valid = True
    guess_pattern = []

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
    mutable_pattern = deepcopy(correct_pattern)
    correctness = []
    for i in range(len(correct_pattern)):
        if guess_pattern[i] == correct_pattern[i] and guess_pattern[i] in mutable_pattern:
            correctness.append('b')
        elif guess_pattern[i] in mutable_pattern:
            mutable_pattern.remove(guess_pattern[i])
            correctness.append('w')
    return correctness

def pre_print(arr):
    preprint = ""
    for a in arr:
        preprint = preprint + " " + a
    preprint = preprint + " "
    return preprint

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
    print("Start by guessing from these colors:\n{0}\n".format(colors))
    count = 0
    won = False
    while count < 10 or not won:
        guess_pattern = get_guess()
        pegs = evaluate_guess(guess_pattern, correct_pattern)
        addtoboard = []
        addtoboard.append(guess_pattern)
        addtoboard.append(pegs)
        print("Debug: cor> {}\nDebug: {} + {}:\n{}".format(correct_pattern, guess_pattern, pegs, addtoboard))
        board.append(addtoboard)
        print_board(board)

def main():
    begin_game()

if __name__ == '__main__':
    main()