from PIL import Image, ImageEnhance, ImageFilter
import os
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).save('dog1edited.jpg')

img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited.jpg')
