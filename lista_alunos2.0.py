lista_alunos = []
total_alunos = int(input('digite a quantidade de alunos que são inseridos aqui:'))
while total_alunos <=0:
    print('Número invalido! Digite a quantidade correta de alunos')
    total_alunos = int(input('digite a quantidade de alunos que são inseridos aqui:'))

for i in range (total_alunos):
    print(f'\nAluno {i+1}:')
    nome = str(input('Nome:'))
    t1 = float(input('T1: '))
    while t1<0 or t1>10:
        print('Erro! Digite uma nota entre 0 e 10')
        t1 = float(input('T1: '))
    t2 = float(input('T2: '))
    while t2<0 or t2>10:
        print('Erro! Digite uma nota entre 0 e 10')
        t2 = float(input('T2: '))
    p1 = float(input('P1: '))
    while p1<0 or p1>10:
        print('Erro! Digite uma nota entre 0 e 10')
        p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    while p2<0 or p2>10:
        print('Erro! Digite uma nota entre 0 e 10')
        p2 = float(input('P2: '))

    mt = 0.4 * t1 + 0.6 * t2
    mp = (p1 + p2) / 2 

    if mt > 5.0 and mp > 5.0:
        mf = 0.3 * mp + 0.7 * mt 
    else: 
        if mt < mp: 
            mf = mt
        else: 
            mf = mp 
    aluno = [nome, [t1, t2], [p1, p2], [mt, mp], mf]
    lista_alunos.append(aluno)
opcao = 0
while opcao != 6:
    print(f'\nMenu de opções')
    print(f'1.Boletins\n2.Buscar aluno pelo nome\n3.Aluno com maior média final\n4.Aluno com maior média final\n5.Percentual de alunos com MF > 5\n6.Sair')
    opcao = int(input(f'Opção: '))
    if opcao ==1:
        print(f'\nBoletim:')
        for i in range(len(lista_alunos)):
            print(f'Nome:', lista_alunos [i] [0])
            print(f'Média teorica: {lista_alunos[i][3][0]:.2f}')
            print(f'Media pratica: {lista_alunos[i][3][1]:.2f}')
            print(f'Média final: {lista_alunos[i][4]:.2f}')
            print(f'-----')

    elif opcao ==2:
        nome_aluno=input('\nGostaria de ver as informações de qual aluno?')
        for i in range(len(lista_alunos)):
            if lista_alunos[i][0]==nome_aluno:
                print(f'Nome:', lista_alunos [i] [0])
                print(f'Média teorica: {lista_alunos[i][3][0]:.2f}')
                print(f'Media pratica: {lista_alunos[i][3][1]:.2f}')
                print(f'Média final: {lista_alunos[i][4]:.2f}')
                print(f'-----')
            else:
              print('Este aluno não existe')

    elif opcao == 3:
        maior = lista_alunos[0][4]
        nome_maior = lista_alunos[0][0]
        for i in range(len(lista_alunos)):
            if lista_alunos[i][4] > maior:
                maior = lista_alunos[i][4]
                nome_maior = lista_alunos[i][0]
        print(f'\nAluno com maior média final:')
        print(f'Nome: {nome_maior}')
        print(f'Média final: {maior:.2f}')

    elif opcao == 4:
        menor = lista_alunos[0][4]
        nome_menor = lista_alunos[0][0]
        for i in range(len(lista_alunos)):
            if lista_alunos[i][4] < menor:
                menor = lista_alunos[i][4]
                nome_menor = lista_alunos[i][0]
        print(f'\nAluno com menor média final:')
        print(f'Nome: {nome_menor}')
        print(f'Média final: {menor:.2f}')

    elif opcao == 5:
        count = 0
        for i in range(len(lista_alunos)):
            if lista_alunos[i][4] > 5:
                count += 1
        percentual = (count / len(lista_alunos)) * 100
        print(f'\nPercentual de alunos com média final acima de 5: {percentual:.1f}%')


        



