from cImage import *
from doubleimage import *

def halfImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW // 2, oldH // 2)

    for row in range(newIm.getHeight()):
        for col in range(newIm.getWidth()):
            originalCol = col * 2
            originalRow = row * 2
            oldPixel = oldImage.getPixel(originalCol, originalRow)

            newIm.setPixel(col, row, oldPixel)

    return newIm


def makeHalfImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Half Size", width * 2, height)
    oldImage.draw(myWin)

    newImage = halfImage(oldImage)
    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()

def makeDoubleHalfImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Double and Half Size", width * 2, height * 3)
    oldImage.draw(myWin)

    newImage = doubleImage(oldImage)
    newImage.setPosition(0, oldImage.getHeight() + 1)
    newImage.draw(myWin)

    originalImage = halfImage(newImage)
    originalImage.setPosition(oldImage.getWidth() + 1, 0)
    originalImage.draw(myWin)

    myWin.exitOnClick()


if __name__ == '__main__':
    #makeHalfImage('castle.gif')
    makeDoubleHalfImage('castle.gif')
