from PIL import Image
def redimencinar(imagem):
    basewidth = 500
    img = Image.open(imagem)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('new_post.jpg', 'JPEG')

#redimencinar('new_post.jpg')
