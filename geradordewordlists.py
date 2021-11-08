import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, 8)

for i in resultado:
    print(''.join(i))