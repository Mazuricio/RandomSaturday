from lerarquivos import ler_imagens, rando_imagens
from editor import Filtro, marca
from notificacao import notificar
from data import escrever, horario
from datetime import datetime
import shutil

def controle():
    agora = datetime.now()
    dia = int(datetime.strftime(agora, '%d'))
    mes = int(datetime.strftime(agora, '%m'))
    hora = int(datetime.strftime(agora, '%H'))
    escrever(mes, dia, hora)


rodar = 3

if horario() == True:
    rodar = 0
else:
    print("o ultimo post foi a menos de 2 horas!!")
    notificar("o ultimo post foi a menos de 2 horas!!")
    rodar = 1


while rodar == 0:
    ##
    print("lendo as imagens")
    pasta = 'imagens'
    #le as imagem
    imagens = ler_imagens(pasta)
    quantas = len(imagens)
    real_quantas = int(quantas) - 1
    print("Temos %s imagens na pasta!" % real_quantas)
    #break
    #Escolhe uma aleatorio
    print("Escolhendo uma aleatoria")
    new_post = rando_imagens(imagens)
    print(new_post)
    mover = new_post
    #Filtro
    print("aplicando Filtro")
    new_post = Filtro(new_post)
    shutil.move(mover, "./utilizadas")
    #Marca
    imagem = marca(new_post)
    # FOI
    print("Edições prontas")
    print("Iniciando postagens!!")
    try:
        print("Postando no twitter")
        from tweet import postar_twiiter
        postar_twiiter()
    except:
        print("Erro ao postar no twitter")
        break
    print("Post no Twiiter feito")
    print("                         ")
    ###########Instagram #########################
    from instagram import postar_instagram
    try:
        print("Postando no Instagram")
        postar_instagram()
    except:
        print("Erro ao postar, tamanho da imagem!!!")
        break
    print("Post no instagram Feito")
    print("                         ")
    ####################### Post IAI BOT #################################

    print("Terminado =)")
    texto =("Temos %s imagens na pasta! \n imagem publicada!!" % quantas)
    notificar(texto)
    controle()
    rodar += 1
