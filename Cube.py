import numpy as np
import Piece as pc


class Cube:
    pieceList = []

    def __init__(self):
        self.pieceList = []

    def getPieceList(self):
        return self.pieceList

    def addPiece(self, piece):
        self.pieceList.append(piece)

    def __str__(self):
        return 'This cube has ' + str(len(self.pieceList)) + ' pieces so far.'


def main():
    test = Cube()
    print(test)

    testPiece = pc.Piece([0, 0, 0], ['w', 'g', 'r'], test)
    print(test)




if __name__ == '__main__':
    main()
