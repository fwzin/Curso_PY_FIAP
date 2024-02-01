#programa 3

nome = input('digite um funcionario: ')
empresa =  input('digite o nome da empresa: ')
qtde_funcionarios = int(input('digite a quantidade de funcionarios: '))
mediaMensalidade = float(input('digite a media de mesalidade: '))

print(nome + 'trabalha na empresa' + empresa)
print('possui: ' ,qtde_funcionarios, 'funcionarios.')
print('a media da mensalidade é de: ' + str(mediaMensalidade))
print('======================Verifique os tipos de dados abaixo======================')
print('o tipo de dado da variavel [nome] é: ',type(nome))
print('o tipo de dado da variavel [empresa] é: ',type(empresa))
print('o tipo de dado da variavel [qtde_funcionarios] é: ',type(qtde_funcionarios))
print('o tipo de dado da variavel [mediaMensalidade] é: ',type(mediaMensalidade))