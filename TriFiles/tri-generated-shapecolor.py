from PIL import Image, ImageDraw, ImageColor
import random 


shapes = ["isosceles triangle", "equilateral triangle", "triangle"]

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

with open('GeneratedFiles/generated-tri-shape-color.txt') as f:
    lines = f.readlines()
    LinesDesc = lines

with open('GeneratedFiles/generated_gen-tri-shape-color.txt') as f:
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

        randoDist = random.randint(0, 100)
        randoSize = random.randint(0, 100)


        x = random.randint(0, 400)
        y = random.randint(0, 400)

        if shape == "equilateral triangle":
            draw.regular_polygon((270+randoDist+x, 120+randoDist+y, 50+randoSize), 3, fill=currentColor)
        if shape == "isosceles triangle":
            draw.polygon([(100+x,100+y), (200+randoSize+x, 300+y), (300+randoSize+x,100+y+randoSize)], fill=currentColor)
        if shape == "triangle":
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            x1 = random.randint(0, 400)
            y1 = random.randint(0, 400)
            x2 = random.randint(0, 400)
            y2 = random.randint(0, 400)
            randoDist = random.randint(0, 200)

            draw.polygon([(x+randoDist,y+randoDist), (x1+randoDist,y1+randoDist), (x2+randoDist,x2+randoDist)], fill=currentColor)

        im.save('GeneratedImages-ShapeColor/' +str(zz) + ". "+  LinesDesc[zz] + '.png', quality=95)
        
     

print(len(LinesDesc))

    # itemz = TopLeft[2]
    # currentColor = ImageColor.getcolor(colors[itemz[0]], "RGB")

    # draw.rectangle((60, 60, 60+int(shapes[itemz[1]][0]), 60+int(shapes[itemz[1]][1])), fill=currentColor)

# draw.regular_polygon((500, 500, 50), 6, fill=(222, 222, 122))

# draw.ellipse((130, 65, 210, 145), fill=(255, 0, 0))
# draw.rectangle((240, 50, 310, 120), fill=(0, 192, 192))

# draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

