class Tipoconta:
    nome =''
    num = 0
    saldo = 0
   

def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. CONSULTAR')
    print('3. EXCLUIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_conta):
    for i in range(2):
        p = Tipoconta()
        p.nome = input('Informe o nome: ')
        p.num = int(input('Informe o telefone: '))
        p.saldo = int(input('Informe o saldo: '))
        vet_conta.append(p)
    return vet_conta

def consulta(vet_conta):
    if len(vet_conta) > 0: 
        nome_pesquisa = input('Qual nome que deseja encontrar? ')
        for p in vet_conta:
            if nome_pesquisa.lower() in p.nome.lower():    #pega uma estrutura do vetor
                print(f'Nome do aluno: {p.nome} \tNúmero da conta: {p.num} \tSaldo da conta: {p.saldo}')
            else:
                print('não há nunhum aluno com esse nome cadastrado')
    
    else: 
        print("Aluno não cadastrado cadastrados")

def excluir(vet_conta):
    print(len(vet_conta))
    if len(vet_conta) > 0:
        menor_conta = vet_conta[0]
        for conta in vet_conta:
            if conta.saldo < menor_conta.saldo:
                menor_conta = conta
        print(menor_conta.saldo)
        vet_conta.remove(menor_conta)

    return vet_conta


def main():
    op = menu()
    vet_conta=[]
    while op >= 1 and op <= 3:
        if op == 1:
            vet_conta = cadastrar(vet_conta)

        elif op == 2:
            consulta(vet_conta)

        elif op == 3:
            excluir(vet_conta)
        op = menu()
main()