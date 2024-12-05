try:
    a = open('Conversa.txt', 'rt')

except:
    print('Deu erro ae ;-;')

else:
    for linha in a:
        print(linha)
