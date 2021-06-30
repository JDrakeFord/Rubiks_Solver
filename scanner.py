import PIL
import PIL.Image


tupleList = []

preim = PIL.Image.open("Cube.jpg")

img = preim.convert('RGB')

for x in range (124, 175):
    for y in range(75, 122):
        tupleList.append(img.getpixel(tuple([x, y])))

print(tupleList)

