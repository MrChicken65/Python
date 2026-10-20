from cImage import *

def negativePixel (oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def makeNegative(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Negative Image", width * 2, height)
    oldImage.draw(myImageWindow) # draws original image in window first
    newImage = EmptyImage(width, height)
    