"""
API do IBGE
https://servicodados.ibge.gov.br/api/docs/

"""

import requests
import json 

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'ibge.py - https://github.com/leogregianin/ibge',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
}

class Regioes(object):

    def __init__(self, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes'
        request = requests.get(url, headers=headers)
        self.json_ibge = json.loads(request.content.decode('utf-8'))
    
    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return len(self.json_ibge)
        
    def getId(self):
        return [self.json_ibge[i]['id'] for i in range(self.count())]
        
    def getSigla(self):
        return [self.json_ibge[i]['sigla'] for i in range(self.count())]

    def getNome(self):
        return [self.json_ibge[i]['nome'] for i in range(self.count())]


class Estados(object):

    def __init__(self, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        request = requests.get(url, headers=headers)
        self.json_ibge = json.loads(request.content.decode('utf-8'))

    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return len(self.json_ibge)
        
    def getId(self):
        return [self.json_ibge[i]['id'] for i in range(self.count())]

    def getSigla(self):
        return [self.json_ibge[i]['sigla'] for i in range(self.count())]

    def getNome(self):
        return [self.json_ibge[i]['nome'] for i in range(self.count())]


class Municipios(object):

    def __init__(self, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
        request = requests.get(url, headers=headers)
        self.json_ibge = json.loads(request.content.decode('utf-8'))

    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return len(self.json_ibge)
        
    def getId(self):
        return [self.json_ibge[i]['id'] for i in range(self.count())]

    def getNome(self):
        return [self.json_ibge[i]['nome'] for i in range(self.count())]

    def getDescricaoUF(self):
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['nome'] for i in range(self.count())]

    def getSiglaUF(self):
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['sigla'] for i in range(self.count())]

    def getDados(self):
        dados = []
        for i in range(self.count()):
            data = dict()
            data['ibge'] = self.json_ibge[i]['id']
            data['nome'] = self.json_ibge[i]['nome']
            data['uf'] = self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['sigla']
            dados.append(data)
        return dados


class Municipio(object):

    def __init__(self, codigo_ibge=None, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{}'
        request = requests.get(url.format(codigo_ibge), headers=headers)
        self.json_ibge = json.loads(request.content.decode('utf-8'))

    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return int(len(self.json_ibge)/3)
        
    def getId(self):
        return self.json_ibge['id']

    def getNome(self):
        return self.json_ibge['nome']

    def getDescricaoUF(self):
        return self.json_ibge['microrregiao']['mesorregiao']['UF']['nome']

    def getUF(self):
        return self.json_ibge['microrregiao']['mesorregiao']['UF']['sigla']


class MunicipioPorUF(object):

    def __init__(self, codigo_uf=None, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'
        request = requests.get(url.format(codigo_uf), headers=headers)
        self.json_ibge = json.loads(request.content.decode('utf-8'))

    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return len(self.json_ibge)
        
    def getId(self):
        return [self.json_ibge[i]['id'] for i in range(self.count())]

    def getNome(self):
        return [self.json_ibge[i]['nome'] for i in range(self.count())]
