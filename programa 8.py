#programa 8

nome = input('digite o nome do paciente: ')
idade = int(input('digite a idade: '))
doença_infectocontagiosa = input('suspeita de doença infectocontagiosa: ').upper()
if idade >= 65:
    print('o paciente ' + nome + ' possui atendimento prioritario!')
elif doença_infectocontagiosa == 'SIM':
    print('o paciente ' + nome + ' deve ser direcionado para a sala de espera reservada')
else:
    print('o paciente '+ nome + ' não possui atendimento prioritario e pode aguardar em sala comum!')