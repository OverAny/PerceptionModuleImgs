
import random

shapes = ["parallelogram", "rectangle", "trapezoid", "square"]

amountToGenerate = 100
lines = []
linesGen = []

for i in range(amountToGenerate):

    shapesR = random.randint(0, len(shapes)-1)

    text = ""
    textGen = ""

    text += "a " + shapes[shapesR]
    textGen += shapes[shapesR]
            
    linesGen.append(textGen)
    lines.append(text)

with open('GeneratedFiles/generated-quad-shape.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('GeneratedFiles/generated_gen-quad-shape.txt', 'w') as f:
    for line in linesGen:
        f.write(line)
        f.write('\n')