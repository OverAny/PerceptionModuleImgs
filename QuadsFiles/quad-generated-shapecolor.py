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

LinesDesc = []

with open('GeneratedFiles/generated-quad-shape-color.txt') as f:
    lines = f.readlines()
    LinesDesc = lines

with open('GeneratedFiles/generated_gen-quad-shape-color.txt') as f:
    lines = f.readlines()
    # can change to all
    im = Image.new('RGB', (800, 800), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for zz in range(100):
        im = Image.new('RGB', (800, 800), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        ls = lines[zz] 


        lineS = ls.split(",")
        color = lineS[0]
        shape = lineS[1].rstrip()

        print(shape)
        currentColor = ImageColor.getcolor(colors[color], "RGB")

        randoDist = random.randint(0, 200)
        randoSize = random.randint(0, 300)


        x = random.randint(0, 200)
        y = random.randint(0, 300)

        if shape == "square":
            draw.rectangle((randoDist+x, randoDist+y, randoDist+x+randoSize, randoDist+y+randoSize), fill=currentColor)
        if shape == "rectangle":
            draw.rectangle((randoDist+x, randoDist+y+100, randoDist+x+randoSize, randoDist+y+randoSize+100), fill=currentColor)
        if shape == "parallelogram":
            draw.polygon([(x,randoSize+y),(x+100,randoSize+y),(randoDist+x+100,y+100), (randoDist+x,y+100)], fill=currentColor, outline=currentColor) 
        if shape == "trapezoid":
            draw.polygon([(x+randoDist+randoSize,y+randoDist),(x+randoSize+randoDist+100,y+randoDist),(x+randoSize+randoDist+200,y+randoDist+100), (x+randoDist,y+randoDist+100)], fill=currentColor, outline=currentColor) 

        im.save('GeneratedImages-ShapeColor/' + LinesDesc[zz] + '.png', quality=95)
        
     

print(len(LinesDesc))

    # itemz = TopLeft[2]
    # currentColor = ImageColor.getcolor(colors[itemz[0]], "RGB")

    # draw.rectangle((60, 60, 60+int(shapes[itemz[1]][0]), 60+int(shapes[itemz[1]][1])), fill=currentColor)

# draw.regular_polygon((500, 500, 50), 6, fill=(222, 222, 122))

# draw.ellipse((130, 65, 210, 145), fill=(255, 0, 0))
# draw.rectangle((240, 50, 310, 120), fill=(0, 192, 192))

# draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

