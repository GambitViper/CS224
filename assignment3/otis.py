#
# CS 224 Spring 2019
# Programming Assignment 3
#
# Elevator optimization problem
#
# Author: Zachary Baklund
# Date: April 22, 2019
#
import sys
from time import sleep, time
from building import Building
from passenger import Passenger
from elevator import Elevator

def get_floors():
    floors_bool = False
    while(not floors_bool):
        try:
            num_floors = int(raw_input("Number of Floors? "))
            if num_floors >= 1:
                floors_bool = True
            else:
                print("INVALID -- Please enter an INTEGER >= 1")
        except ValueError:
            print("INVALID -- Please enter an INTEGER >= 1")
    return num_floors

def get_passengers(num_floors):
    passenger_bool = False
    while(not passenger_bool):
        try:
            num_passengers = int(raw_input("Number of Passengers? "))
            if num_passengers >= 1:
                passenger_bool = True
            else:
                print("INVALID -- Please enter an INTEGER >= 1")
        except ValueError:
            print("INVALID -- Please enter an INTEGER >= 1")
    passenger_list = []
    for i in range(num_passengers):
        passenger_list.append(Passenger(i, num_floors))
    return passenger_list

def check_patrons(passenger_list):
    for p in passenger_list:
        if p.done == False:
            return False
    return True

def find_passengers_on_floor(passenger_list, floor):
    passengers_on_floor = []
    for p in passenger_list:
        if p.src_floor == floor and not p.done and not p.in_elevator:
            passengers_on_floor.append(p)
    return passengers_on_floor

def board_passengers_to_elevator(passengers, elevator):
    for p in passengers:
        if p.direction == elevator.direction:
            elevator.passenger_enter(p)

def dispatch_passengers_to_floor(elevator):
    for p in elevator.register_list:
        if p.dest_floor == elevator.curr_floor:
            elevator.passenger_exit(p)

def change_direction_check(passenger_list, elevator, num_floors):
    if elevator.direction == "U" and not (elevator.curr_floor + 1) > num_floors:
        for p in passenger_list:
            if p.src_floor >= elevator.curr_floor and not p.in_elevator and not p.done:
                return "U"
        return "D" if not elevator.register_list else "U"
    elif elevator.direction == "D" and not (elevator.curr_floor - 1) < 1:
        for p in passenger_list:
            if p.src_floor <= elevator.curr_floor and not p.in_elevator and not p.done:
                return "D"
        return "U" if not elevator.register_list else "D"
    else:
        return elevator.direction


def main():
    start_time = time()
    moves = 0
    noout = True
    if (len(sys.argv) > 1 and sys.argv[1] == "fast") or (len(sys.argv) > 2 and sys.argv[2] == "fast"):
        noout = False
        
    num_floors = get_floors()
    passenger_list = get_passengers(num_floors)
    elevator = Elevator(num_floors)

    b = Building(num_floors, passenger_list, elevator)

    if noout:
        b.output()

    elevator_complete = False
    while(not elevator_complete):
        if noout:
            sleep(.25)
        passengers_on_floor = find_passengers_on_floor(passenger_list, elevator.curr_floor)
        board_passengers_to_elevator(passengers_on_floor, elevator)
        dispatch_passengers_to_floor(elevator)
        if len(sys.argv) > 1 and sys.argv[1] == "mine":
            elevator.direction = change_direction_check(passenger_list, elevator, num_floors)
        b.run()
        if noout:
            b.output()
        moves += 1
        elevator_complete = check_patrons(passenger_list)
    print("{} moves in {} seconds".format(moves, time() - start_time))

if __name__ == "__main__":
    main()

