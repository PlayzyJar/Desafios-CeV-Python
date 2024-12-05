from time import sleep


def maior(*nums):
    mai = cont = 0
    print('>>Analizando os valores: ', end='')
    for n, v in enumerate(nums):
        print(f'{v} ', end='')
        if n == 0:
            mai = v
        if v >= mai:
            mai = v
        cont += 1
        sleep(0.5)
    print(f'\n>>Foram informados {cont} valores maior é {mai}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
