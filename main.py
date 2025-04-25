lista_alunos = []
total_alunos = int(input('digite a quantidade de alunos que são inseridos aqui:'))

for i in range (total_alunos):
    nome = str(input('Nome:'))
    t1 = float(input('T1: '))
    t2 = float(input('T2: '))
    p1 = float(input('P1: '))
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