import time
class Elevator:
    def __init__(self, name="1"):
        self.current_floor = 1
        self.name = name
    
    def getFloor(self):
        return self.current_floor
    
    def getName(self):
        return self.name

    def display_floor(self):
        print(f"current floor of the elevator {self.name}: {self.current_floor}")

    def move(self,current,floor):

        while self.current_floor!=current:
            if self.current_floor>current:
                self.display_floor()
                time.sleep(1)
                self.current_floor-=1
            else:
                self.display_floor()
                time.sleep(1)
                self.current_floor+=1

        while self.current_floor!=floor:
            if self.current_floor>floor:
                self.display_floor()
                time.sleep(1)
                self.current_floor-=1
            else:
                self.display_floor()
                time.sleep(1)
                self.current_floor+=1
            
        self.display_floor()
        