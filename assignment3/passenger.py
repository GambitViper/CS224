from random import randrange, choice

class Passenger(object):

    # pid         -- Passenger's ID
    # src_floor   -- Passemger's starting floor
    # dest_floor  -- Passenger's destination floor
    # direction   -- Passenger's direction of travel
    # in_elevator -- Indicates if passenger is in elevator
    # done        -- Indicates if passenger arrived and exited

    def __init__(self, passenger_id, num_floors):
        self.pid = passenger_id
        self.src_floor = randrange(1,num_floors)
        self.dest_floor = self.find_dest(self.src_floor, num_floors)
        self.direction = "U" if randrange(0,1) == 0 else "D"
        self.in_elevator = False
        self.done = False

    def find_dest(self, src_floor, num_floors):
        floors = range(1,num_floors + 1)
        floors.remove(src_floor)
        self.dest_floor = choice(floors)
