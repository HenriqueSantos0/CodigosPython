import os #IMporta o modulo ou biblioteca OS(Integra os programas e recursos do sistema operacional)

print("#"*60) #Imprimindo o "#" 60 vezes

#Criando uma variavel que recebe do usuraio um Ip
ip_ou_host = input("Digite ip ou host a ser verificado: ")

print("-"*60)#Imprimindo o "-" 60 vezes

#Chamando system da biblioteca OS - comando ping
#-n numero de pacotes que serão 6{}
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-"*60)#Imprimindo o "-" 60 vezes