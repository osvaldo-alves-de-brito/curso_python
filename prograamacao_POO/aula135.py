# Agregação

class CarrinhoDeCompras():
    def __init__(self):
        self._produtos = [] # protected

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)
        # for produto in produtos:
        #     self._produtos.append(produto)

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())