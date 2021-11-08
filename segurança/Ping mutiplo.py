import os #IMporta o modulo ou biblioteca OS(Integra os programas e recursos do sistema operacional)
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.slitline()
   
    for ip in dump:
        print('Verificando o ip', ip)
        print('-'*60)
        os.system('ping -n 2{}'.format(ip))
        print('-'*60)
        time.sleep(5)