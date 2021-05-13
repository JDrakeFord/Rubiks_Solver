import numpy as np
import Piece as pc

#Cube class
class Cube:
    pieceList = []
    centerList = []
    edgeList = []
    cornerList = []
    cubeString = ''

    def __init__(self, cube_string):
        self.pieceList = []
        self.centerList = []
        self.edgeList = []
        self.cornerList = []
        self.cubeString = cube_string

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


#main method
def main():
    test = Cube('')
    print(test)
    print(test.getCornerList())

    testPiece = pc.Piece([0, 0, 0], ['w', 'g', 'r'], test)
    testPiece2 = pc.Piece([0, 1, 0], ['w', 'None', 'r'], test)
    print(test)
    print(test.getEdgeList())



if __name__ == '__main__':
    main()