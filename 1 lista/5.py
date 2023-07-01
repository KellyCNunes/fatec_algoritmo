class Tipoconta:
    nome =''
    num = 0
    saldo = 0
   

def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. CONSULTAR')
    print('3. VISUALIZAR')
    print('4. ALTERAR')
    print('5. EXCLUIR')
    print('6. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_conta):
    for i in range(2):
        p = Tipoconta()
        p.nome = input('Informe o nome do estudante: ')
        p.num = int(input('Informe o telefone: '))
        p.saldo = int(input('Informe a série do estudante: '))
        vet_conta.append(p)
    return vet_conta

def consulta(vet_conta):
    if len(vet_conta) > 0: 
        nome_pesquisa = input('Qual nome que deseja encontrar? ')
        for p in vet_conta:
            if nome_pesquisa.lower() in p.nome.lower():
                print(f'Nome do aluno: {p.nome} \tNúmero da conta: {p.num} \tSaldo da conta: {p.saldo}')

        else:
            print('não há nunhum aluno com esse nome cadastrado')
    
    else: 
        print("Aluno não cadastrado cadastrados")

def visualizar(vet_conta):
    if len(vet_conta)>0:
        for i in range(len(vet_conta)):
            print(f'Nome: {vet_conta[i].nome} \tNúmero da conta: {vet_conta[i].num} \tSaldo da conta:  {vet_conta[i].saldo}')
    else:
        print('Esse aluno não está cadastrado')
        
def alterar(vet_conta):
    if len(vet_conta) > 0:
        codigo_pesquisa = int(input('Qual código deseja pesquisar? '))
        for i in range(len(vet_conta)):
            if vet_conta[i].codigo == codigo_pesquisa:
    
    return vet_conta

def excluir(vet_conta):
    if len(vet_conta) >  0:
        menor_conta = vet_conta[0].saldo
        indice = 0
            for i in range(len(vet_conta)):
                if vet_conta[i].saldo < menor_conta:
                    menor_conta = vet_conta[i].saldo
                    indice = i
        del vet_conta[indice]
        return vet_conta
    
    else: 
        print('Nenhuma informação encontrada')

    

def main():
    op = menu()
    vet_conta=[]
    while op >= 1 and op <= 3:
        if op == 1:
            vet_conta = cadastrar(vet_conta)

        elif op == 2:
            consulta(vet_conta)

        elif op == 3:
            visualizar(vet_conta)

        elif op == 4:
            alterar(vet_conta)

        elif op == 5:
            excluir(vet_conta)


        op = menu()
        
    

main()