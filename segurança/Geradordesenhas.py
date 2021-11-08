import random
import string

tamanho = int(input('Digite o tamanho de senha que você deseja:'))

chars = string.ascii_letters + string.digts + '!@#$%&*()-=+'

rnd = random.systemRandom() 

print(' '.join(rnd.choice(chars) for i in range(tamanho)))

