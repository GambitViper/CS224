
def foo(fn):
    str_list = fn.splitlines()
    print str_list
    for line in str_list:
        print "-line[:3] {}".format(line[:3])
        print "-line[:2] {}".format(line[:2])
        print "-line[-2:] {}".format(line[-2:])
        print "-line.count('z') {}".format(line.count('z'))
        if line[:3] == 'The' or line[:2] == 'do' or line[-2:] == 'da' or line.count('z') > 0:
            print line
            str_list.pop(str_list.index(line))
            print str_list
        else:
            substrings = line.split('tt')
            for substring in substrings:
                print substring

def main():
    file1 = 'Thisttisttattstring\nThettstringttstartsttwithttThe\ndottstartsttwithttdo\ndadttendttwithttda\nKeepttme!\nzzzzzzzz\nsomettmorettzzzzs\n'

    foo(file1)

if __name__ == '__main__':
    main()