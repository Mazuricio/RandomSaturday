import re, os, random
pasta = 'imagens'
def ler_imagens(pasta):
    #pasta = 'imagens'
    padrao = "\.(png|jpg|jpeg)$"i
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if re.match(padrao, arq)]
    #print(jpgs)
    #print(len(jpgs))
    if len(jpgs) == 1:
        print("Ultimo Arquivo!!!!!!!!!!!")
    elif len(jpgs) == 0:
        print("Pasta sem imagens!!!!!!")
    return jpgs

def rando_imagens(lista):
    quantos = len(lista)
    if quantos == 0:
        return None
    #print("Temos: %s imagens" %quantos)
    resultado = random.randint(0, quantos-1)
    #print(resultado)
    #print("A sorteada é "+str(resultado)+ ", que correspondente a imagem " + lista[resultado])
    return lista[resultado]

#imagens = ler_imagens(pasta)
#print(imagens)
#print(imagens[14])
#selecionada = rando_imagens(imagens)
#print(selecionada)
#shutil.move(selecionada, "./utilizadas")

