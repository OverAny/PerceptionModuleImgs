
import random

shapes = ["isosceles triangle", "equilateral triangle", "triangle"]

amountToGenerate = 100
lines = []
linesGen = []

for i in range(amountToGenerate):

    shapesR = random.randint(0, len(shapes)-1)

    text = ""
    textGen = ""
    if (shapes[shapesR] == "isosceles triangle" or shapes[shapesR] == "equilateral triangle"):
        text += "an " + shapes[shapesR]
    else:
        text += "a " + shapes[shapesR]
    textGen += shapes[shapesR]
            
    linesGen.append(textGen)
    lines.append(text)

with open('GeneratedFiles/generated-tri-shape.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('GeneratedFiles/generated_gen-tri-shape.txt', 'w') as f:
    for line in linesGen:
        f.write(line)
        f.write('\n')