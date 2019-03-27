from mountain import Mountain

def make_mountain(data):
    return Mountain(data[0], int(data[1]), int(data[2]), 
                    tuple(data[3].split(':')), tuple(data[4].split(':')), False)

def main():
    fn = open("mountains.txt", "r")
    inp = fn.read().splitlines()
    swiss_mountains = [make_mountain(d.split()) for d in inp]
    for m in swiss_mountains:
        print m

    print "Sort by height:"
    height_sorted = sorted(swiss_mountains, key=lambda x: x.elevation, reverse = True)
    for hm in height_sorted:
        print "{:>16s} : {:<15d}".format(hm.name, hm.elevation)

if __name__ == '__main__':
    main()