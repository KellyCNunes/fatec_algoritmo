class Tipoaluno:
    nome =''
    data_nasc = 0
    tel = 0
    end = ""
    serie = 0

def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR')
    print('2. CONSULTAR')
    print('3. VISUALIZAR')
    print('4. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao

def cadastrar(vet_aluno):
    for i in range(2):
        p = Tipoaluno()
        p.data_nasc = int(input('Informe a data de nascimento do estudantes: '))
        p.nome = input('Informe o nome do estudante: ')
        p.tel = int(input('Informe o telefone: '))
        p.end = input('Informe o endereço do estudante: ')
        p.serie = int(input('Informe a série do estudante: '))
        vet_aluno.append(p)
    return vet_aluno

def consulta(vet_aluno):
    if len(vet_aluno) > 0: 
        nome_pesquisa = input('Qual nome que deseja encontrar? ')
        for p in vet_aluno:
            if nome_pesquisa.lower() in p.nome.lower():    #letra minuscula
                print(f'Nome do aluno: {p.nome} \tData de nascimento: {p.data_nasc} \tTelefone: {p.tel} \tEndereço: {p.end} \tSérie: {p.serie}')

        else:
            print('não há nunhum aluno com esse nome cadastrado')
    
    else: 
        print("Aluno não cadastrado cadastrados")

def visualizar(vet_aluno):
    if len(vet_aluno)>0:
        for i in range(len(vet_aluno)):
            print(f'Nome: {vet_aluno[i].nome} \tData de nascimento: {vet_aluno[i].data_nasc} \tTelefone:  {vet_aluno[i].tel} \tEndereço: {vet_aluno[i].end} \tSérie: {vet_aluno[i].serie}')
    else:
        print('Esse aluno não está cadastrado')



def main():
    op = menu()
    vet_aluno=[]
    while op >= 1 and op <= 3:
        if op == 1:
            vet_aluno = cadastrar(vet_aluno)

        elif op == 2:
            consulta(vet_aluno)

        elif op == 3:
            visualizar(vet_aluno)

        op = menu()
        
    

main()