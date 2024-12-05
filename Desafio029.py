vel = int(input('      >>>Radar de Velocidade<<<\n>>A quantos km/h estava o veículo? '))
if vel <= 80:
    print('>>{}km/h \n>>O veículo está dentro dos limites de velocidade.'.format(vel))
else:
    print('>>{}km/h \n>>Você foi multado em R${}!'.format(vel, (vel-80)*7))
print('>>Tenha um bom dia! Dirija com segurança')
