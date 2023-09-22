from Elevator import Elevator

class ElevatorSystem:
    def __init__(self):
        self.ele1 = Elevator("1")
        self.ele2 = Elevator("2")
    
    def move(self):
        self.ele1.display_floor()
        self.ele2.display_floor()
        print("_________________________________________________")

        currentFloor = input("Enter your current floor(integer): ")
        desireFloor = input("Enter your desired floor(integer): ")
        while not currentFloor.isdigit() or not desireFloor.isdigit():
            print("please enter a valid number")
            currentFloor = input("Enter your current floor(integer): ")
            desireFloor = input("Enter your desired floor(integer): ")
        currentFloor = int(currentFloor)
        desireFloor = int(desireFloor)

        print("_________________________________________________")
        useEle = self.ele1 if abs(self.ele1.getFloor()-currentFloor) <= abs(self.ele2.getFloor()-currentFloor) else self.ele2
        print(f"use elevator {useEle.getName()}")
        print("_________________________________________________")
        useEle.move(currentFloor, desireFloor)