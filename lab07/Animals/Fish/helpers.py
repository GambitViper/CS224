
def print_members(fish):
    print('Fish list:')
    for f in fish.members:
        print('  {}'.format(f))

def sort_members(fish):
    fish.members.sort()