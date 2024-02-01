#programa 11

nome = input('digite o nome do paciente: ')
idade = int(input('digite a idade: '))
doença_infectocontagiosa = input('suspeita de doença infectocontagiosa: ').upper()

if doença_infectocontagiosa == 'SIM':
    print('encaminhe o paciente para a sala amarela')
elif doença_infectocontagiosa == 'NÃO' or 'NAO':
    print('encaminhe o paciente para a sala branca')
else:
    print('responda corretamente a suspeita de doença infectocontagiosa com SIM ou NÃO')

if idade >= 65:
    print('paciente com prioridade')
else:
    genero = input('digite o sexo do paciente: ').upper()
    if genero == 'FEMININO' and idade > 10:
        gravidez = input('a paciente está gravida?').upper()
        if gravidez == 'SIM':
            print('paciente com prioridade')
        else:
            print('paciente sem prioridade')
    else:
        print('paciente sem prioridade')

