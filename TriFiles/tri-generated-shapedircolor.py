from PIL import Image, ImageDraw, ImageColor
import random 



def drawNow(num, color, shape, typeOne):
    randoDist = random.randint(-10, 10)
    randoSize = random.randint(-10, 10)

    currentColor = ImageColor.getcolor(colors[color], "RGB")
    
    x = 0
    y = 0


    if typeOne == "topleft":
        x = 0
        y = 0
    if typeOne == "topright":
        x = 400
        y = 0
    if typeOne == "bottomleft":
        x = 0
        y = 400
    if typeOne == "bottomright":
        x = 400
        y = 400

    xTwo = 0
    yTwo = 0


    if num == 0:
        xTwo = 0
        yTwo = 0
    if num == 1:
        xTwo = 150
        yTwo = 0
    if num == 2:
        xTwo = 0
        yTwo = 150
    if num == 3:
        xTwo = 150
        yTwo = 150
    # parallelogram
    # draw.polygon([(40+x,40+randoSize+y),(60+x,80+randoSize+y),(120+randoDist+x,80+y), (100+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 

    # # trapezoid
    # draw.polygon([(60+x+randoDist+randoSize,40+y+randoDist),(40+x+randoSize+randoDist,80+y+randoDist),(140+x+randoDist,80+y+randoDist), (120+x+randoDist,40+y+randoDist)], fill=currentColor, outline=currentColor) 

    #draw.polygon([(190+x,40+randoSize+y),(210+x,80+randoSize+y),(270+randoDist+x,80+y), (250+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 

    if shape == "equilateral triangle":
        draw.regular_polygon((120+randoDist+x+xTwo, 120+randoDist+y+yTwo, 50+randoSize), 3, fill=currentColor)
    if shape == "isosceles triangle":
        draw.polygon([(100+x+xTwo,100+y+yTwo), (125+randoSize+x+xTwo, 180+y+yTwo), (150+x+xTwo,100+y+yTwo)], fill=currentColor)
    if shape == "triangle":

        x1 = random.randint(-30, 30)
        y1 = random.randint(-30, 30)
        x2 = random.randint(-30, 30)
        y2 = random.randint(-30, 30)
        x3 = random.randint(-30, 30)
        y3 = random.randint(-30, 30)


        draw.polygon([(100+x+xTwo+x1,100+y+yTwo+y1), (125+randoSize+x+xTwo+x2, 180+y+yTwo+y2), (150+randoSize+x+xTwo+x3,100+y+randoSize+yTwo+y3)], fill=currentColor)

colors = {
    "orange": "#ff9900", 
    "yellow": "#ffff00", 
    "green": "#33cc33",
    "blue": "#0033cc",
    "purple": "#9900cc",
    "red": "#ff0000",
    "black": "#000000",
    "pink": "#ff6699", 
    "brown": "#993300"
    }


directions = ["bottom", "top"]
directionsSide = ["left", "right"]

TopLeft = []
TopRight = []
BottomLeft = []
BottomRight = []

LinesDesc = []

with open('GeneratedFiles/generated-tri-shape-direction-color.txt') as f:
    lines = f.readlines()
    LinesDesc = lines

with open('GeneratedFiles/generated_gen-tri-shape-direction-color.txt') as f:
    lines = f.readlines()
    # can change to all
    for zz in range(100):
        im = Image.new('RGB', (800, 800), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        ls = lines[zz].split("/")      
        for line in ls:
            item = None
            lineS = line.split(",")  

            # remov2e /n at the end
            lineS[3] = lineS[3].rstrip()

            if lineS[2] == "bottom":
                if lineS[3] == "left":
                    BottomLeft.append([lineS[0], lineS[1]])
                if lineS[3] == "right":
                    BottomRight.append([lineS[0], lineS[1]])
            if lineS[2] == "top":
                if lineS[3] == "left":
                    TopLeft.append([lineS[0], lineS[1]])
                if lineS[3] == "right":
                    TopRight.append([lineS[0], lineS[1]])

        print(TopLeft)
        print(TopRight)
        print(BottomLeft)
        print(BottomRight)


        li=range(0,4)

        if len(TopLeft) != 0:
            num = random.sample(li,len(TopLeft))
            for i in range(len(num)):
                print(num)
                drawNow(num[i], TopLeft[i][0], TopLeft[i][1], "topleft")

        if len(TopRight) != 0:
            num = random.sample(li,len(TopRight))
            for i in range(len(num)):
                print(num)
                drawNow(num[i], TopRight[i][0], TopRight[i][1], "topright")

        if len(BottomLeft) != 0:
            num = random.sample(li,len(BottomLeft))
            for i in range(len(num)):
                print(num)
                drawNow(num[i], BottomLeft[i][0], BottomLeft[i][1], "bottomleft")

        if len(BottomRight) != 0:
            num = random.sample(li,len(BottomRight))
            for i in range(len(num)):
                print(num)
                drawNow(num[i], BottomRight[i][0], BottomRight[i][1], "bottomright")

        im.save('GeneratedImages-ShapeDirColor/' + LinesDesc[zz] + '.png', quality=95)
       
        TopLeft.clear()
        TopRight.clear()
        BottomLeft.clear()
        BottomRight.clear()

print(len(LinesDesc))

