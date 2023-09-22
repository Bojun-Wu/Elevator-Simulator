from Elevator_system import ElevatorSystem
import os

if __name__ == '__main__':
    ele = ElevatorSystem()
    rideAgain = True
    while rideAgain!="No":
        os.system('clear')
        ele.move()
        print("____________________Arrive!!!____________________")
        rideAgain = input("Do you want to ride again(Yes or No): ")
        print("_________________________________________________")