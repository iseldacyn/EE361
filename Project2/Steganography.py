from cImage import *


# stegano function takes a file and secret text and arguments and returns a FileImage
# first, creates a new FileImage with the last four bits of each pixel color channel
# deleted, shown by '& ~0x0F' operation
# then, the secret message is encoded in the bottom left of the image (as the corner pixels
# of an image are generally not looked at frequently)
# the first pixel is assigned the length of the message
# each subsequent pixel in the row are assigned each character of the image
# NOTE: each character is converted to an int to perform bitwise operations
# the secret is assumed to be a shorter length than the width of the image
# the new image with the encoded secret message is then returned as a FileImage
def stegano(imageFileName, secret):
    oldImage = FileImage(imageFileName)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    newImage = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPix = oldImage.getPixel(col, row)
            newPix = Pixel(oldPix.getRed() & ~0x0F, oldPix.getGreen() & ~0x0F, oldPix.getBlue() & ~0x0F)
            newImage.setPixel(col, row, newPix)

    for i in range(len(secret)+1):
        pix = newImage.getPixel(i, height-1)
        if i == 0:
            lowerHalf = len(secret) & ~0xF0
            upperHalf = len(secret) & ~0x0F
        else:
            c = ord(secret[i-1])
            lowerHalf = c & ~0xF0
            upperHalf = c & ~0x0F
        newR = pix.getRed() | lowerHalf
        newG = pix.getGreen() | (upperHalf >> 4)
        pix = Pixel(newR, newG, pix.getBlue())
        newImage.setPixel(i, height-1, pix)

    return newImage


# reverseStegano function takes an image file as an argument and returns a secret message
# first, the length of the messages is decoded from the very bottom-left corner of the image
# then, each letter of the secret text is decoded from each subsequent pixel in the row
# NOTE: each letter is stored as an int, which is then converted back to a char in the string
# each letter is then added to a string, which is then returned
def reverseStegano(imageFileName):
    # imageFileName = FileImage(imageFileName)
    height = imageFileName.getHeight()
    secret = ''

    pix = imageFileName.getPixel(0, height-1)
    R = pix.getRed() & ~0xF0
    G = pix.getGreen() & ~0xF0
    size = (G << 4) | R

    for i in range(size):
        pix = imageFileName.getPixel(i+1, height-1)
        R = pix.getRed() & ~0xF0
        G = pix.getGreen() & ~0xF0
        c = (G << 4) | R
        secret = secret + chr(c)

    return secret


# demo display function
def Disp(oldImage, newImage):
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Stenography", width * 2, height)
    oldImage.draw(myWin)

    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()


# tests the steganography and reverse steganography functions twice
# include disp function to show how original image remains largely unchanged
def main():
    im1 = 'redEyes1.gif'
    im2 = stegano(im1, 'Hello, World!')
    secret = reverseStegano(im2)
    print(secret)
    Disp(FileImage(im1), im2)

    im3 = 'redEyes2.gif'
    im4 = stegano(im3, 'This is a test of Stenography on redEyes2.gif')
    secret = reverseStegano(im4)
    print(secret)
    Disp(FileImage(im3), im4)

if __name__ == '__main__':
    main()
