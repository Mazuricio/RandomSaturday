import os, shutil
def ler_imagens(pasta):
    #pasta = 'imagens'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg") or arq.lower().endswith(".png")  or arq.lower().endswith(".jpeg")]
    #print(jpgs)
    #print(len(jpgs))
    return jpgs

pasta = "utilizadas"
imagens = ler_imagens(pasta)
#print('Movendo Imagens')
for itens in imagens:
    print("Movendo %s" %itens)
    shutil.move(itens, "./imagens")

print("Pronto")