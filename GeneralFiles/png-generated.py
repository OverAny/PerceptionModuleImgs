from PIL import Image, ImageDraw, ImageColor
import random 


# draw.rectangle((50, 50, 200, 200), fill=(0, 192, 192))
# draw.rectangle((200, 50, 350, 200), fill=(0, 0, 192))
# draw.rectangle((50, 200, 200, 350), fill=(0, 192, 0))
# draw.rectangle((200, 200, 350, 350), fill=(0, 0, 0))

# draw.rectangle((450, 50, 600, 200), fill=(0, 192, 192))
# draw.rectangle((600, 50, 750, 200), fill=(0, 0, 192))
# draw.rectangle((450, 200, 600, 350), fill=(0, 192, 0))
# draw.rectangle((600, 200, 750, 350), fill=(0, 0, 0))

# draw.rectangle((50, 450, 200, 600), fill=(0, 192, 192))
# draw.rectangle((200, 450, 350, 600), fill=(0, 0, 192))
# draw.rectangle((50, 600, 200, 750), fill=(0, 192, 0))
# draw.rectangle((200, 600, 350, 750), fill=(0, 0, 0))

# draw.rectangle((450, 450, 600, 600), fill=(0, 192, 192))
# draw.rectangle((600, 450, 750, 600), fill=(0, 0, 192))
# draw.rectangle((450, 600, 600, 750), fill=(0, 192, 0))
# draw.rectangle((600, 600, 750, 750), fill=(0, 0, 0))


def drawNow(num, color, shape, typeOne):
    randoDist = random.randint(-9, 30)
    randoSize = random.randint(-30, 0)
    
    currentColor = ImageColor.getcolor(colors[color], "RGB")
    
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

    if num == 0:
        if shape == "circle":
            draw.ellipse((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "square":
            draw.rectangle((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 200+randoDist+y+randoSize), fill=currentColor)
        if shape == "line":
            draw.line((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor, width=6)
        if shape == "hexagon":
            draw.regular_polygon((120+randoDist+x, 120+randoDist+y, 50+randoSize), 6, fill=currentColor)
        if shape == "triangle":
            draw.regular_polygon((120+randoDist+x, 120+randoDist+y, 50+randoSize), 3, fill=currentColor)
        if shape == "pentagon":
            draw.regular_polygon((120+randoDist+x, 120+randoDist+y, 50+randoSize), 5, fill=currentColor)

    if num == 1:
        if shape == "circle":
            draw.ellipse((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "square":
            draw.rectangle((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 200+randoDist+y+randoSize), fill=currentColor)
        if shape == "line":
            draw.line((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor, width=6) 
        if shape == "hexagon":
            draw.regular_polygon((270+randoDist+x, 120+randoDist+y, 50+randoSize), 6, fill=currentColor)
        if shape == "triangle":
            draw.regular_polygon((270+randoDist+x, 120+randoDist+y, 50+randoSize), 3, fill=currentColor)
        if shape == "pentagon":
            draw.regular_polygon((270+randoDist+x, 120+randoDist+y, 50+randoSize), 5, fill=currentColor)

    if num == 2:
        if shape == "circle":
            draw.ellipse((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "square":
            draw.rectangle((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 350+randoDist+y+randoSize), fill=currentColor)
        if shape == "line":
            draw.line((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor, width=6)
        if shape == "hexagon":
            draw.regular_polygon((120+randoDist+x, 270+randoDist+y, 50+randoSize), 6, fill=currentColor)
        if shape == "triangle":
            draw.regular_polygon((120+randoDist+x, 270+randoDist+y, 50+randoSize), 3, fill=currentColor)
        if shape == "pentagon":
            draw.regular_polygon((120+randoDist+x, 270+randoDist+y, 50+randoSize), 5, fill=currentColor)

    if num == 3:
        if shape == "circle":
            draw.ellipse((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "square":
            draw.rectangle((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 350+randoDist+y+randoSize), fill=currentColor)
        if shape == "line":
            draw.line((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor, width=6)
        if shape == "hexagon":
            draw.regular_polygon((270+randoDist+x, 270+randoDist+y, 50+randoSize), 6, fill=currentColor)
        if shape == "triangle":
            draw.regular_polygon((270+randoDist+x, 270+randoDist+y, 50+randoSize), 3, fill=currentColor)
        if shape == "pentagon":
            draw.regular_polygon((270+randoDist+x, 270+randoDist+y, 50+randoSize), 5, fill=currentColor)


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

# for reference
shapes = {
    "square": [100, 100], 
    "line": [100, 100], 
    "rectangle": [100, 60], 
    "triangle": [50, 3], 
    "hexagon": [50, 6],
    "pentagon": [50, 5],
    "circle":  [100, 100]
    }

directions = ["bottom", "top"]
directionsSide = ["left", "right"]

TopLeft = []
TopRight = []
BottomLeft = []
BottomRight = []

LinesDesc = []

with open('GeneratedFiles/generated.txt') as f:
    lines = f.readlines()
    LinesDesc = lines

with open('GeneratedFiles/generated_gen.txt') as f:
    lines = f.readlines()
    # can change to all
    for zz in range(len(lines)):
        im = Image.new('RGB', (800, 800), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        ls = lines[zz].split("/")      
        for line in ls:
            item = None
            lineS = line.split(",")  

            # remove /n at the end
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
            print(num)
            for i in range(len(num)):
                drawNow(num[i], TopLeft[i][0], TopLeft[i][1], "topleft")

        if len(TopRight) != 0:
            num = random.sample(li,len(TopRight))
            for i in range(len(num)):
                drawNow(num[i], TopRight[i][0], TopRight[i][1], "topright")

        if len(BottomLeft) != 0:
            num = random.sample(li,len(BottomLeft))
            for i in range(len(num)):
                drawNow(num[i], BottomLeft[i][0], BottomLeft[i][1], "bottomleft")

        if len(BottomRight) != 0:
            num = random.sample(li,len(BottomRight))
            for i in range(len(num)):
                drawNow(num[i], BottomRight[i][0], BottomRight[i][1], "bottomright")
    
        im.save('GeneratedImages/' + LinesDesc[zz].replace('\n', '') + '.png', quality=95)
       
        TopLeft.clear()
        TopRight.clear()
        BottomLeft.clear()
        BottomRight.clear()

print(len(LinesDesc))


    # itemz = TopLeft[2]
    # currentColor = ImageColor.getcolor(colors[itemz[0]], "RGB")

    # draw.rectangle((60, 60, 60+int(shapes[itemz[1]][0]), 60+int(shapes[itemz[1]][1])), fill=currentColor)



# draw.regular_polygon((500, 500, 50), 6, fill=(222, 222, 122))

# draw.ellipse((130, 65, 210, 145), fill=(255, 0, 0))
# draw.rectangle((240, 50, 310, 120), fill=(0, 192, 192))

# draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

