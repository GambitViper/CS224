# CS 224 Spring 2019 - Programming Assignment 1

This program performs simple analysis of a data element across a
large number of data files representing runs of a traveling salesman
algorithm.

## Running the program

Each runbest file contains a single line. Reading that line gives you a string.
From that string, you must access the minimum distance, which is preceded by F.

Here is an example line from one of the files:

```
G 1265 I 5091 L 55 F 79666.000 -1.000 ( 0, 7935) 5 4 18 50 47 15 32 12 11 10 36 35 51 1 40 41 42 16 7 34 9 8 33 20 26 0 28 27 29 30 38 17 37 31 24 21 25 39 49 3 48 2 13 6 54 19 52 53 23 22 43 46 45 44 14
```

In this example line, the value of interest is 79666.0. The rest of the line is not relevant
for this assignment.

## Author

* Author: **Zachary Baklund**
* Date: February 18, 2019
