#programa 8

nome = input('digite o nome do paciente: ')
idade = int(input('digite a idade: '))
doença_infectocontagiosa = input('suspeita de doença infectocontagiosa: ').upper()
if idade >= 65 and doença_infectocontagiosa == 'SIM':
    print('o paciente será direcionado para a sala amarela com prioridade')
elif idade < 65 and doença_infectocontagiosa == 'SIM':
    print('o paciente será direcionado para a sala amarela sem prioridade')
elif idade >= 65 and doença_infectocontagiosa == 'NÃO' or 'NAO':
    print('o paciente será direcionado para a sala branca com prioridade')
elif idade < 65 and doença_infectocontagiosa == 'NÃO' or 'NAO':
    print('o paicente será direcionado para a sala branca sem prioridade')
else:
    print('responda corretamente a suspeita de doença infectocontagiosa com SIM ou NÃO')