class TipoEndereco:       #f.endereco.rua
    rua =''
    num = 0
    bairro = ""
    cidade = ''
class TipoFuncionario:
    nome =''
    codigo = 0
    endereco = TipoEndereco()
    salario = 0

def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. VISUALIZAR')
    print('3. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_fun):
    for i in range(2):
        f = TipoFuncionario()
        f.nome = input('Informe o nome do funcionário: ')
        f.cod = int(input('Informe o código do funcionário: '))
        f.salario = int(input('Informe o salário  do funcionário: '))
        f.endereco.rua = input('Informe o  nome da rua do funcionário: ')
        f.endereco.num = int(input('Informe o número da casa: '))
        f.endereco.bairro = input('Informe o nome do bairro: ')
        f.endereco.cidade = input('Informe o nome da cidade: ')
        vet_conta.append(p)
    return vet_fun

def consulta(vet_fun):
    if len(vet_fun) > 0: 
        nome_pesquisa = input('Qual nome que deseja encontrar? ')
        for p in vet_fun:
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

def main():
    op = menu()
    vet_conta=[]
    vet_fun=[]
    while op >= 1 and op <= 2:
        if op == 1:
            vet_prod = cadastrar(vet_prod)

        elif op == 2:
            visualizar(vet_prod)

        op = menu()


main()