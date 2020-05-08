from django.db import models

# VendasService
#     método: registrarVenda(venda)

# EstoqueService
#     método: removerDoEstoque(produtos)

# Caixa
#     prop: venda {
#         produtos: [produtos]
#         total: () => produtos.reduce(0, (prod, _total) => prod.valor += _total)
#         }
#     }

#     método: concluirVenda() { this.venda.produtos = []}
#     método: adicionarProdutoAVenda(produto)
#     método: finalizarVenda(venda) {
#         EstoqueService.removerDoEstoque(venda.produtos)
#         VendasService.registrarVenda(venda)
#         concluirVenda();
#     }
