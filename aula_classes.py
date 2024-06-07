class Produto:
    ct = 0
    def __init__(self, nome, valor_compra=0, valor_venda=0, qtd_estoque=0, qtd_minima=0):
        self.nome = nome
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
        Produto.ct += 1
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        if type(novo_nome) == str:
            self.nome = novo_nome
        else:
            print("Dados inconsistentes")
    def get_valor_compra(self):
        return self.valor_compra
    def set_valor_compra(self,novo_valor_compra):
        if type(novo_valor_compra) == int:
            self.valor_compra = novo_valor_compra
        else:
            print("Dados inconsistentes")
    def get_valor_venda(self):
        return self.valor_venda
    def set_valor_venda(self,novo_valor_venda):
        self.valor_venda = novo_valor_venda
    def get_qtd_estoque(self):
        return self.qtd_estoque
    def set_qtd_estoque(self,nova_qtd_estoque):
        if type(nova_qtd_estoque) == int:
            self.qtd_estoque = nova_qtd_estoque
        else:
            print("Dados inconsistentes")
    def get_qtd_minima(self):
        return self.qtd_minima
    def set_qtd_minima(self,nova_qtd_minima):
        self.qtd_minima = nova_qtd_minima
    def __str__(self):
        return f"{self.nome},{self.valor_compra},{self.valor_venda},{self.qtd_estoque},{self.qtd_minima}"
    def lucro(self,lucro):
        lucro = (self.valor_compra - self.valor_venda) * -1
        return lucro
    def atualiza_estoque(self,qtd_vendas):
        self.qtd_estoque = self.qtd_estoque - qtd_vendas
    def repor_produto(self,qtd_produtos):
        self.qtd_estoque = self.qtd_estoque + qtd_produtos
    def alerta_estoque(self):
        if self.qtd_estoque >= self.qtd_minima:
            return False
        else:
            return True
    def maior_qtd(self,produto):
        if self.qtd_estoque > produto:
            return ("O produto tem mais estoque que o outro")
        else:
            return "O produto tem menos estoque que o outro"
    def maior_lucro(self,produto_compra,produto_venda):
        if self.lucro(self.valor_compra) > (produto_compra - produto_venda) * -1:
            return "O produto tem mais lucro que o outro"
        else:
            return "O produto tem menos lucro que o outro"
    def qtd_produtos():
        return Produto.ct
if __name__ == '__main__':
    produto1 = Produto('Guitarra',800,1500,10,2)
    produto2 = Produto('Baixo')
    produto3 = Produto('Bateria',1000,3000)
    produto4 = Produto('Piano','','',1)
    print("produto 1:")
    print(produto1.get_nome())
    print(produto1.get_valor_compra())
    print(produto1.get_valor_venda())
    print(produto1.get_qtd_estoque())
    print(produto1.get_qtd_minima())
    produto1.set_qtd_minima(int(input("Digite a quantidade mínima:")))
    print(produto1.get_qtd_minima())
    print(produto1.__str__())
    print(produto1.lucro(0))
    produto1.atualiza_estoque(3)
    print("Estoque pós venda:",produto1.get_qtd_estoque())
    print(produto1.alerta_estoque())
    print(produto1.maior_qtd(produto4.get_qtd_estoque()))
    print(produto1.maior_lucro(produto2.get_valor_compra(),produto2.get_valor_venda()))

    print("produto 2:")
    print(produto2.get_nome())

    print("produto 3:")
    print(produto3.get_nome())
    print(produto3.get_valor_compra())
    print(produto3.get_valor_venda())

    print("produto 4:")
    print(produto4.get_nome())
    print(produto4.get_qtd_estoque())

    print("Quantidade de produtos cadastrados:",Produto.qtd_produtos())









