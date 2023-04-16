arquivo_contatos = open('dados/contatos-escrita-2.csv', encoding='latin_1', mode='w')

contatos = [
    '11,Priscila,priscila@priscila.com.br\n',
    '12,Larissa,larissa@larissa.com.br\n',
    '13,Marcia,marcia@marcia.com.br\n',
    '14,Felipe,felipe@felipe.com.br\n'
]

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()
arquivo_contatos.seek(0) #ponteiro do último vai pra posicao 0 de caracter

for linha in arquivo_contatos:
    print(linha)