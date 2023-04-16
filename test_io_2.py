arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

print(type(arquivo.buffer))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', 'latin_1') #tem que ser em bytes a escrita do buffer
arquivo.buffer.write(contato)

arquivo.close()