class TipoValidade:
    dia = 0
    mes = ''
    ano = 0

class TipoFabricacao:
    dia = 0
    mes = ''
    ano = 0

class TipoProduto:
    código = 0
    nome = ''
    data_fabricacao = 0
    data_validade = 0
    preco = 0



def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. VISUALIZAR')
    print('3. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_prod):
    for i in range(2):
        f = TipoProduto()
        f.dia = int(input('Informe a dia: '))
        f.mes = input('Informe o mês: ')
        f.ano = int(input('Informe o ano: '))
        f.data_validade.dia = int(input('Informe o dia de validade: '))
        f.data_validade.mes = int(input('Informe o mês de validade: '))
        f.data_validade.ano = int(input('Informe o ano de validade: '))
        f.data_fabricacao.dia = int(input('Informe o dia de fabricação: '))
        f.data_fabricacao.mes = int(input('Informe o mês de fabricação: '))
        f.data_fabricacao.ano = int(input('Informe o ano de fabricação: '))
        vet_prod.append(p)
    return vet_prod

def visualizar(vet_prod):
    if len(vet_prod)>0:
        for i in range(len(vet_prod)):
            print(f'Código: {vet_prod[i].codigo} \tNome: {vet_prod[i].nome} \tData de fabricação:  {vet_conta[i].data_fabricação} \tData de validade:  {vet_conta[i].data_validade} \tData de preco:  {vet_conta[i].preco}')
    else:
        print('Esse aluno não está cadastrado')


def main():
    op = menu()
    vet_prod=[]
    while op >= 1 and op <= 2:
        if op == 1:
            vet_prod = cadastrar(vet_prod)

        elif op == 2:
            visualizar(vet_prod)

        op = menu()
        
    

main()