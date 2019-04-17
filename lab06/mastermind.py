#
# 
# Author: Connor Ludwigson
# Date: March 13, 2019
#

from random import randint
from random import shuffle
from sys import exit

debug = False                               ## SET TRUE TO REVEAL TARGET
colors = ['B', 'W', 'R', 'G', 'P', 'O']     ## Global color list for valid colors
ccts = []                                   ## Global parallel color counts list


def main():
	board = create_new_game()   # Create game
	print("Welcome to Mastermind! Try to guess the pattern of colors!")
	print("The pegs to the right of your guess convey its quality, and are displayed in a random order.")
	guess = get_guess()         # Get first guess
	count = 1                   # Initialize count
	while guess != board[0][0]:
		board[0].append(guess)  # Append guess and evaluated guess
		board[1].append(evaluate_guess(guess, board[0][0]))
		print_board(board)      # Print

		guess = get_guess()     # Next guess and increment count
		count += 1
	print("You guessed the correct pattern in {} guesses! : {}".format(count, ' '.join(board[0][0])))

# Sets up the game
def create_new_game():
	global ccts
	board = [[[colors[c] for c in [randint(0, 5) for _ in range(0, 4)]]], [['T', 'A', 'R', 'G']]]
	# First column = Guesses, Second Column = Pegs; First Row is target.
	# Get color counts for proper peg calculations
	ccts = [0] * len(colors)
	for i in range(0, len(board[0][0])):
		ccts[colors.index(board[0][0][i])] += 1
	return board

# Gets a guess pattern from the user
def get_guess():
	print('Potential guesses: {}'.format(' '.join(colors)))
	guess = [0] * 4
	for i in range(0, 4):
		# While guess is invalid, get new guess
		while guess[i] not in colors:
			guess[i] = raw_input('Please enter a valid guess number {}: '.format(i + 1)).upper()
			# User types q or Q to quit
			if guess[i] == 'Q':
				exit('Thanks for playing!')
	return guess

# Evaluates the user's guess
def evaluate_guess(guess, target):
	gcts = [0] * len(colors)
	pegs = ['-'] * len(guess)
	# Get black pegs first because of white peg problem
	for i in range(0, len(guess)):
		if guess[i] == target[i]:
			pegs[i] = 'b'
			gcts[colors.index(guess[i])] += 1
	# Get white pegs depending on black pegs and identified color count
	for i in range(0, len(target)):
		if pegs[i] != 'b' and gcts[colors.index(guess[i])] != ccts[colors.index(guess[i])]:
			for j in range(len(target)):
				if guess[i] == target[j]:
					pegs[i] = 'w'
					break
	shuffle(pegs)
	return pegs

# Prints the game board in a simple concise manner
def print_board(board):
	n = 1
	if debug:   # Index to target for printing
		print('DEBUG MODE. FIRST ROW IS TARGET PATTERN.')
		n = 0
	print('---------------------')
	for i in range(n, len(board[0])):
		print('| {} | {} |'.format(' '.join(board[0][i]), ' '.join(board[1][i])))
	print('---------------------')


if __name__ == '__main__':
	main()