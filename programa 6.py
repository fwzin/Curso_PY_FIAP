#programa 6

nome = input('digite o nome do paciente: ')
idade = int(input('digite a idade: '))
prioridade = 'NÃO'
if idade >= 65:
    prioridade = 'SIM'
print('o paciente  ' + nome + ' possui atendimento prioritario? ' + prioridade)