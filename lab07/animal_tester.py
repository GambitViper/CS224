import Animals

m = Animals.Mammals.mammals.Mammals()
f = Animals.Fish.fish.Fish()
b = Animals.Birds.birds.Birds()
s = Animals.SquirmyThings.squirmys.Squirmys()

def print_animals():
    Animals.Mammals.helpers.print_members(m)
    Animals.Fish.helpers.print_members(f)
    Animals.Birds.helpers.print_members(b)
    Animals.SquirmyThings.helpers.print_members(s)

def print_animals_count():
    print(str(m.num_mammals) + ": Mammals")
    Animals.Mammals.helpers.print_members(m)
    print(str(f.num_fish) + ": Fish")
    Animals.Fish.helpers.print_members(f)
    print(str(b.num_birds) + ": Birds")
    Animals.Birds.helpers.print_members(b)
    print(str(s.num_squirmys) + ": Squirmys")
    Animals.SquirmyThings.helpers.print_members(s)

def main():
    Animals.Fish.helpers.print_members(f)
    print("++Gorilla -> Fish")
    f.add_member("Gorilla")
    Animals.Fish.helpers.print_members(f)

    Animals.Birds.helpers.print_members(b)
    print("--Blue Hen <- Birds")
    b.delete_member("Blue Hen")
    Animals.Birds.helpers.print_members(b)

if __name__ == "__main__":
    main()