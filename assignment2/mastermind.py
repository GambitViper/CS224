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

def minMax(computer_patterns, all_possible_patterns):
    # Apply minimax technique to find a next guess as follows: For each possible guess, that is, 
    # any unused code of the 1296 not just those in S, calculate how many possibilities in S would be eliminated 
    # for each possible colored/white peg score. The score of a guess is the minimum number of possibilities 
    # it might eliminate from S. A single pass through S for each unused code of the 1296 will provide a hit count 
    # for each colored/white peg score found; the colored/white peg score with the highest hit count will 
    # eliminate the fewest possibilities; calculate the score of a guess by 
    # using "minimum eliminated" = "count of elements in S" - (minus) "highest hit count". 
    # From the set of guesses with the maximum score, select one as the next guess, 
    # choosing a member of S whenever possible.
    peg_outcomes = [[],['w'],['w','w'],['w','w','w'],['w','w','w','w'],
                    ['b'],['b','w'],['b','w','w'],['b','w','w','w'],
                    ['b','b'],['b','b','w'],['b','b','w','w'],
                    ['b','b','b'],['b','b','b','b']]
    cpumin = maxint
    best_pattern = None
    for guess in computer_patterns:
        cpumax = 0
        for pegs in peg_outcomes:
            count = 0
            for cpusolution in all_possible_patterns:
                if evaluate_guess(guess, cpusolution) == pegs:
                    count += 1
            if count > cpumax:
                cpumax = count
        if cpumax < cpumin:
            cpumin = cpumax
            best_pattern = guess
    return best_pattern

def computer_guess(computer_patterns, all_possible_patterns):
    if len(computer_patterns) == 1296:
        return computer_patterns.pop(computer_patterns.index(['B','B','W','W']))
    else:
        return minMax(computer_patterns, all_possible_patterns)
        # selection = choice(computer_patterns)
        # return computer_patterns.pop(computer_patterns.index(selection))

def cull_patterns(computer_patterns, pegs, previous_guess):
    for pattern in computer_patterns:
        if evaluate_guess(previous_guess, pattern) != pegs:
            computer_patterns.remove(pattern)

def begin_game(cpu = False):
    print("Welcome to MasterMind!\n")
    board = []
    correct_pattern = create_new_game()
    if cpu:
        all_possible_patterns = init_patterns()
        computer_guesses = init_patterns()
        previous_guess = []
    print("Start by guessing from these colors:")
    count = 0
    won = False
    while not won:
        guess_pattern = []
        if cpu:
            guess_pattern = computer_guess(computer_guesses, all_possible_patterns)
            previous_guess = guess_pattern
        else:
            guess_pattern = get_guess()
        pegs = evaluate_guess(guess_pattern, correct_pattern)
        if cpu:
            cull_patterns(computer_guesses, pegs, previous_guess)
        addtoboard = []
        addtoboard.append(guess_pattern)
        addtoboard.append(pegs)
        # print("Debug: cor> {}\nDebug: {} + {}:\n{}".format(correct_pattern, guess_pattern, pegs, addtoboard))
        board.append(addtoboard)
        print_board(board)
        if guess_pattern == correct_pattern:
            won = True
            print("!-- You Won --!")

def main():
    begin_game(True)

if __name__ == '__main__':
    main()