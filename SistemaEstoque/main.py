from estoque.estoque import Estoque

def menu():
    estoque = Estoque()

    while True:
        print("\n=== 🛒 Sistema de Estoque ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar quantidade")
        print("4 - Remover produto")
        print("5 - Mostrar valor total em estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome do produto: ")
                preco = float(input("Preço: R$"))
                quantidade = int(input("Quantidade: "))
                estoque.adicionar_produto(nome, preco, quantidade)
                print(f"✅ Produto '{nome}' adicionado!")

            elif opcao == "2":
                produtos = estoque.listar_produtos()
                if produtos:
                    print("\n📦 Produtos no estoque:")
                    for nome, dados in produtos.items():
                        print(f"{nome} - R${dados['preco']:.2f} ({dados['quantidade']} un.)")
                else:
                    print("❌ Nenhum produto cadastrado.")

            elif opcao == "3":
                nome = input("Nome do produto: ")
                nova_qtd = int(input("Nova quantidade: "))
                estoque.atualizar_quantidade(nome, nova_qtd)
                print("🔄 Quantidade atualizada!")

            elif opcao == "4":
                nome = input("Nome do produto: ")
                estoque.remover_produto(nome)
                print("🗑️ Produto removido!")

            elif opcao == "5":
                total = estoque.calcular_valor_total()
                print(f"💰 Valor total em estoque: R${total:.2f}")

            elif opcao == "0":
                print("👋 Saindo do sistema...")
                break

            else:
                print("⚠️ Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()
