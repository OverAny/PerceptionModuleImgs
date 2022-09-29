from PIL import Image, ImageDraw, ImageColor
import random 


# shapes = ["parallelogram", "rectangle", "trapezoid", "square"]

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

    # parallelogram
    # draw.polygon([(40+x,40+randoSize+y),(60+x,80+randoSize+y),(120+randoDist+x,80+y), (100+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 

    # # trapezoid
    # draw.polygon([(60+x+randoDist+randoSize,40+y+randoDist),(40+x+randoSize+randoDist,80+y+randoDist),(140+x+randoDist,80+y+randoDist), (120+x+randoDist,40+y+randoDist)], fill=currentColor, outline=currentColor) 

    #draw.polygon([(190+x,40+randoSize+y),(210+x,80+randoSize+y),(270+randoDist+x,80+y), (250+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 

    if num == 0:
        if shape == "square":
            draw.rectangle((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((60+randoDist+x, 60+randoDist+y, 160+randoDist+x+randoSize, 200+randoDist+y+randoSize), fill=currentColor)
        if shape == "parallelogram":
            draw.polygon([(40+x,40+randoSize+y),(60+x,80+randoSize+y),(120+randoDist+x,80+y), (100+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 
        if shape == "trapezoid":
            draw.polygon([(60+x+randoDist+randoSize,40+y+randoDist),(40+x+randoSize+randoDist,80+y+randoDist),(140+x+randoDist,80+y+randoDist), (120+x+randoDist,40+y+randoDist)], fill=currentColor, outline=currentColor) 

    if num == 1:
        if shape == "square":
            draw.rectangle((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 160+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((210+randoDist+x, 60+randoDist+y, 310+randoDist+x+randoSize, 200+randoDist+y+randoSize), fill=currentColor)        
        if shape == "parallelogram":
            draw.polygon([(190+x,40+randoSize+y),(210+x,80+randoSize+y),(270+randoDist+x,80+y), (250+randoDist+x,40+y)], fill=currentColor, outline=currentColor) 
        if shape == "trapezoid":
            draw.polygon([(210+x+randoDist+randoSize,40+y+randoDist),(190+x+randoSize+randoDist,80+y+randoDist),(290+x+randoDist,80+y+randoDist), (270+x+randoDist,40+y+randoDist)], fill=currentColor, outline=currentColor) 

    if num == 2:
        if shape == "square":
            draw.rectangle((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((60+randoDist+x, 210+randoDist+y, 160+randoDist+x+randoSize, 350+randoDist+y+randoSize), fill=currentColor)
        if shape == "parallelogram":
            draw.polygon([(40+x,190+randoSize+y),(60+x,230+randoSize+y),(120+randoDist+x,230+y), (100+randoDist+x,190+y)], fill=currentColor, outline=currentColor) 
        if shape == "trapezoid":
            draw.polygon([(60+x+randoDist+randoSize,190+y+randoDist),(40+x+randoSize+randoDist,230+y+randoDist),(140+x+randoDist,230+y+randoDist), (120+x+randoDist,190+y+randoDist)], fill=currentColor, outline=currentColor) 

    if num == 3:
        if shape == "square":
            draw.rectangle((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 310+randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((210+randoDist+x, 210+randoDist+y, 310+randoDist+x+randoSize, 350+randoDist+y+randoSize), fill=currentColor)
        if shape == "parallelogram":
            draw.polygon([(190+x,190+randoSize+y),(210+x,230+randoSize+y),(270+randoDist+x,230+y), (250+randoDist+x,190+y)], fill=currentColor, outline=currentColor) 
        if shape == "trapezoid":
            draw.polygon([(210+x+randoDist+randoSize,190+y+randoDist),(190+x+randoSize+randoDist,230+y+randoDist),(290+x+randoDist,230+y+randoDist), (270+x+randoDist,190+y+randoDist)], fill=currentColor, outline=currentColor) 

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

with open('GeneratedFiles/generated-quad-shape-direction-color.txt') as f:
    lines = f.readlines()
    LinesDesc = lines

with open('GeneratedFiles/generated_gen-quad-shape-direction-color.txt') as f:
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
    
        im.save('GeneratedImages-ShapeDirColor/' + LinesDesc[zz] + '.png', quality=95)
       
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

