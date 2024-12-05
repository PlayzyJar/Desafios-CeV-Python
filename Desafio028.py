from random import randint
cores = {'clean': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'anil': '\033[36m'}
print(cores['anil'], '-=-'*20, '\n                    >>Adivinhe o Número<<\n', '-=-'*20, cores['clean']*20)
nome = str(input('>>Olá, qual o seu nome? ')).strip()
print('>>Prazer em conhecê-lo {}{}{} '.format(cores['anil'], nome, cores['clean']))
res1 = str(input('>>Vou pensar num número de 1 à 5 e você tem que adivinhar qual é, ok? ')).strip().lower()
numero = randint(1, 5)
if res1 == 'ok':
    res2 = int(input('>>Hmm... Pronto! \n>>Qual o número que eu pensei? '))
    if res2 == 'nao sei':
        res3 = str(input('>>Quer uma dica chapa? '))
        if res3 == 'quero':
            print('>>O número está entre 1 e 5 ;)')
            res2 = str(input('>>Então, qual foi o número que eu pensei? Tenta a sorte. '))
            if res2 == numero:
                print('{}>>Acertô!{} Tu é bom no chute ein? '.format(cores['verde'], cores['clean']))
            else:
                print('{}>>ERROU!{} Era {}, nem no chute tu acerta cara? '.format(cores['vermelho'], cores['clean'], numero))
        else:
            res2 = str(input('>>Então fale o número chapa: '))
            if res2 == numero:
                print('{}Acertô{} mizeravi'.format(cores['verde'], cores['clean']))
            else:
                print('{}>>ERROOUU!{} O número era {}'.format(cores['vermelho'], cores['clean'], numero))
    else:
        if res2 == numero:
            print('>>Vou resumir em duas palavras, {}PARA BÊNS! Tu Acertou.{}'.format(cores['verde'], cores['clean']))
        else:
            print('{}>>Errou!{} Eu pensei no número {}, triste não é pessoal?'.format(cores['vermelho'], cores['clean'], numero))
else:
    print('>>Então, tchau. Tenha um bom dia! :)')
