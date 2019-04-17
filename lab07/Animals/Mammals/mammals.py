
class Mammals:
    num_mammals = 3
    def __init__(self):
        # create some member animals
        self.members = ['Lion', 'Tiger', 'Bear']
                
    def add_member(self, new_m):
        self.members.append(new_m)
        Mammals.num_mammals += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Mammals.num_mammals -= 1
            