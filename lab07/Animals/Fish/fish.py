class Fish:
    num_fish = 3
    def __init__(self):
        #create some member animals
        self.members = ['Pike', 'Walleye', 'Muskee']
    
    def add_member(self, new_f):
        self.members.append(new_f)
        Fish.num_fish += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Fish.num_fish -= 1