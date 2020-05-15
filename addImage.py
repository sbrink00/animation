from display import *

def readImageFile(imagefile):
  with open(imagefile, "r") as f:
    lines = f.readlines()
    width,height = (int(x) for x in lines[1].replace("\n", "").split(" "))
    image = " ".join(lines[3:]).replace("\n", "").split(" ")
    image.remove("")
    newImage = []
    for i in range(0, len(image), 3):
      newImage.append([int(x) for x in image[i:i + 3]])
    newImage = resize(newImage, width, height)
    return newImage

def resize(image, width, height):
  output = []
  for y in range(height):
    temp = []
    for x in range(width):
      temp.append(image[y * width + x])
    output.append(temp)
  return output

def addTextImage(screen, imagefile, move):
  image = readImageFile(imagefile)
  for y in range(len(image)):
    for x in range(len(image[0])):
      newy,newx = y + move[1],x + move[0]
      if newy >= 0 and newy < len(screen) and newx >= 0 and newx < len(screen[0]):
        screen[newy][newx] = image[y][x]
