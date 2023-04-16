import contatos_utils

try:
    # arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

    # for linha in arquivo_contatos:
    #     print(linha, end='')

    contatos = contatos_utils.csv_para_contatos('dados/contatos.csv', 'latin_1')
    contatos_utils.contatos_para_pickle(contatos, 'dados/contatos.pickle')

    #carregando pelo pickle:
    # contatos = contatos_utils.pickle_para_contatos('dados/contatos.pickle')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()