# ibge
Data collection of geographical divisions of Brazil by IBGE (https://servicodados.ibge.gov.br/api/docs).

Coleta de dados das divisões geográficas do Brasil feita pelo IBGE (https://servicodados.ibge.gov.br/api/docs).

# Install

```bash
$ pip install -r requirements.txt
```


# Como usar


## Regiões

```python
from ibge import *
ibge = Regioes()
```

#### count() - number datatype
```python
ibge.count())
5
```

#### json() - array of objects datatype
```python
ibge.json()
[{'id': 1, 'sigla': 'N', 'nome': 'Norte'}, {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}, {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}, {'id': 4, 'sigla': 'S', 'nome': 'Sul'}, {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}]
```

#### getId() - array datatype
```python
ibge.getId()
[1, 2, 3, 4, 5]
```

#### getSigla() - array datatype
```python
ibge.getSigla()
['N', 'NE', 'SE', 'S', 'CO']
```

#### getNome() - array datatype
```python
ibge.getNome()
['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
```


## Estados

```python
from ibge import *
ibge = Estados()
```

#### count() - number datatype
```python
ibge.count()
27
```

#### json() - array of objects datatype
```python
ibge.json()
[{'id': 11, 'sigla': 'RO', 'nome': 'Rondônia', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 12, 'sigla': 'AC', 'nome': 'Acre', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 13, 'sigla': 'AM', 'nome': 'Amazonas', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 15, 'sigla': 'PA', 'nome': 'Pará', 'regiao':{'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 17, 'sigla': 'TO', 'nome': 'Tocantins', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 21, 'sigla': 'MA', 'nome': 'Maranhão', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 22, 'sigla': 'PI', 'nome': 'Piauí', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 23, 'sigla': 'CE', 'nome': 'Ceará', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 24, 'sigla': 'RN', 'nome': 'Rio Grande do Norte', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 25, 'sigla': 'PB', 'nome': 'Paraíba', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 26, 'sigla': 'PE', 'nome': 'Pernambuco', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 27, 'sigla': 'AL', 'nome': 'Alagoas', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 28, 'sigla': 'SE', 'nome': 'Sergipe', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 29, 'sigla': 'BA', 'nome': 'Bahia', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 31, 'sigla': 'MG', 'nome': 'Minas Gerais', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 32, 'sigla': 'ES', 'nome': 'Espírito Santo', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 33, 'sigla': 'RJ', 'nome': 'Rio de Janeiro', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 35, 'sigla': 'SP', 'nome': 'São Paulo', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 41, 'sigla': 'PR', 'nome': 'Paraná', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 42, 'sigla': 'SC', 'nome': 'Santa Catarina', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 43, 'sigla': 'RS', 'nome': 'Rio Grande do Sul', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 50, 'sigla': 'MS', 'nome': 'Mato Grosso do Sul', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 51, 'sigla': 'MT', 'nome': 'Mato Grosso', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 53, 'sigla': 'DF', 'nome': 'Distrito Federal', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}]
```

#### getId() - array datatype
```python
ibge.getId()
[11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]
```

#### getSigla() - array datatype
```python
ibge.getSigla()
['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']
```

#### getNome() - array datatype
```python
ibge.getNome()
['Rondônia', 'Acre', 'Amazonas', 'Roraima', 'Pará', 'Amapá', 'Tocantins', 'Maranhão', 'Piauí', 'Ceará', 'Rio Grande do Norte', 'Paraíba', 'Pernambuco', 'Alagoas', 'Sergipe', 'Bahia', 'Minas Gerais', 'Espírito Santo', 'Rio de Janeiro', 'São Paulo', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul', 'Mato Grosso do Sul', 'Mato Grosso', 'Goiás', 'Distrito Federal']
```


## Municípios

```python
from ibge import *
ibge = Municipios()
```

#### count() - number datatype
```python
ibge.count()
5570
```

#### json() - array of objects datatype
```python
ibge.json()

(...)
[{'id': 5221858, 'nome': 'Valparaíso de Goiás', 'microrregiao': {'id': 52012, 'nome': 'Entorno de Brasília', 'mesorregiao': {'id': 5204, 'nome': 'Leste Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5221908, 'nome': 'Varjão', 'microrregiao': {'id': 52014, 'nome': 'Vale do Rio dos Bois', 'mesorregiao': {'id': 5205, 'nome': 'Sul Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5222005, 'nome': 'Vianópolis', 'microrregiao': {'id': 52016, 'nome': 'Pires do Rio', 'mesorregiao': {'id': 5205, 'nome': 'Sul Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5222054, 'nome': 'Vicentinópolis', 'microrregiao': {'id': 52015, 'nome': 'Meia Ponte', 'mesorregiao': {'id': 5205, 'nome': 'Sul Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5222203, 'nome': 'Vila Boa', 'microrregiao': {'id': 52012, 'nome': 'Entorno de Brasília', 'mesorregiao': {'id': 5204, 'nome': 'Leste Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5222302, 'nome': 'Vila Propício', 'microrregiao': {'id': 52012, 'nome': 'Entorno de Brasília', 'mesorregiao': {'id': 5204, 'nome': 'Leste Goiano', 'UF': {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}, {'id': 5300108, 'nome': 'Brasília', 'microrregiao': {'id': 53001, 'nome':'Brasília', 'mesorregiao': {'id': 5301, 'nome': 'Distrito Federal', 'UF': {'id': 53, 'sigla': 'DF', 'nome': 'Distrito Federal', 'regiao': {'id': 5,
'sigla': 'CO', 'nome': 'Centro-Oeste'}}}}}]
```

#### getId() - array datatype
```python
ibge.getId()

(...)
[5210000, 5210109, 5210158, 5210208, 5210307, 5210406, 5210562, 5210604, 5210802, 5210901, 5211008,
5211206, 5211305, 5211404, 5211503, 5211602, 5211701, 5211800, 5211909, 5212006, 5212055, 5212105, 5212204, 5212253, 5212303, 5212501, 5212600, 5212709, 5212808, 5212907, 5212956, 5213004, 5213053, 5213087, 5213103, 5213400, 5213509, 5213707, 5213756, 5213772, 5213806, 5213855, 5213905, 5214002, 5214051, 5214101, 5214408, 5214507, 5214606, 5214705, 5214804, 5214838, 5214861, 5214879, 5214903, 5215009, 5215207, 5215231, 5215256, 5215306, 5215405, 5215504, 5215603, 5215652, 5215702, 5215801, 5215900, 5216007, 5216304, 5216403, 5216452, 5216809, 5216908, 5217104, 5217203, 5217302, 5217401, 5217609, 5217708, 5218003, 5218052, 5218102, 5218300, 5218391, 5218508, 5218607, 5218706, 5218789, 5218805, 5218904, 5219001, 5219100, 5219209, 5219258, 5219308, 5219357, 5219407, 5219456, 5219506, 5219605, 5219704, 5219712, 5219738, 5219753, 5219803, 5219902, 5220009, 5220058, 5220108, 5220157, 5220207, 5220264, 5220280, 5220405, 5220454, 5220504, 5220603, 5220686, 5220702, 5221007, 5221080, 5221197, 5221304, 5221403, 5221452, 5221502, 5221551, 5221577, 5221601, 5221700, 5221809, 5221858, 5221908, 5222005, 5222054, 5222203, 5222302, 5300108]
```

#### getNome() - array datatype
```python
ibge.getNome()

(...)
['Nova Crixás', 'Nova Glória', 'Nova Iguaçu de Goiás', 'Nova Roma', 'Nova Veneza', 'Novo Brasil', 'Novo Gama', 'Novo Planalto', 'Orizona', 'Ouro Verde de Goiás', 'Ouvidor', 'Padre Bernardo', 'Palestina de Goiás', 'Palmeiras de Goiás', 'Palmelo', 'Palminópolis', 'Panamá', 'Paranaiguara', 'Paraúna', 'Perolândia', 'Petrolina de Goiás', 'Pilar de Goiás', 'Piracanjuba', 'Piranhas', 'Pirenópolis', 'Pires do Rio', 'Planaltina', 'Pontalina', 'Porangatu', 'Porteirão', 'Portelândia', 'Posse', 'Professor Jamil', 'Quirinópolis', 'Rialma', 'Rianápolis', 'Rio Quente', 'Rio Verde', 'Rubiataba', 'Sanclerlândia', 'Santa Bárbara de Goiás', 'Santa Cruz de Goiás', 'Santa Fé de Goiás', 'Santa Helena de Goiás', 'Santa Isabel', 'Santa Rita do Araguaia', 'Santa Rita do Novo Destino', 'Santa Rosa de Goiás', 'Santa Tereza de Goiás', 'Santa Terezinha de Goiás', 'Santo Antônio da Barra', 'Santo Antônio de Goiás', 'Santo Antônio do Descoberto', 'São Domingos', 'São Francisco de Goiás', "São João d'Aliança", 'São João da Paraúna', 'São Luís de Montes Belos', 'São Luiz do Norte', 'São Miguel do Araguaia', 'São Miguel do Passa Quatro', 'São Patrício', 'São Simão', 'Senador Canedo', 'Serranópolis', 'Silvânia', 'Simolândia', "Sítio d'Abadia", 'Taquaral de Goiás', 'Teresina de Goiás', 'Terezópolis de Goiás', 'Três Ranchos', 'Trindade', 'Trombas', 'Turvânia', 'Turvelândia', 'Uirapuru', 'Uruaçu', 'Uruana', 'Urutaí', 'Valparaíso de Goiás', 'Varjão', 'Vianópolis', 'Vicentinópolis', 'Vila Boa', 'Vila Propício', 'Brasília']

```

#### getDescricaoUF() - string datatype
```python
ibge.getDescricaoUF()

(...)
```

#### getDados() - object datatype
```python
ibge.getDados()

(...)
[{'ibge': 5220108, 'nome': 'São Luís de Montes Belos', 'uf': 'GO'}, {'ibge': 5220157, 'nome': 'São Luiz do Norte', 'uf': 'GO'}, {'ibge': 5220207, 'nome': 'São Miguel do Araguaia', 'uf': 'GO'}, {'ibge': 5220264, 'nome': 'São Miguel do Passa Quatro', 'uf': 'GO'}, {'ibge': 5220280, 'nome': 'São Patrício', 'uf': 'GO'}, {'ibge': 5220405, 'nome': 'São Simão', 'uf': 'GO'}, {'ibge': 5220454, 'nome': 'Senador Canedo', 'uf': 'GO'}, {'ibge': 5220504, 'nome': 'Serranópolis', 'uf': 'GO'}, {'ibge': 5220603, 'nome': 'Silvânia', 'uf': 'GO'}, {'ibge': 5220686, 'nome': 'Simolândia', 'uf': 'GO'},{'ibge': 5220702, 'nome': "Sítio d'Abadia", 'uf': 'GO'}, {'ibge': 5221007, 'nome': 'Taquaral de Goiás', 'uf': 'GO'}, {'ibge': 5221080, 'nome': 'Teresina de Goiás', 'uf': 'GO'}, {'ibge': 5221197, 'nome': 'Terezópolis de Goiás', 'uf': 'GO'}, {'ibge': 5221304, 'nome': 'Três Ranchos', 'uf': 'GO'}, {'ibge': 5221403, 'nome': 'Trindade', 'uf': 'GO'}, {'ibge': 5221452, 'nome': 'Trombas', 'uf': 'GO'}, {'ibge': 5221502, 'nome': 'Turvânia', 'uf': 'GO'}, {'ibge': 5221551, 'nome': 'Turvelândia', 'uf': 'GO'}, {'ibge': 5221577, 'nome': 'Uirapuru', 'uf': 'GO'}, {'ibge': 5221601, 'nome': 'Uruaçu', 'uf': 'GO'}, {'ibge': 5221700, 'nome': 'Uruana', 'uf': 'GO'}, {'ibge': 5221809, 'nome': 'Urutaí', 'uf': 'GO'}, {'ibge': 5221858, 'nome': 'Valparaíso deGoiás', 'uf': 'GO'}, {'ibge': 5221908, 'nome': 'Varjão', 'uf': 'GO'}, {'ibge': 5222005, 'nome': 'Vianópolis', 'uf': 'GO'}, {'ibge': 5222054, 'nome': 'Vicentinópolis', 'uf': 'GO'}, {'ibge': 5222203, 'nome': 'Vila Boa', 'uf': 'GO'}, {'ibge': 5222302, 'nome': 'Vila Propício', 'uf': 'GO'}, {'ibge':5300108, 'nome': 'Brasília', 'uf': 'DF'}]
```


## Município específico

```python
from ibge import *
ibge = Municipio('3302106')
```

#### count() - number datatype
```python
ibge.count()
1
```

#### json() - array of objects datatype
```python
ibge.json()
{'id': 3302106, 'nome': 'Itaocara', 'microrregiao': {'id': 33002, 'nome': 'Santo Antônio de Pádua', 'mesorregiao': {'id': 3301, 'nome': 'Noroeste Fluminense', 'UF': {'id': 33, 'sigla': 'RJ', 'nome': 'Rio de Janeiro', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}}}}
```

#### getNome() - array datatype
```python
ibge.getNome()
Itaocara
```

#### getId() - array datatype
```python
ibge.getId())
3302106
```

#### getUF() - string datatype
```python
ibge.getUF()
RJ
```

#### getDescricaoUF() - string datatype
```python
ibge.getDescricaoUF()
Rio de Janeiro
```


## Municípios por UF

```python
from ibge import *
ibge = MunicipioPorUF('14')
```

#### count() - number datatype
```python
ibge.count()
15
```

#### json() - array of objects datatype
```python
ibge.json()

[{'id': 1400027, 'nome': 'Amajari', 'microrregiao': {'id': 14001, 'nome': 'Boa Vista', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400050, 'nome': 'Alto Alegre', 'microrregiao': {'id': 14001, 'nome': 'Boa Vista', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400100, 'nome': 'Boa Vista', 'microrregiao': {'id': 14001, 'nome': 'Boa Vista', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome':'Norte'}}}}}, {'id': 1400159, 'nome': 'Bonfim', 'microrregiao': {'id': 14002, 'nome': 'Nordeste de Roraima', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400175, 'nome':'Cantá', 'microrregiao': {'id': 14002, 'nome': 'Nordeste de Roraima', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400209, 'nome': 'Caracaraí', 'microrregiao': {'id': 14003, 'nome': 'Caracaraí', 'mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400233, 'nome': 'Caroebe', 'microrregiao': {'id': 14004, 'nome': 'Sudeste de Roraima', 'mesorregiao':{'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400282, 'nome': 'Iracema', 'microrregiao': {'id': 14003, 'nome': 'Caracaraí', 'mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400308, 'nome': 'Mucajaí', 'microrregiao':{'id': 14003, 'nome': 'Caracaraí', 'mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400407, 'nome': 'Normandia', 'microrregiao': {'id': 14002, 'nome': 'Nordeste de Roraima', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400456, 'nome': 'Pacaraima', 'microrregiao': {'id': 14001, 'nome': 'Boa Vista', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400472, 'nome': 'Rorainópolis', 'microrregiao': {'id': 14004, 'nome': 'Sudeste de Roraima', 'mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla':'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400506, 'nome': 'São João da Baliza', 'microrregiao': {'id': 14004, 'nome': 'Sudeste de Roraima', 'mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400605, 'nome': 'São Luiz', 'microrregiao': {'id': 14004, 'nome': 'Sudeste de Roraima','mesorregiao': {'id': 1402, 'nome': 'Sul de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1400704, 'nome': 'Uiramutã', 'microrregiao': {'id': 14002, 'nome': 'Nordeste de Roraima', 'mesorregiao': {'id': 1401, 'nome': 'Norte de Roraima', 'UF': {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}]
```

```python
ibge.getId()
[1400027, 1400050, 1400100, 1400159, 1400175, 1400209, 1400233, 1400282, 1400308, 1400407, 1400456, 1400472, 1400506, 1400605, 1400704]
```

#### getNome() - array datatype
```python
ibge.getNome()
['Amajari', 'Alto Alegre', 'Boa Vista', 'Bonfim', 'Cantá', 'Caracaraí', 'Caroebe', 'Iracema', 'Mucajaí', 'Normandia', 'Pacaraima', 'Rorainópolis', 'São João da Baliza', 'São Luiz', 'Uiramutã']
```

# Licença
IBGE - https://servicodados.ibge.gov.br/api/docs


