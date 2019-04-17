from random import randint
from random import shuffle
from sys import exit

class Mastermind(object):

    def __init__(self, debug):
        self.debug = debug
        self.colors = ['B', 'W', 'R', 'G', 'P', 'O']
        self.board = [[[self.colors[c] for c in [randint(0, 5) for _ in range(0, 4)]]], [['T', 'A', 'R', 'G']]]
	    # First column = Guesses, Second Column = Pegs; First Row is target.
	    # Get color counts for proper peg calculations
        self.ccts = [0] * len(self.colors)
        for i in range(0, len(self.board[0][0])):
            self.ccts[self.colors.index(self.board[0][0][i])] += 1

    def get_guess(self):
        print('Potential guesses: {}'.format(' '.join(self.colors)))
        guess = [0] * 4
        for i in range(0, 4):
            # While guess is invalid, get new guess
            while guess[i] not in self.colors:
                guess[i] = raw_input('Please enter a valid guess number {}: '.format(i + 1)).upper()
                # User types q or Q to quit
                if guess[i] == 'Q':
                    exit('Thanks for playing!')
        return guess

    def evaluate_guess(self, guess, target):
        gcts = [0] * len(self.colors)
        pegs = ['-'] * len(guess)
        # Get black pegs first because of white peg problem
        for i in range(0, len(guess)):
            if guess[i] == target[i]:
                pegs[i] = 'b'
                gcts[self.colors.index(guess[i])] += 1
        # Get white pegs depending on black pegs and identified color count
        for i in range(0, len(target)):
            if pegs[i] != 'b' and gcts[self.colors.index(guess[i])] != self.ccts[self.colors.index(guess[i])]:
                for j in range(len(target)):
                    if guess[i] == target[j]:
                        pegs[i] = 'w'
                        break
        shuffle(pegs)
        return pegs

    def print_board(self, board):
        n = 1
        if self.debug:   # Index to target for printing
            print('DEBUG MODE. FIRST ROW IS TARGET PATTERN.')
            n = 0
        print('---------------------')
        for i in range(n, len(board[0])):
            print('| {} | {} |'.format(' '.join(board[0][i]), ' '.join(board[1][i])))
        print('---------------------')

    def play_game(self):
        print("Welcome to Mastermind! Try to guess the pattern of colors!")
        print("The pegs to the right of your guess convey its quality, and are displayed in a random order.")
        guess = self.get_guess()         # Get first guess
        count = 1                   # Initialize count
        while guess != self.board[0][0]:
            self.board[0].append(guess)  # Append guess and evaluated guess
            self.board[1].append(self.evaluate_guess(guess, self.board[0][0]))
            self.print_board(self.board)      # Print

            guess = self.get_guess()     # Next guess and increment count
            count += 1
        print("You guessed the correct pattern in {} guesses! : {}".format(count, ' '.join(self.board[0][0])))

def main():
    m = Mastermind(False)
    m.play_game()

if __name__ == "__main__":
    main()