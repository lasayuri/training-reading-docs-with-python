import csv
from contato import Contato

def csv_para_contatos(caminho, encoding):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id = linha[0]
            nome = linha[1]
            email = linha[2]
            # igual a: id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo: #wb para abrir um binario
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(contato['id'], contato['nome'], email=contato['email'])
            #equivale a: c = Contato(**contato)
            contatos.append(c)
    
    return contatos