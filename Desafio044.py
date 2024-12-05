print('-=-'*20, '{:^60}'.format('\n                    == Lojas Playzy´s =='))
print('-=-'*20)
prt = float(input('>>Qual o preço das compras? R$'))
res1 = str(input('''>>Selecione a forma de pagamento: \n[1] Á vista dinheiro/cheque
[2] À vista no cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão\n>>Sua opção: '''))
if res1 == '1':
    print('>>À vista suas compras de R${:.2f} ficaram por R${:.2f} no final.'.format(prt, prt-(prt*0.10)))
elif res1 == '2':
    print('>>No cartão à vista suas compras de R${:.2f} ficaram por R${:.2f} no final.'.format(prt, prt - (prt * 0.05)))
elif res1 == '3':
    print('>>Em 2x no cartão suas compras ficaram por R${:.2f} no final.'.format(prt))
elif res1 == '4':
    parcel = int(input('>>Em quantas parcelas? '))
    prtcj = prt + (prt*0.20)
    parcelcj = prtcj / parcel
    print('>>Em {}x no cartão as parcelas vão ser de R${} e o total vai ser R${}'.format(parcel, parcelcj, prtcj))
else:
    print('>>Opção inválida, tente novamente.')
