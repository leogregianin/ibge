"""
API do IBGE
https://servicodados.ibge.gov.br/api/docs/

"""

import requests
import json
import urllib3
import ssl

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'ibge.py - https://github.com/leogregianin/ibge',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
}

class HttpUnsafeLegacyRenegotiationAdapter(requests.adapters.HTTPAdapter):
    '''
        Transport adapter" that allows us to accept unsafe legacy renegotiation
        Based on https://github.com/urllib3/urllib3/issues/2653 and
        https://stackoverflow.com/a/71646353
    '''

    def __init__(self, **kwargs):
        self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        # A partir do Python 3.12 será possível utilizar:
        # self.ssl_context.options |= ssl.OP_LEGACY_SERVER_CONNECT
        self.ssl_context.options |= 0x4
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


class Regioes(object):

    def __init__(self):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes'
        with requests.sessions.Session() as session:
            session.mount('https://', HttpUnsafeLegacyRenegotiationAdapter())
            request = session.get(url, headers=headers)
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

    def __init__(self):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        with requests.sessions.Session() as session:
            session.mount('https://', HttpUnsafeLegacyRenegotiationAdapter())
            request = session.get(url, headers=headers)
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

    def __init__(self):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
        with requests.sessions.Session() as session:
            session.mount('https://', HttpUnsafeLegacyRenegotiationAdapter())
            request = session.get(url, headers=headers)
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
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['nome']
                for i in range(self.count())]

    def getSiglaUF(self):
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['sigla']
                for i in range(self.count())]

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

    def __init__(self, codigo_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{}'
        with requests.sessions.Session() as session:
            session.mount('https://', HttpUnsafeLegacyRenegotiationAdapter())
            request = session.get(url.format(codigo_ibge), headers=headers)
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

    def __init__(self, codigo_uf=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'
        with requests.sessions.Session() as session:
            session.mount('https://', HttpUnsafeLegacyRenegotiationAdapter())
            request = session.get(url.format(codigo_uf), headers=headers)
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
