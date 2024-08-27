from utilitarios import (cadastrar_categoria, cadastrar_transacao, saldo_total)

#categorias
categoria_receitas = cadastrar_categoria("receita")
categoria_contas = cadastrar_categoria("contas")
categoria_lazer = cadastrar_categoria("lazer")
categoria_viagens = cadastrar_categoria("viagens")

#transações
cadastrar_transacao(descricao="salario JAN/2024", valor=1000, categoria=categoria_receitas)
cadastrar_transacao(descricao="ingresso show", valor=-100, categoria=categoria_lazer)
cadastrar_transacao(descricao="conta de luz", valor= -100, categoria=categoria_contas)
cadastrar_transacao(descricao="disney", valor= -400, categoria=categoria_viagens)

total = saldo_total()
print(total)