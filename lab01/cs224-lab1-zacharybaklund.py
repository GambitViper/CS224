#
# CS 224 Spring 2019
# Lab Assignment 1
#
# Counts the number of times each character is mentioned
# in the text of the plays
#
# Author: Zachary Baklund
# Date: February 13, 2019
#

from os import listdir
import re

fn0 = open('characters.txt', 'r')
lines0 = fn0.readlines()
characters = []
fn0.close()
for line in lines0:
    character = line.strip("\n")
    characters.append(character)
counts = [0]*len(characters)
fn1 = open('shakespeare.txt', 'r')
lines1 = fn1.readlines()
fn1.close()
for line in lines1:
    for char in characters:
        counts[characters.index(char)] += line.count(char)
for char in characters:
    print("{:<12s} :   {:>3d}".format(char, counts[characters.index(char)]))
