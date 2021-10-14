# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

# variavel de controle do while
b = 1

# Estrutura de repetição responsavel pela seleção do bloco de operação
while b == 1:

    # variavel de controle de seleção de operações
    a = int(input('Selecione o numero da operação desejada\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão \n '))

    # esse bloco executa a operação de soma
    if a == 1:
        n1 = int(input('Escreva o primeiro numero'))
        n2 = int(input('Escreva o segundo numero'))
        r = n1 + n2
        print('o resultado da soma foi', r)

    # esse bloco executa a operação de subtração
    elif a == 2:
        n1 = int(input('Escreva o primeiro numero'))
        n2 = int(input('Escreva o segundo numero'))
        r = n1 - n2
        print('o resultado da subtração foi', r)

    # esse bloco executa a operação de multiplicação
    elif a == 3:
        n1 = int(input('Escreva o primeiro numero'))
        n2 = int(input('Escreva o segundo numero'))
        r = n1 * n2
        print('o resultado da multiplicação foi', r)

    # esse bloco executa a operação de divisão
    elif a == 4:
        n1 = int(input('Escreva o primeiro numero'))
        n2 = int(input('Escreva o segundo numero'))
        r = n1 / n2
        print('o resultado da divisão foi', r)

    # Mensagem de operação invalida
    else:
        print('essa operação não é vaida')

    # Controle de fluxo do while
    b = int(input('Deseja realizar outra operação\n Se sim, selecione 1\n Se não, selecione 2 \n '))

    # Interrupção do while
    if b == 2:
        break

# Mensagem de agradecimento
print('obrigado por usar os nossos serviços')


