import numpy as np


class Piece:
    position = [0, 0, 0]
    colors = ['w', 'w', 'w']
    type = "Corner"

    def __init__(self, inputPosition, inputColors):
        for i in range(0, 3):
            self.position[i] = inputPosition[i]
            self.colors[i] = inputColors[i]
            self.setType()

    def setType(self):
        count = 0
        for i in range(0, 3):
            if self.colors[i] == 'None':
                count = count + 1
        if count == 0:
            self.type = 'Corner'
        if count == 1:
            self.type = 'Edge'
        if count == 2:
            self.type = 'Center'


    def getPosition(self):
        return self.position

    def getColors(self):
        return self.colors

    def getType(self):
        return self.type

    def __str__(self):
        return "Position (x,y,z) = " + str(self.position) + "\nColors (x,y,z) = "+ str(self.colors) + "\nType: " + self.getType()

def main():
    test = Piece([1, 1, 1], ['None', 'None', 'g'])
    print(test)

if __name__ == '__main__':
    main()


