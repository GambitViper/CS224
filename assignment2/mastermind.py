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
from random import randrange

colors = ['B', 'W', 'R', 'G', 'P', 'O']
board = []
correct_pattern = []

def create_new_game():
    # returns a valid game pattern.
    return [colors[randrange(0,len(colors))] for r in range(len(colors))]

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


def evaluate_guess(guess_pattern):
    # returns a sequence of pegs indicating correctness of the guess.
    correctness = []
    for i in range(len(correct_pattern)):
        if guess_pattern[i] in correct_pattern:
            if guess_pattern[i] == correct_pattern[i]:
                correctness.append('b')
            else:
                correctness.append('w')
    return correctness


def print_board(game_board):
    # prints the board display
    print "notimplemented"

def begin_game():
    print("Welcome to MasterMind!\n")
    correct_pattern = create_new_game()
    print("Start by guessing from these colors:\n{0}\n".format(colors))
    guess_pattern = get_guess()
    print("Your guess was: {0}".format(guess_pattern))
    pegs = evaluate_guess(guess_pattern)
    board.append()

begin_game()