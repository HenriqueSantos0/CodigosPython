#def carro1(velocidade):
    #trajeto = 0
    #while trajeto <=100:
        #print('Carro1: ', trajeto)
        #trajeto+=velocidade
        
        
#def carro2(velocidade):
    #trajeto = 0
    #while trajeto <=100:
        #print('Carro2: ', trajeto)
        #trajeto+=velocidade       
        
#carro1(10)
#carro2(20)
#Nesse exemplo primeiro exxecuta o carro1 para depois executar o carro2, ou seja, as funções não ocorrem simultanemante.


from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <=100:
        print('Carro: ', piloto , trajeto)
        trajeto+=velocidade
        tim.sleep(0.5)
        print('Piloto: {} km: {}\n'.format(ppiloto, trajeto)

t_carro1 = Thread(target=carro, args=velocidade[1, 'Lucas'])
t_carro2 = Thread(target=carro, args=velocidade[2, 'Henrique'])

t_carro1.start()
t_carro2.start()

#serve para criar um teste de stress ou scan simultaneo, e serve para enviar varias mensagens ao mesmo tmpo

