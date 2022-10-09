
import csv

with open('dados.txt', encoding='utf-8') as arquivo_referencia:

  tabela = csv.reader(arquivo_referencia, delimiter=',')

  for l in tabela:
    id_autor = l[0]
    nome = l[1]
    mensagem = l[2]

    print(id_autor, nome , mensagem) 





