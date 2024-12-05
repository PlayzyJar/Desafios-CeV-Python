from playsound import playsound

music = str(input('     >>>Player Mp3 by PlayzyCovers<<<\n>>Qual música você quer ouvir? ')).strip().lower()
if music == 'faidherbe squad':
    print('>>Você está ouvindo Faidherbe Squad - ProleteR\n \n                            >>Curta sua música ')
    playsound('Desafio021.mp3')
else:
    print('>>Desculpe, no momento não temos essa música.')
