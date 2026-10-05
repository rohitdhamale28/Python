# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:12:37 2023

@author: anilk
"""
#pip install Pillow
# Imports PIL module 
from PIL import Image
  
# open method used to open different extension image file
im = Image.open(r"images/clock.jpg") 
  
# This method will show image in any image viewer 
print(type(im))
im.show() 


from PIL import Image
filename = r"images/clock.jpg"
fname="house.jpg"
with Image.open(fname) as img:
    a=img.load()
    print(type(a))


print(type(img))
print(img.format)
print(img.mode)
print(img.size)

isinstance(img, Image.Image)

img.show()

#to see image details
print(img.format)
#'JPEG'

print(img.size)
#(3989, 2644)

print(img.mode)


#crop the image to some size
#cropped_image = img.crop((left, top, right, bottom))
cropped_img = img.crop((300, 150, 700, 1000))
print(cropped_img.size)
#(400, 850)

cropped_img.show()

#to reduce image size

low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
low_res_img.show()

#similar scaling is possible with reduce function
low_res_img = cropped_img.reduce(4)

# to save the image in the file
cropped_img.save("cropped_image.jpg")
low_res_img.save("low_resolution_cropped_image.png")
low_res_img.show()

#image will appear in inverted way
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()
converted_img = img.transpose(Image.TRANSVERSE)
converted_img.show()
'''
There are seven options that you can pass as arguments to .transpose():

Image.FLIP_LEFT_RIGHT: Flips the image left to right, resulting in a mirror image
Image.FLIP_TOP_BOTTOM: Flips the image top to bottom
Image.ROTATE_90: Rotates the image by 90 degrees counterclockwise
Image.ROTATE_180: Rotates the image by 180 degrees
Image.ROTATE_270: Rotates the image by 270 degrees counterclockwise, which is the same as 90 degrees clockwise
Image.TRANSPOSE: Transposes the rows and columns using the top-left pixel as the origin, with the top-left pixel being the same in the transposed image as in the original image
Image.TRANSVERSE: Transposes the rows and columns using the bottom-left pixel as the origin, with the bottom-left pixel being the one that remains fixed between the original and modified versions
'''
rotated_img = img.rotate(45)
rotated_img.show()

#convert numpy array to image and image to array
from PIL import Image
import numpy as np
im = Image.open('images/clock.jpg')
im2arr = np.array(im) # im2arr.shape: height x width x channel
arr2im = Image.fromarray(im2arr)

#other way to get numpy array
#This can be achieved using the imread() function that 
#loads the image an array of pixels directly and the imshow() 
#function that will display an array of pixels as an image.

#The example below loads and displays the 
#same image using Matplotlib that, in turn, 
#will use Pillow under the covers.

# load and display an image with Matplotlib
from matplotlib import image
import  matplotlib.pyplot as plt
# load image as pixel array
data = image.imread(r'images/clock.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
plt.imshow(data)
plt.show()


#using convert function
#Passing ‘L’ into the pillow convert function converts the 
#image from it’s regular RGB colors to simple black and white 
#(gray-scale).

from PIL import Image

img = Image.open(r"house.jpg")

new_img = img.convert('L')
new_img.show()

#Another mode setting that you can pass it the convert function 
#is ‘1’.
#It adds some kind of “blur” effect onto the image, which adds a 
#unique look to it, which kind of looks nice.

from PIL import Image
 
img = Image.open(r"house.jpg")
 
new_img = img.convert('1')
new_img.show()
'''
Image.split() method is used to split the image into individual bands. This method returns a tuple of individual image bands from an image.
Splitting an “RGB” image creates three new images each containing a
# copy of one of the original bands (red, green, blue).
'''
img1=Image.Image.split(img)
img1[1].show()
 
img1[2].show()


from PIL import Image, ImageDraw, ImagePalette

# Create a new palette image
labels = Image.new('P', (100,100))
labels.save('result.png')
# Push an RGBA palette into it, Red, Green, Blue, 253*Black
labels.putpalette([255,0,0,255, 0,255,0,255, 0,0,255,255, *(253*[0,0,0])], rawmode='RGBA')


# Get a drawing context and draw ellipse using palette entries 0 and 1
#in ellipse first 2 values represents rectangular boundry to draw elipse
drawer = ImageDraw.Draw(labels)
drawer.ellipse([(25,25),(75,75)], fill=1, outline=0)

labels.save('result.png')


from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (230, 200, 126))
draw = ImageDraw.Draw(im)
draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
im.show()
im.save('./pillow_imagedraw.jpg', quality=95)
