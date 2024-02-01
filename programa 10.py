#programa 10

nome = input('digite o nome do paciente: ')
idade = int(input('digite a idade: '))
doença_infectocontagiosa = input('suspeita de doença infectocontagiosa: ').upper()
if idade >= 65:
    print('paciente com prioridade')
    if doença_infectocontagiosa == 'SIM':
        print('encaminhe o paciente para a sala amarela')
    elif doença_infectocontagiosa == 'NÃO' or 'NAO':
        print('encaminhe o paciente para a sala branca')
    else:
        print('responda corretamente a suspeita de doença infectocontagiosa com SIM ou NÃO')
else:
    print('paciente sem prioridade')
    if doença_infectocontagiosa == 'SIM':
        print('encaminhe o paciente para a sala amarela')
    elif doença_infectocontagiosa == 'NÃO' or 'NAO':
        print('encaminhe o paciente para a sala branca')
    else:
        print('responda corretamente a suspeita de doença infectocontagiosa com SIM ou NÃO')




