from PIL import Image, ImageFilter, ImageDraw, ImageFont
from redimencionar import redimencinar
def Filtro(imagem):
    #Le a imagem
    redimencinar(imagem)
    new = "new_post.jpg"
    im = Image.open(new)
    nome_imagem = 'new_post.jpg'
    #redimenciona a imagem
    #Aplica o Filtro
    im_sharp = im.filter( ImageFilter.SHARPEN )
    #img.save('sompic.jpg')
    #Salva a imagem

    im_sharp.save( nome_imagem, 'JPEG' )
    #Splitting the image into its respective bands, i.e. Red, Green,
    #and Blue for RGB
    r,g,b = im_sharp.split()
    #Viewing EXIF data embedded in image
    exif_data = im._getexif()
    exif_data
    #tamanhoimagem = im.size
    return nome_imagem #, tamanhoimagem
def marca(imagem):
    img = Image.open(imagem)
    draw = ImageDraw.Draw(img)
    texto = "@saturdayrandom"
    tamanhotexto = int(15*(img.size[1]/img.size[0]))
    print(tamanhotexto)
    #print(img.size[0])#/img.size[1])
    fnt = ImageFont.truetype('fonte.ttf', tamanhotexto)
    pos = 0,0
    draw.text((pos[0]-0.5, pos[1]-0.5), texto,(0,0,0),font=fnt)
    draw.text((pos[0]+0.5, pos[1]-0.5), texto,(0,0,0),font=fnt)
    draw.text((pos[0]+0.5, pos[1]+0.5), texto,(0,0,0),font=fnt)
    draw.text((pos[0]-0.5, pos[1]+0.5), texto,(0,0,0),font=fnt)
    draw.text(pos, texto, font=fnt, fill=(255,255,255,128))
    img.save(imagem)
#imagem = ler_imagens('imagens')
#print(imagem[0])
#new_imagem = marca('imagem-19.jpg')
#marca(new_imagem)
