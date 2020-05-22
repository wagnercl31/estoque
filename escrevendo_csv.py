import csv
with open('fix/produtos.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'produto', 'ncm', 'preco', 'estoque', 'estoque_minimo'
    ])

    rows =[
      ['Abobrinha italiana cx', 1233, 45.00, 50, 10],
      ['Abobrinha italiana Kg', 1234,	3.49, 123, 16],
      ['Abobrinha brasileira cx',	1234, 48.00, 523, 12], 
      ['Abobrinha brasaileira Kg', 1234, 3.99, 123, 10] ,
      ['Abobora sc', 1234, 48.00, 123, 10],
      ['Abobora Kg', 1234, 3.19, 123, 10],
      ['Abobora moranga sc', 1234, 48.00, 123, 10], 
      ['Abobora moranga Kg', 1234, 3.19, 123, 10],
      ['Alho roxo cx', 1234, 135.00, 123, 10],
      ['Alho roxo Kg', 1234, 22.90, 123, 10],
      ['Alho Descascado kg', 1234, 16.00, 123, 10], 
      ['Batata doce cx', 1234, 35.00, 123, 10],
      ['Batata doce Kg', 1234, 2.78, 123, 10],
      ['Beterraba cx', 1234, 58.00, 123, 10],
      ['Beterraba Kg',  1234, 4.98, 123, 10],
      ['Berinjela cx', 1234, 30.00, 123, 10],
      ['Berinjela kg',  1234, 3.98, 123, 10],
      ['Batata bolinha sc', 1234, 150.00, 123, 10],
      ['Batata bolinha Kg', 1234, 4.99, 123, 10],
      ['Batata holandesa sc', 1234, 150.00, 123, 10], 
      ['batata holandesa Kg', 1234, 4.99, 123, 10],
      ['Batata asterix sc', 1234, 180.00, 123, 10],
      ['batata asterix Kg', 1234, 5.9, 123, 10],
      ['Cará cx', 1234, 45.00, 123, 10],
      ['Cará Kg', 1234, 3.69, 123, 10],
      ['Cenoura cx', 1234, 65.00, 123, 10],
      ['Cenoura Kg', 1234, 4.99, 123, 10],
      ['Chuchu cx', 1234, 34.00, 123, 10],
      ['Chuchu Kg', 1234, 2.29, 123, 10],
      ['Cebola sc', 1234, 58.00, 123, 10],
      ['Cebola Kg', 1234, 4.78, 123, 10],
      ['Cebola roxa sc', 1234, 78.00, 123, 10], 
      ['Cebola roxa Kg', 1234, 6.98, 123, 10],
      ['Ervilha torta cx', 1234, 110.00, 123, 10], 
      ['ervilha torta Kg', 1234, 13.00, 123, 10],
      ['Feijão de corda Kg', 1234, 8.00, 123, 10],
      ['Feijão fradinho Kg', 1234, 6.80, 123, 10],
      ['Feijão carioca Kg', 1234, 8.50, 123, 10],
    ]
    csv_writer.writerows(rows)