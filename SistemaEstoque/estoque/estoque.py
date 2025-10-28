class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        """Adiciona um novo produto ao estoque."""
        if nome in self.produtos:
            raise ValueError("Produto já existe no estoque.")
        if preco <= 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser positivos.")
        self.produtos[nome] = {"preco": preco, "quantidade": quantidade}

    def listar_produtos(self):
        """Retorna uma lista com todos os produtos do estoque."""
        return self.produtos

    def atualizar_quantidade(self, nome, nova_qtd):
        """Atualiza a quantidade de um produto existente."""
        if nome not in self.produtos:
            raise ValueError("Produto não encontrado.")
        if nova_qtd < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.produtos[nome]["quantidade"] = nova_qtd

    def remover_produto(self, nome):
        """Remove um produto do estoque."""
        if nome not in self.produtos:
            raise ValueError("Produto não encontrado.")
        del self.produtos[nome]

    def calcular_valor_total(self):
        """Retorna o valor total do estoque."""
        total = 0
        for item in self.produtos.values():
            total += item["preco"] * item["quantidade"]
        return total
