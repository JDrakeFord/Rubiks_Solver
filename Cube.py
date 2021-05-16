#imports
from maths import Point, Matrix

# 90 degree rotations in the XY plane. CW is clockwise, CC is counter-clockwise.
ROT_XY_CW = Matrix(0, 1, 0,
                   -1, 0, 0,
                   0, 0, 1)
ROT_XY_CC = Matrix(0, -1, 0,
                   1, 0, 0,
                   0, 0, 1)

# 90 degree rotations in the XZ plane (around the y-axis when viewed pointing toward you).
ROT_XZ_CW = Matrix(0, 0, -1,
                   0, 1, 0,
                   1, 0, 0)
ROT_XZ_CC = Matrix(0, 0, 1,
                   0, 1, 0,
                   -1, 0, 0)

# 90 degree rotations in the YZ plane (around the x-axis when viewed pointing toward you).
ROT_YZ_CW = Matrix(1, 0, 0,
                   0, 0, 1,
                   0, -1, 0)
ROT_YZ_CC = Matrix(1, 0, 0,
                   0, 0, -1,
                   0, 1, 0)


# Cube class
class Cube:
    pieceList = []
    cubeString = ''

    def __init__(self, cube_string):
        self.pieceList = []
        self.centerList = []
        self.edgeList = []
        self.cornerList = []
        self.cubeString = cube_string

    def R(self):
        for piece in self.pieceList:
            if piece.getPosition().getitem():
                print("nice")


    def F(self):
        for piece in self.pieceList:
            if piece.getPosition().getX() == 1:
                piece = piece * ROT_YZ_CW



    def getPieceList(self):
        return self.pieceList

    def addPiece(self, piece):
        self.pieceList.append(piece)

    def getCenterList(self):
        return self.centerList

    def getEdgeList(self):
        return self.edgeList

    def getCornerList(self):
        return self.cornerList

    def addToTypeList(self, piece):
        if piece.getType() == 'Center':
            self.centerList.append(piece)
        elif piece.getType() == 'Edge':
            self.edgeList.append(piece)
        elif piece.getType() == 'Corner':
            self.cornerList.append(piece)

    def __str__(self):
        part1 = 'This cube has ' + str(len(self.pieceList)) + ' piece objects so far.\n' \
               'This cube has ' + str(len(self.centerList)) + ' center piece objects.\n' \
               'This cube has ' + str(len(self.edgeList)) + ' edge piece objects.\n' \
               'This cube has ' + str(len(self.cornerList)) + ' corner piece objects.\n\n'
        part2 = ''

        return part1 + part2

# Piece class
class Piece:
    position = Point(0,0,0)
    colors = ['w', 'w', 'w']
    type = "Corner"

    def __init__(self, inputPosition, inputColors, cube):
        for i in range(0, 3):
            self.position[i] = inputPosition[i]
            self.colors[i] = inputColors[i]
            self.setType()
        cube.addPiece(self)
        cube.addToTypeList(self)

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
        """
        :param:self
        :return: Point object for position
        """
        return self.position

    def getColors(self):
        return self.colors

    def getType(self):
        return self.type

    def __str__(self):
        return "Position (x,y,z) = " + str(self.position) + "\nColors (x,y,z) = "+ str(self.colors) + "\nType: " + self.getType()

    def __repr__(self):
        return "Position (x,y,z) = " + str(self.position) + "\nColors (x,y,z) = "+ str(self.colors) + "\nType: " + self.getType()
