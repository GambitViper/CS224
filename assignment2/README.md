# CS 224 Spring 2019 - Programming Assignment 1

For this assignment, you will write a Python version of the Mastermind game. Mastermind is a two-player logic game and what passed for fun before the internet existed.

## Running the program

```
python mastermind.py debug cpu
```
* (debug) is an optional command-line argument -- When present this turns on a debug print that shows the correct pattern and intermediary memory allocation for the guess and the pegs associated with that guess according to the secret pattern
* (cpu) is an optional command-line argument -- When present this optional argument invokes the function definitions that solve the mastermind problem stochastically by removing possible patterns from a total patterns list and then picking randomly from the remaining possibilities
* Ordering of these arguments does not matter ie. `python mastermind.py debug cpu` is just the same as `python mastermind.py cpu debug` you can also invoke each mode stand alone such as: `python mastermind.py cpu` or `python mastermind.py debug`

## Author

* Author: **Zachary Baklund**
* Date: March 4, 2019
