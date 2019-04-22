
class Squirmys:
    num_squirmys = 3
    def __init__(self):
        # create some member animals
        self.members = ['Worm', 'Snake', 'Lizard']
                
    def add_member(self, new_m):
        self.members.append(new_s)
        Squirmys.num_mammals += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Squirmys.num_mammals -= 1