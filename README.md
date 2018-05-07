# ibge
Data collection of geographical divisions of Brazil by IBGE (https://servicodados.ibge.gov.br/api/docs).
Coleta de dados das divisões geográficas do Brasil feita pelo IBGE (https://servicodados.ibge.gov.br/api/docs).


# Como usar


## Regiões

```python
from ibge import *
ibge = Regioes()
```

```python
ibge.count())
5
```

```python
ibge.json()
[{'id': 1, 'sigla': 'N', 'nome': 'Norte'}, {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}, {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}, {'id': 4, 'sigla': 'S', 'nome': 'Sul'}, {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}]
```

```python
ibge.getId()
[1, 2, 3, 4, 5]
```

```python
ibge.getSigla()
['N', 'NE', 'SE', 'S', 'CO']
```

```python
ibge.getNome()
['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
```


## Estados

```python
from ibge import *
ibge = Estados()
```

```python
ibge.count()
27
```

```python
ibge.json()
[{'id': 11, 'sigla': 'RO', 'nome': 'Rondônia', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 12, 'sigla': 'AC', 'nome': 'Acre', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 13, 'sigla': 'AM', 'nome': 'Amazonas', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 14, 'sigla': 'RR', 'nome': 'Roraima', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 15, 'sigla': 'PA', 'nome': 'Pará', 'regiao':{'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 17, 'sigla': 'TO', 'nome': 'Tocantins', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}, {'id': 21, 'sigla': 'MA', 'nome': 'Maranhão', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 22, 'sigla': 'PI', 'nome': 'Piauí', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 23, 'sigla': 'CE', 'nome': 'Ceará', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 24, 'sigla': 'RN', 'nome': 'Rio Grande do Norte', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 25, 'sigla': 'PB', 'nome': 'Paraíba', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 26, 'sigla': 'PE', 'nome': 'Pernambuco', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 27, 'sigla': 'AL', 'nome': 'Alagoas', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 28, 'sigla': 'SE', 'nome': 'Sergipe', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 29, 'sigla': 'BA', 'nome': 'Bahia', 'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}}, {'id': 31, 'sigla': 'MG', 'nome': 'Minas Gerais', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 32, 'sigla': 'ES', 'nome': 'Espírito Santo', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 33, 'sigla': 'RJ', 'nome': 'Rio de Janeiro', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 35, 'sigla': 'SP', 'nome': 'São Paulo', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}, {'id': 41, 'sigla': 'PR', 'nome': 'Paraná', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 42, 'sigla': 'SC', 'nome': 'Santa Catarina', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 43, 'sigla': 'RS', 'nome': 'Rio Grande do Sul', 'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}}, {'id': 50, 'sigla': 'MS', 'nome': 'Mato Grosso do Sul', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 51, 'sigla': 'MT', 'nome': 'Mato Grosso', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 52, 'sigla': 'GO', 'nome': 'Goiás', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}, {'id': 53, 'sigla': 'DF', 'nome': 'Distrito Federal', 'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}]
```

```python
ibge.getId()
[11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]
```

```python
ibge.getSigla()
['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']
```

```python
ibge.getNome()
['Rondônia', 'Acre', 'Amazonas', 'Roraima', 'Pará', 'Amapá', 'Tocantins', 'Maranhão', 'Piauí', 'Ceará', 'Rio Grande do Norte', 'Paraíba', 'Pernambuco', 'Alagoas', 'Sergipe', 'Bahia', 'Minas Gerais', 'Espírito Santo', 'Rio de Janeiro', 'São Paulo', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul', 'Mato Grosso do Sul', 'Mato Grosso', 'Goiás', 'Distrito Federal']
```


## Municípios

```python
from ibge import *
ibge = Municipios()
```

```python
ibge.count()
5570
```

```python
ibge.json()
ibge.getNome()
ibge.getId()
ibge.getDescricaoUF()
ibge.getDados()
```


## Município específico

```python
from ibge import *
ibge = Municipio('3302106')
```

```python
ibge.count()
1
```

```python
ibge.json()
{'id': 3302106, 'nome': 'Itaocara', 'microrregiao': {'id': 33002, 'nome': 'Santo Antônio de Pádua', 'mesorregiao': {'id': 3301, 'nome': 'Noroeste Fluminense', 'UF': {'id': 33, 'sigla': 'RJ', 'nome': 'Rio de Janeiro', 'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}}}}}
```

```python
ibge.getNome()
Itaocara
```

```python
ibge.getId())
3302106
```

```python
ibge.getUF()
RJ
```

```python
ibge.getDescricaoUF()
Rio de Janeiro
```


## Municípios por UF

```python
from ibge import *
ibge = MunicipioPorUF('16')
```

```python
ibge.count()
16
```

```python
ibge.json()
[{'id': 1600055, 'nome': 'Serra do Navio', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600105, 'nome': 'Amapá', 'microrregiao': {'id': 16002, 'nome': 'Amapá', 'mesorregiao': {'id': 1601, 'nome': 'Norte do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600154, 'nome': 'Pedra Branca do Amapari', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600204, 'nome': 'Calçoene', 'microrregiao': {'id': 16001, 'nome': 'Oiapoque', 'mesorregiao': {'id': 1601, 'nome': 'Norte do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600212, 'nome': 'Cutias', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600238, 'nome': 'Ferreira Gomes', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600253, 'nome': 'Itaubal', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600279, 'nome': 'Laranjal do Jari', 'microrregiao': {'id': 16004, 'nome': 'Mazagão', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600303, 'nome': 'Macapá', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600402, 'nome': 'Mazagão', 'microrregiao': {'id': 16004, 'nome': 'Mazagão', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600501, 'nome': 'Oiapoque', 'microrregiao': {'id': 16001, 'nome': 'Oiapoque', 'mesorregiao': {'id': 1601, 'nome': 'Norte do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600535, 'nome': 'Porto Grande', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600550, 'nome': 'Pracuúba', 'microrregiao': {'id': 16002, 'nome': 'Amapá', 'mesorregiao': {'id': 1601, 'nome': 'Norte do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600600, 'nome': 'Santana', 'microrregiao': {'id': 16003, 'nome': 'Macapá', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600709, 'nome': 'Tartarugalzinho', 'microrregiao': {'id': 16002, 'nome': 'Amapá', 'mesorregiao': {'id': 1601, 'nome': 'Norte do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}, {'id': 1600808, 'nome': 'Vitória do Jari', 'microrregiao': {'id': 16004, 'nome': 'Mazagão', 'mesorregiao': {'id': 1602, 'nome': 'Sul do Amapá', 'UF': {'id': 16, 'sigla': 'AP', 'nome': 'Amapá', 'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}}}}}]
```

```python
ibge.getId()
[1600055, 1600105, 1600154, 1600204, 1600212, 1600238, 1600253, 1600279, 1600303, 1600402, 1600501, 1600535, 1600550, 1600600, 1600709, 1600808]
```

```python
ibge.getNome()
['Serra do Navio', 'Amapá', 'Pedra Branca do Amapari', 'Calçoene', 'Cutias', 'Ferreira Gomes', 'Itaubal', 'Laranjal do Jari', 'Macapá', 'Mazagão', 'Oiapoque', 'Porto Grande', 'Pracuúba', 'Santana', 'Tartarugalzinho', 'Vitória do Jari']
```
