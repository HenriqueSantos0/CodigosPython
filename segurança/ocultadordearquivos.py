import ctypes

atributo_ocultar = 0x02

#tambem é possivel ocultar pastas
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', aatributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('arquivo não foi ocultado')