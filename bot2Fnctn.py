from PIL import Image, ImageDraw

def img_size(*img):
    b,h=100000,10000
    for i in img:
        im = Image.open(i)
        b1,h1 =im.size[0],im.size[1]
        b=(b1 if b1<b else b)
        h=(h1 if h1<h else h)
        im.close()
    return (b,h)

def img_size2(img,b,h):
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
    im.paste(im5, (int((w-w1)/2)+20,(int((h-h1)/2)+5)))
    return im

def merge5ellips(im1,im2, im3,im4,im5):
    im=merge4(im1,im2,im3,im4)
    w=im.size[0]
    h=im.size[1]
    w1=im5.size[0]
    h1=im5.size[1]
    point1 = (int((w - w1) / 2), int((h - h1) / 2))
    point2 = (point1[0] + w1, point1[1] + h1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((point1[0]-10, point1[1]-10,point2[0]+10,point2[1]+10), fill='#ffffff')
    mask_in = Image.new("L",im5.size,0)
    draw = ImageDraw.Draw(mask_in)
    draw.ellipse((0,0,w1,h1),fill=255 )
    im.paste(im5,(point1[0],point1[1]), mask_in)
    return im

def merge4diag(im1, im2, im3, im4):

        def img_size(*img):
            im = Image.open(img[1])
            b, h = im.size[0], im.size[1]
            for i in img[2:]:
                im = Image.open(i)
                b1, h1 = im.size[0], im.size[1]
                b = (b if b < b1 else b1)
                h = (h if h < h1 else h1)
                im.close()
            return (b, h)

        def img_size2(img, b, h):
            im = Image.open(img)
            b1, h1 = im.size[0], im.size[1]
            return im.crop(((b1 - b) / 2, (h1 - h) / 2, (b1 - b) / 2 + b, (h1 - h) / 2 + h))

        def mask(b1, h1,p1,p2,p3,p4,p5 ):
            mask = Image.new("L", (b1, h1), '#ffffff')
            draw = ImageDraw.Draw(mask)
            draw.polygon((p1[0],p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1],
                          p5[0], p5[1]), fill='#000000')
            return mask

        b1,h1 = img_size(im1,  im2, im3, im4)
        b, h = int(1.8*b1+10), int(1.8*h1+10)
        im = Image.new("RGBA", (b, h), '#ffffff')
        point1 = (0, int(0.8 * h1))
        point2 = (int(0.9 * b1), int(0.9 * h1))
        point3 = (b1, 0)
        point4 = (b1, h1)
        point5 = (0, h1)
        mask1=mask(b1, h1, point1,point2, point3, point4, point5)
        i1=img_size2(im1,b1,h1)
        im.paste(i1, (0, 0), mask1)
        i1.close()


        point1 = (0, 0)
        point2 = (int(0.2 * b1),0)
        point3 = (int(0.1 * b1), int(0.9 * h1))
        point4 = (b1, h1)
        point5 = (0, h1)
        mask2 = mask(b1, h1, point1, point2, point3, point4, point5)
        i2 = img_size2(im2, b1, h1)
        im.paste(i2, (int(0.8*b1+10),0), mask2)
        i2.close()

        point1 = (0, 0)
        point2 = (b1, 0)
        point3 = (b1, h1)
        point4 = (int(0.8 * b1), h1)
        point5 = (int(0.9 * b1), int(0.1 * h1))
        mask3 = mask(b1, h1, point1, point2, point3, point4, point5)
        i3 = img_size2(im3, b1, h1)
        im.paste(i3, (0, int(0.8 * h1 + 10)), mask3)
        i3.close()

        point1 = (0, 0)
        point2 = (b1, 0)
        point3 = (b1, int(0.2 * h1))
        point4 = (int(0.1 * b1), int(0.1 * h1))
        point5 = (0, h1)
        mask4 = mask(b1, h1, point1, point2, point3, point4, point5)
        i4 = img_size2(im4, b1, h1)
        im.paste(i4, (int(0.8*b1+10), int(0.8 * h1 + 10)), mask4)
        i4.close()
        return im

