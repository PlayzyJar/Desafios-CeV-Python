sexo = str(input('>>Infrome seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MASCULINOFEMININO':
    sexo = str(input('>>Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()
if sexo in 'MASCULINO':
    print('>>Sexo Masculino registrado com succeso!')
elif sexo in 'FEMININO':
    print('>>Sexo Feminino registrado com sucesso!')
