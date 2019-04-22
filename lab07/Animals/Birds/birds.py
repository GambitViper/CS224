class Birds:
    num_birds = 3
    def __init__(self):
        # create some member animals
        self.members = ['Eagle', 'Blue Hen', 'Penguin']
                
    def add_member(self, new_b):
        self.members.append(new_b)
        Birds.num_birds += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Birds.num_birds -= 1