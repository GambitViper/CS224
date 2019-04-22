from random import randrange

class Elevator(object):

    # num_floors    -- Number of floors in the building
    # register_list -- List of customers in the elevator
    # curr_floor    -- Current floor the elevator is on
    # direction     -- Direction of travel

    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.register_list = list()
        self.curr_floor = randrange(1,num_floors)
        self.direction = "U"

    # move(self) Method to move the elevator one floor
    def move(self):
        if self.direction == "U" and not (self.curr_floor + 1) > num_floors:
            self.curr_floor += 1
        elif self.direction == "D" and not (self.curr_floor - 1) < 1:
            self.curr_floor -= 1
        else:
            print("Error elevator has left the building!")
    
    # reg pass(self, passenger) Passenger enters elevator
    def passenger_enter(self, passenger):
        self.register_list.append(passenger.pid)

    # exit pass(self, passenger) Passenger exits elevator
    def passenger_exit(self, passenger):
        self.register_list.remove(passenger.pid)
