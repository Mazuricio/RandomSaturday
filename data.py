from datetime import datetime
import csv
import os

agora = datetime.now()
dia_n = int(datetime.strftime(agora, '%d'))
mes_n = int(datetime.strftime(agora, '%m'))
hora_n = int(datetime.strftime(agora, '%H'))

## ler 
with open("data.csv", "r") as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for item in leitor:
        if item[0] == "dia":
            dia_v = int(item[1])
        elif item[0] == "mes":
            mes_v = int(item[1])
        elif item[0] == "hora":
            hora_v = int(item[1])

def escrever(mes, dia, hora):
    #escrever 
    os.remove("data.csv")
    with open("data.csv", "a") as arquivo:
        escreve = csv.writer(arquivo, delimiter=",", lineterminator="\n")
        escreve.writerow(["dia", dia])
        escreve.writerow(["mes", mes])
        escreve.writerow(["hora", hora])


#escrever(mes_n, dia_n, hora_n)

def horario():
    if (mes_n - mes_v) != 0:
        #print("mes", mes_n - mes_v)
        return True
    elif (dia_n - dia_v) != 0:
        #print("dia", dia_n - dia_v)
        return True
    elif (hora_n - hora_v) >= 2:
        #print("hora", hora_n - hora_v)
        return True
    else:
        return False
    



#horario()
#print(horario())
#arquivo = open("arquivo.txt", "a")