# This came together a lot quicker than I expected :)
with open("Day_12\input") as f:
    data = f.read().splitlines()

#data = ['F10', 'N3', 'F7', 'R90', 'F11']

class Boat:
    def __init__(self, startNorth, startEast):
        self.startNorth = int(startNorth)
        self.startEast = int(startEast)
        self.posNorth = int(startNorth)
        self.posEast = int(startEast)
        self.wp = Waypoint(1, 10)

    def ProcessInstruction(self, instruction):
        if instruction[0] == 'F':
            self.MoveForward(int(instruction[1:]))
        else:
            self.wp.MoveRelative(instruction)

    def MoveForward(self, distance):
        self.posNorth += distance * self.wp.GetRelativeNorth()
        self.posEast += distance * self.wp.GetRelativeEast()

    def ManhattanDistance(self):
        return abs(self.posNorth) + abs(self.posEast)


class Waypoint:
    def __init__(self, relativeNorth, relativeEast):
        self.relNorth = int(relativeNorth)
        self.relEast = int(relativeEast)

    def MoveRelative(self, instruction):

        self.moveCommand = {
            'N':self.MoveNorth,
            'S':self.MoveSouth,
            'E':self.MoveEast,
            'W':self.MoveWest,
            'L':self.RotateLeft,
            'R':self.RotateRight
        }
        self.moveCommand[instruction[0]](int(instruction[1:]))

    def GetRelativeNorth(self):
        return self.relNorth

    def GetRelativeEast(self):
        return self.relEast

    def RotateLeft(self, amount):
        for self._i in range(int(amount/90)):
            self._tmpN = self.relNorth
            self._tmpE = self.relEast
            self.relNorth = self._tmpE
            self.relEast = - self._tmpN

    def RotateRight(self, amount):
        for self._i in range(int(amount/90)):
            self._tmpN = self.relNorth
            self._tmpE = self.relEast
            self.relNorth = - self._tmpE
            self.relEast = self._tmpN


    def MoveNorth(self, distance):
        self.relNorth += distance

    def MoveSouth(self, distance):
        self.relNorth -= distance

    def MoveEast(self, distance):
        self.relEast += distance

    def MoveWest(self, distance):
        self.relEast -= distance

a = Boat(0, 0)
[a.ProcessInstruction(d) for d in data]
print(a.ManhattanDistance())