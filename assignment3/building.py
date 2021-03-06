

class Building(object):

    # num_floors     -- Number of floors in the building
    # passenger_list -- List of passengers
    # elevator       -- The building's elevator (object)

    def __init__(self, num_floors, passenger_list, elevator):
        self.num_floors = num_floors
        self.passenger_list = passenger_list
        self.elevator = elevator

    # run(self)    -- Method that operates the elevator
    def run(self):
        self.elevator.move()
    # output(self) -- Prints the building
    def output(self):
        print("------------------------------------------------------------")
        print("{:^20s}{:^20s}{:^20s}".format("Floor", "Customer", "Elevator"))
        print("------------------------------------------------------------")
        for i in range(self.num_floors, 0, -1):
            present_passengers = self.passengers_on_floor(i)
            print("   {:<20d}{:^20s}{:>20s}".format(i, self.preproc(present_passengers), "X   " if self.elevator.curr_floor == i else " "))
            print("------------------------------------------------------------")

    def passengers_on_floor(self, floor):
        return [str(i.pid) + str(i.direction) for i in self.passenger_list if i.src_floor == floor and not i.done]

    def preproc(self, passenger_list):
        str_passengers = ""
        for p in passenger_list:
            str_passengers += "{} ".format(p)
        return str_passengers