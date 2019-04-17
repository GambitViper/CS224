
def print_members(birds):
    print('Bird list:')
    for b in birds.members:
        print('  {}'.format(b))

def sort_members(birds):
    birds.members.sort()
    