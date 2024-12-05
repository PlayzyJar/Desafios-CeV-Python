def escreva(msg):
    print('{}={}'.format('\033[1;36m', '\033[m') * len(msg))
    print(msg)
    print('{}={}'.format('\033[1;36m', '\033[m') * len(msg))


escreva(f'{"  >> PlayzyCovers Productions <<  "}')
escreva(f'{"  >> Curso de Python no YouTube <<  "}')
escreva(f'{"  >> Curso em Vídeo <<  "}')
