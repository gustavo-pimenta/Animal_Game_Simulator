import random
from random import randint

def sorteio(): # get the random result of the game
    num1 = random.randint(0,9999)
    num2 = random.randint(0,9999)
    num3 = random.randint(0,9999)
    num4 = random.randint(0,9999)
    num5 = random.randint(0,9999)

    num1 = str(num1).zfill(4)
    result1 = num1
    result1 = str(result1[2]+result1[3])

    num2 = str(num2).zfill(4)
    result2 = num2
    result2 = str(result2[2]+result2[3])

    num3 = str(num3).zfill(4)
    result3 = num3
    result3 = str(result3[2]+result3[3])

    num4 = str(num4).zfill(4)
    result4 = num4
    result4 = str(result4[2]+result4[3])
    
    num5 = str(num5).zfill(4)
    result5 = num5
    result5 = str(result5[2]+result5[3])

    return num1, num2, num3, num4, num5, result1, result2, result3, result4, result5
    
def sorteio2():

    moderno = 0
    rio = 1
    salteado = 0
    sorteio = []

    # Gerador Dos Numeros da lista

    i = 0
    while(i < 5):
        sorteio.append(randint(1000, 9999))
        i += 1


    print(sorteio)

    # Moderno
    for numerosL in sorteio:
        moderno += numerosL
    moderno = moderno % 1000
    sorteio.append(moderno)

    # Rio
    rio = (sorteio[0]*sorteio[1])

    if(rio >= 10000000):
        rio = (rio % 1000000)/1000
    else:
        rio = (rio % 100000) / 100
    sorteio.append(int(rio))

    # Salteado
    salteado = (sorteio[0] % 100)*4

    sorteio.append(salteado)

    print(sorteio)







