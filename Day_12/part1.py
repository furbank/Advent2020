# This seemed like a good puzzle to create a class for and work with objects
with open("Day_12\input") as f:
    data = f.read().splitlines()

#data = ['F10', 'N3', 'F7', 'R90', 'F11']

class Boat:

    def __init__(self, startNorth, startEast, heading):
        self.heading = int(heading)
        self.startNorth = int(startNorth)
        self.startEast = int(startEast)
        self.posNorth = int(startNorth)
        self.posEast = int(startEast)

    def Move(self, instruction):

        self.moveCommand = {
            'N':self.MoveNorth,
            'S':self.MoveSouth,
            'E':self.MoveEast,
            'W':self.MoveWest,
            'L':self.TurnLeft,
            'R':self.TurnRight,
            'F':self.MoveForward
        }
        self.moveCommand[instruction[0]](int(instruction[1:]))

    def TurnLeft(self, amount):
        # print(f'Change heading anti-clockwise {amount} degrees')
        self.heading = (self.heading - amount) % 360

    def TurnRight(self, amount):
        # print(f'Change heading clockwise {amount} degrees')
        self.heading = (self.heading + amount) % 360

    def MoveNorth(self, distance):
        # print(f'Move north {distance} units')
        self.posNorth += distance

    def MoveSouth(self, distance):
        # print(f'Move south {distance} units')
        self.posNorth -= distance

    def MoveEast(self, distance):
        # print(f'Move east {distance} units')
        self.posEast += distance

    def MoveWest(self, distance):
        # print(f'Move west {distance} units')
        self.posEast -= distance

    def MoveForward(self, distance):
        # print(f'Move forward {distance} units')
        # print('heading:', self.heading)

        orientation = {
            0: self.MoveNorth,
            90: self.MoveEast,
            180: self.MoveSouth,
            270: self.MoveWest
        }
        orientation[self.heading](distance)

    def ManhattanDistance(self):
        return abs(self.posNorth) + abs(self.posEast)

a = Boat(0, 0, 90)
[a.Move(d) for d in data]
print(a.ManhattanDistance())