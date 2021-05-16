from Cube import Cube, Piece
from maths import Point, Matrix

# INITIALIZE SOLVED CUBE
cube = Cube('')
test = Cube('')
print(test)
print(test.getCornerList())

testPiece = Piece([0, 0, 0], ['w', 'g', 'r'], test)
testPiece2 = Piece([0, 1, 0], ['w', 'None', 'r'], test)
print(test)
print(test.getEdgeList())