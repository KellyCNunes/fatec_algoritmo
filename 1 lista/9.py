class TipoCliente:
    codigo = 0
    nome = ''
    telefone = ''


class Tipodoc:
    num_doc = 0
    codigo = 0
    dia_venc = 0
    dia_pag = 0
    valor = 0
    juros = 0


def menu():
    print('Menu do sistema: ')
    print('1. CADASTRAR CLIENTES')
    print('2. RELATÓRIO DE CLIENTES')
    print('3. CADASTRAR DOCUMENTOS')
    print('4. RELATÓRIO DE DOCUMENTOS')
    print('5. EXCLUIR CLIENTES SEM DOCUMENTOS')
    print('6. EXCLUIR DOCUMENTOS INDIVIDUAL PELO NÚMERO ')
    print('7. EXCLUIR DOCUMENTOS PELO CLIENTE')
    print('8. EXCLUIR DOCUMENTOS POR PERÍODO')
    print('9. ALTERAR INFORMAÇÕES DOS CLIENTES')
    print('10. MOSTRAR O TOTAL DE DOCUMENTOS POR CLIENTE')
    print('11. SAIR')
    opcao = int(input('Qual opção deseja? '))
    return opcao


def cad_cliente(vet_cliente):  # 1
    if len(vet_cliente) <= 15:
        client = TipoCliente()
        client.codigo = int(
            input("Digite o código do cliente para cadastro: "))
        if encon_cliente(vet_cliente, client.codigo) == False:
            client.nome = input("Digite o nome do cliente para cadastro: ")
            client.telefone = (
                input("Digite o telefone do cliente para cadastro, com (DDD): "))
            vet_cliente.append(client)
        else:
            ('O código do cliente já existe')
    return vet_cliente


def relat_client(vet_cliente):  # 2
    if len(vet_cliente) > 0:
        for i in range(len(vet_cliente)):
            print(
                f"Cliente:{vet_cliente[i].nome} /tCódigo do cliente:{vet_cliente[i].codigo} /tTelefone:{vet_cliente[i].telefone}")
    else:
        print("Cliente não encontrado! ")


def cad_doc(vet_cliente, vet_doc):
    if len(vet_doc) <= 30:
        cod = int(input("Digite o código do cliente para cadastro: "))
        if encon_cliente(vet_cliente, cod) == True:
            doc = Tipodoc()
            doc.codigo = cod
            doc.num_doc = int(input('Digite o número do documento'))
            doc.valor = int(input('Digite o valor'))
            doc.dia_ven = int(input('Digite a data de vencimento'))
            doc.dia_pag = int(input('Digite a data de pagamento'))

            if doc.dia_pag > doc.dia_ven:
                doc.juros = doc.valor * 0.05
                doc.valor = doc.valor + doc.juros
                print(
                    f'Haverá a cobrança no valor de {doc.juros} de juros, totalizando {doc.valor}')
            else:
                doc.juros = 0
            vet_doc.append(doc)
        else:
            print('Não existe cliente com esse código')
    else:
        print('Limite de documentos alcançado')
    return vet_doc


def encon_cliente(vet_cliente, codigo):  # funçãodeverificação
    for i in range(len(vet_cliente)):
        if vet_cliente[i].codigo == codigo:
            return True
    return False


def doc_cliente(codigo, vet_doc):  # funçao de verificaçao
    for i in range(len(vet_doc)):
        if vet_doc[i].codigo == codigo:
            return True
    return False


def rel_doc(d):  # 4
    if len(d) > 0:
        for i in range(len(d)):
            print(
                f"Documento:{d[i].num_doc} /tCódigo do cliente:{d[i].codigo} /tValor:{d[i].valor} /tData de Vencimento:{d[i].dia_ven} /tData de Pagamento:{d[i].dia_pag}")
    # else:
        # print("Documento não encontrado! ")


def excl_client_sem_doc(vet_cliente, vet_doc):  # 5
    for cliente in vet_cliente:
        if not doc_cliente(cliente.codigo, vet_doc):
            vet_cliente.remove(cliente)


def excl_doc_pelo_num(vet_doc):  # 6
    if len(vet_doc) > 0:
        numero = int(input("Digite o número do documento para excluir: "))
        for i in range(len(vet_doc)):
            if numero == vet_doc[i].num_doc:
                indice = i
            vet_doc.pop(indice)
            print("Documento excluído!")
    return vet_doc


def excl_doc_client(vet_cliente, vet_doc):  # 7
    if len(vet_cliente) > 0:
        codigo = int(
            input("Digite o código do cliente que deseja excluir os arquivos: "))
        for i in range(len(vet_doc)):
            if codigo == vet_doc.codigo:
                vet_doc.remove
            print('Documento excluído')
    else:
        print('Cliente não encontrado')
    return vet_doc


def excl_doc_perd(vet_doc):  # 8
    if len(vet_doc) > 0:
        dia = int(input("Digite o primeiro dia: "))
        dia2 = int(input("Digite o segundo dia: "))
        for i in range(len(vet_doc)-1, -1, -1):
            if vet_doc[i].dia_ven < dia or vet_doc[i].dia_ven > dia2:
                indice = i
                vet_doc.pop(indice)
                print("Documento excluido ")
    return vet_doc


def alterar_info_client(vet_cliente):  # 9
    if len(vet_cliente) > 0:
        codigo = int(input('Qual código do cliente que deseja alterar?:  '))
        for i in range(len(vet_cliente)):
            if vet_cliente[i].codigo == codigo:
                vet_cliente[i].nome = input('Digite o novo nome: ')
                vet_cliente[i].telefone = int(
                    input('Digite o novo número de telefone'))
    else:
        print('Cliente não encontrado')
    return vet_cliente


def mostrar_total_doc_client(vet_cliente, vet_doc):  # 10
    if len(vet_cliente) > 0:
        codigo = int(
            input("Digite o código do cliente para visualizar a quantidade de documentos: "))
        for i in range(len(vet_cliente)):
            if vet_cliente[i].codigo == codigo:
                print(f"O cliente tem {len(vet_doc)} documentos cadastrados")
    else:
        print('Esse aluno não está cadastrado')


def main():
    op = menu()
    vet_cliente = []
    vet_doc = []
    while op >= 1 and op <= 10:
        if op == 1:
            vet_cliente = cad_cliente(vet_cliente)

        elif op == 2:
            relat_client(vet_cliente)

        elif op == 3:
            cad_doc(vet_cliente, vet_doc)

        elif op == 4:
            rel_doc(vet_doc)

        elif op == 5:
            excl_client_sem_doc(vet_doc, vet_cliente)

        elif op == 6:
            excl_doc_pelo_num(vet_doc)

        elif op == 7:
            excl_doc_client(vet_cliente, vet_doc)

        elif op == 8:
            excl_doc_perd(vet_doc)

        elif op == 9:
            alterar_info_client(vet_cliente)

        elif op == 10:
            mostrar_total_doc_client(vet_cliente, vet_doc)

        op = menu()


main()
