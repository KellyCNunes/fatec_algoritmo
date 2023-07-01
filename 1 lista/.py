class Tipoproduto:
    codigo = 0
    nome = " "
    preco = 0

def main():
    produto = Tipoproduto
    vet_prod = []
    for i in range(5):
        produto.codigo = int(input('digite ocodigo do seu produto: '))
        produto.nome = str(input('digite o nome do seu produto: '))
        produto.preco = float(input('digite o preço do sue produto: '))
        produto.preco = produto.preco + (produto.preco * 10/100)
        print(f'\n o valor do novo produto é: {produto.preco}')

main()