class Vehicle:
    def __init__(self,s,c,w):
        self.speed = s
        self.crater_time = c
        self.drivable = w

    def can_drive(self,weather):
        return self.drivable[weather]
    
