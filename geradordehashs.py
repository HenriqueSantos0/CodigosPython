import hashlib

string = input("Digite o texto a ser codificado")

menu= int(input('''### Menu - Escolha o tipo de hash ####
              1) md5
              2) SHA1
              3) SHA2556
              4) SHA512
              Dgite o numero do hash a ser gerado: '''))
if menu==1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O hash MD5 da string é:, ' resultado.hexdigest())
elif menu===2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O hash SHA1 da string é:, ' resultado.hexdigest())
elif menu==3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O hash SHA256 da string é:, ' resultado.hexdigest())
elif menu==4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O hash SHA512 da string é:, ' resultado.hexdigest())
else:
    print('O progrma falhou, confira se o numero pertence ao menu e digite novamente')