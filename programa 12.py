#programa 12

nivel = input('digite o nivel de acesso: ').upper()
if nivel == 'ADM' or nivel == 'usr':
    genero = input('digite seu genero: ').upper()
    if nivel == 'ADM':
        if genero == 'FEMININO':
            print('Olá Administradora')
        else:
            print('Olá Administrador')
    else:
        if genero == 'FEMININO':
            print('Olá Usuária')
        else:
            print('Olá Usuário')
elif nivel == 'GUEST':
    print('Olá Visitante')
else:
    print('Olá Desconhecido(a)')