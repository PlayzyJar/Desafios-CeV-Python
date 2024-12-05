import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31m>>Infelizmente o site "Pudim" não está disponível no momento.\033[m')
else:
    print('\033[32m>>O site "Pudim" foi acessado com sucesso!\033[m')
