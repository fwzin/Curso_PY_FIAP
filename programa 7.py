#programa 7

nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
if idade >= 65:
    print('o paciente ' + nome + ' possui atendimento prioritario!')
else:
    print('o paciente '+ nome + ' não possui atendiemnto prioritario')
