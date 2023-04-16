# arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')
# mode w limpa o arquivo e escreve sobre ele o novo valor
# mode a faz append no valor anterior

arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')

contato = '11,Priscila,priscila@godoy.com.br\n'

arquivo_contatos.write(contato)