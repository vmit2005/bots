from PIL import Image, ImageDraw

def img_size(img):
    im = Image.open(img)
    b1,h1 =im.size[0],im.size[1]
    im.close()
    return (b1,h1)

def img_siz2(img,b,h):
    im = Image.open(img)
    b1,h1 =im.size[0],im.size[1]
    # print((b1-b)/2,(h1-h)/2,(b1-b)/2+b,(h1-h)/2+h)
    return im.crop(((b1-b)/2,(h1-h)/2,(b1-b)/2+b,(h1-h)/2+h))


def merge4(im1, im2, im3, im4):
    w = im1.size[0] + 10 + im2.size[0]
    h = im1.size[1]+10 +im2.size[1]
    im = Image.new("RGBA", (w, h), '#ffffff')
    im.paste(im1)
    im.paste(im2, (im1.size[0] + 10, 0))
    im.paste(im3, (0 , im1.size[1]+10))
    im.paste(im4, (im1.size[0]+10, im1.size[1]+10))
    return im

def merge5(im1,im2, im3,im4,im5):
    im=merge4(im1,im2,im3,im4)
    w=im.size[0]
    h=im.size[1]
    w1=im5.size[0]
    h1=im5.size[1]
    draw=ImageDraw.Draw(im)
    draw.rectangle((10+(w-w1)/2, -10+(h-h1)/2, (w-w1)/2+w1+30, 10+(h-h1)/2+h1+10),fill=(255,255,255))
    im.paste(im5, (int((im1.size[0]+im2.size[0]-im5.size[0])/2+20),(int((im1.size[1]+im2.size[1]-im1.size[1])/2+20))))
    return im





i1=img_size("image1.jpg",400,600)
i2=img_size("image2.jpg",400,600)
i3=img_size("image3.jpg",400,600)
i4=img_size("image1.jpg",400,400)


img=merge5(i1,i3,i3,i2,i4)
img.save('i.png')
img.show()