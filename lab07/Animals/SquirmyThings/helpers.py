
def print_members(squirmys):
    print('Squirmy list:')
    for s in squirmys.members:
        print('  {}'.format(s))

def sort_members(squirmys):
    squirmys.members.sort()
    