import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/?gl=BR')
except:
    print('\033[31mO site YOUTUBE nao esta disponivel no momento.\033[m')
else:
    print('\033[34mConsegui acessar o site YOUTUBE com sucesso.\033[m')