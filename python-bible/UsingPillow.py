'''
Created on Apr 20, 2014

Use Pillow for image manipulation
@author: boyerje
'''

from PIL import Image,ImageDraw
def create_image(w,h):
    img=Image.new('RGB',(w,h),(255,255,255))
    draw=ImageDraw.Draw(img)
    draw.line((0,h/2,20,h/2), fill=(255,0,0))
    fp=open('image1.jpg','w')
    img.save(fp, 'JPEG')
    
create_image(200,300)