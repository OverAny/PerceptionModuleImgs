
import random

shapes = ["parallelogram", "rectangle", "trapezoid", "square"]
colors = ["orange", "yellow", "green", "blue", "purple", "red", "black", "pink", "brown"]
directionsUp = ["bottom", "top"]
directionsSide = ["left", "right"]


numbers = 4
amountToGenerate = 100
lines = []
linesGen = []

for i in range(amountToGenerate):
    text = ""
    textGen = ""
    ran = random.randint(1, numbers)

    for x in range(ran):
        colorR = random.randint(0, len(colors)-1)
        shapesR = random.randint(0, len(shapes)-1)
        directionsUpR = random.randint(0, len(directionsUp)-1)
        directionsSideR = random.randint(0, len(directionsSide)-1)
        if (x != ran-1):
            if (colors[colorR] != "orange"):
                text += "a " + colors[colorR] + " " + shapes[shapesR] + " in the " + directionsUp[directionsUpR] + " " + directionsSide[directionsSideR] + " and "
            else:
                text += "an " + colors[colorR] + " " + shapes[shapesR] + " in the " + directionsUp[directionsUpR] + " " + directionsSide[directionsSideR] + " and "
            textGen += colors[colorR]+","+shapes[shapesR]+","+directionsUp[directionsUpR]+","+directionsSide[directionsSideR]+"/"
        else: 
            text += "a " + colors[colorR] + " " + shapes[shapesR] + " in the " + directionsUp[directionsUpR] + " " + directionsSide[directionsSideR]
            textGen += colors[colorR]+","+shapes[shapesR]+","+directionsUp[directionsUpR]+","+directionsSide[directionsSideR]

    linesGen.append(textGen)
    lines.append(text)

with open('GeneratedFiles/generated-quad-shape-direction-color.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('GeneratedFiles/generated_gen-quad-shape-direction-color.txt', 'w') as f:
    for line in linesGen:
        f.write(line)
        f.write('\n')