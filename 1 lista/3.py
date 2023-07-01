class Tipoproduto:
    codigo = 0
    nome = " "
    preco = 0

def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. REAJUSTAR')
    print('3. VISUALIZAR')
    print('4. CONSULTA POR NOME')
    print('5. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_pro):
    for i in range(3):
        p = Tipoproduto()
        p.codigo = int(input('Informe o código: '))
        p.nome = input('Informe o nome: ')
        p.preco = float(input('Informe o preço: '))
        vet_prod.append(p)
    return vet_prod

def visualizar(vet_prod):
    if len(vet_prod)>0:
        for i in range(len(vet_prod)):
            print(f'Código: {vet_prod[i].codigo} \tNome: {vet_prod[i].nome} \tPreço:  {vet_prod[i].preco:.2f}')
    else:
        print('Não há produtos cadastrados')

def reajustar(vet_prod):
    if len(vet_prod)>0:
        for i in range(len(vet_prod)):
            vet_prod[i].preco += vet_prod[i].preco * 10/100
        print('Reajuste realizado com sucesso!')

    else:
        print('Não há produtos cadastrados')
    return vet_prod

def consulta_nome(vet_prod):
    if len(vet_prod) > 0: 
        nome_pesquisa = input('Qual nome que encontra? ')
        for prod in vet_prod:
            if nome_pesquisa.lower() in prod.nome.lower():
                print(f'Código: {prod.codigo} \tPreço: {prod.preco:.2f}')
    
    else: 
        print("Não há produtos cadastrados")

def alterar(vet_prod):
    if len(vet_prod) > 0:
        codigo_pesquisa = int(input('Qual código deseja pesquisar? '))
        for i in range(len(vet_prod)):
            if vet_prod[i].codigo == codigo_pesquisa:
    
    return vet_prod

def main():
    op = menu()
    vet_prod = []
    while op >= 1 and op <= 3:
        if op == 1:
            vet_prod = cadastrar(vet_prod)

        elif op == 2:
            reajustar(vet_prod)

        elif op == 3:
            visualizar(vet_prod)

        elif op == 4:
            consulta_nome(vet_prod)

        elif op == 5:
            alterar(vet_prod)

        
        op = menu()

main()