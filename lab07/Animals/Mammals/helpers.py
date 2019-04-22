
def print_members(mammals):
    print('Mammal list:')
    for m in mammals.members:
        print('  {}'.format(m))

def sort_members(mammals):
    mammals.members.sort()
    