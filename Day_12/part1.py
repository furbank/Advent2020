with open("Day_12\input") as f:
    data = f.read().splitlines()

class Boat:

    def __init__(self, startNorth, startEast, heading):
        self.heading = heading
        self.startNorth = startNorth
        self.startEast = startEast
        self.posNorth = startNorth
        self.posEast = startEast

    def Move(self, instruction):
# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the
        pass

    def TurnLeft(self, amount):
        self.heading = (self.heading - amount) % 360

    def TurnRight(self, amount):
        self.heading = (self.heading + amount) % 360

    def MoveNorth(self, distance):
        self.posNorth += distance

    def MoveSouth(self, distance):
        self.posNorth -= distance

    def MoveEast(self, distance):
        self.posEast += distance

    def MoveWest(self, distance):
        self.posEast -= distance

    def MoveForward(self, distance):
        pass

    def MoveBackward(self, distance):
        pass

    def ManhattanDistance(self):
        return abs(self.posNorth) + abs(self.posEast)


