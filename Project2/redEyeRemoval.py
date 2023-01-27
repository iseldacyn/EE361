from cImage import *

# removal of red eyes from on an image within the specified rectangle
# takes an image file and a specified rectangle coordinates as arguments
# creates a new image the same size as the old image
# goes through each pixel in the old image and assigns it to the new image
# if the old pixel is within and row and column specified, the R value of the pixel is measured
# if it is greater than 150, it is reassigned to be the average of the G and B values
def removeRedEyes(imageFileName, col1, row1, col2, row2):
    # imageFileName = FileImage(imageFileName)
    width = imageFileName.getWidth()
    height = imageFileName.getHeight()

    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = imageFileName.getPixel(col, row)
            if ((row >= row1) & (row <= row2)) & ((col >= col1) & (col <= col2)):
                if oldPixel.getRed() > 150:
                    G = oldPixel.getGreen()
                    B = oldPixel.getBlue()
                    newR = (G + B) // 2
                    newPixel = Pixel(newR, G, B)
                    newIm.setPixel(col, row, newPixel)
                else:
                    newIm.setPixel(col, row, oldPixel)
            else:
                newIm.setPixel(col, row, oldPixel)

    return newIm

# display function for original image and new image side-by-side
def Disp(oldImage, newImage):
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Remove Red Eyes", width * 2, height)
    oldImage.draw(myWin)

    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()

# tests red eye removal function with 3 different cases
def main():
    im1 = FileImage('redEyes1.gif')
    im2 = FileImage('redEyes2.gif')
    im3 = FileImage('redEyes3.gif')
    newim1 = removeRedEyes(im1, 120, 195, 140, 215)
    newim1 = removeRedEyes(newim1, 220, 185, 240, 205)
    newim2 = removeRedEyes(im2, 70, 180, 115, 195)
    newim2 = removeRedEyes(newim2, 210, 170, 250, 180)
    newim3 = removeRedEyes(im3, 100, 90, 140, 140)
    newim3 = removeRedEyes(newim3, 350, 100, 395, 145)

    Disp(im1, newim1)
    Disp(im2, newim2)
    Disp(im3, newim3)


if __name__ == '__main__':
    main()
