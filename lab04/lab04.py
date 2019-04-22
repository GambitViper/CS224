#
# CS 224 Spring 2019
# Lab Assignment 4
#
# grep
#
# Author: Zachary Baklund
# Date: March 13, 2019
#

from os import listdir

def grep(lookup):
    # your code goes here
    results = []

    fn = listdir('datafiles')
    for textfile in fn:
        fsub = open("datafiles/" + textfile, 'r')
        flines = fsub.read().splitlines()
        for i, line in enumerate(flines):
            if line.upper().count(lookup.upper()) > 0:
                results.append("{}: {}: {}".format(textfile, i, line))
    
    return results

def main():
    # call grep from here
    grepfor = raw_input("grep -n : ")
    results = grep(grepfor)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()


