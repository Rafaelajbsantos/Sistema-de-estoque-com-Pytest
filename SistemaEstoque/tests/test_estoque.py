

import sys
import os
import pytest

# Adiciona a pasta raiz do projeto ao sys.path
# Isso permite que o Python encontre o pacote 'estoque'
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from estoque.estoque import Estoque  # agora deve funcionar


def test_adicionar_produto():
    e = Estoque()
    e.adicionar_produto("Arroz", 10, 5)
    assert "Arroz" in e.produtos

def test_nao_permitir_produto_duplicado():
    e = Estoque()
    e.adicionar_produto("Feijão", 8, 3)
    with pytest.raises(ValueError):
        e.adicionar_produto("Feijão", 8, 3)

def test_atualizar_quantidade():
    e = Estoque()
    e.adicionar_produto("Macarrão", 5, 2)
    e.atualizar_quantidade("Macarrão", 10)
    assert e.produtos["Macarrão"]["quantidade"] == 10

def test_remover_produto():
    e = Estoque()
    e.adicionar_produto("Café", 15, 4)
    e.remover_produto("Café")
    assert "Café" not in e.produtos

def test_calcular_valor_total():
    e = Estoque()
    e.adicionar_produto("Açúcar", 4, 5)
    e.adicionar_produto("Sal", 2, 3)
    assert e.calcular_valor_total() == (4*5 + 2*3)
