
import random

shapes = ["isosceles triangle", "equilateral triangle", "triangle"]
colors = ["orange", "yellow", "green", "blue", "purple", "red", "black", "pink", "brown"]

amountToGenerate = 100
lines = []
linesGen = []

for i in range(amountToGenerate):
    
    colorR = random.randint(0, len(colors)-1)
    shapesR = random.randint(0, len(shapes)-1)

    text = ""
    textGen = ""

    if (colors[colorR] != "orange"):
        text += "a " + colors[colorR] + " " + shapes[shapesR] + "."
    else:
        text += "an " + colors[colorR] + " " + shapes[shapesR] + "."
    textGen += colors[colorR]+","+shapes[shapesR]
            
    linesGen.append(textGen)
    lines.append(text)

with open('GeneratedFiles/generated-tri-shape-color.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('GeneratedFiles/generated_gen-tri-shape-color.txt', 'w') as f:
    for line in linesGen:
        f.write(line)
        f.write('\n')