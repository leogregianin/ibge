#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from ibge.localidades import (
    Regioes,
    Estados,
    Municipios,
    Municipio,
    MunicipioPorUF
)


class TestCase(unittest.TestCase):

    def setUp(self):
        self.regioes = Regioes()
        self.estados = Estados()
        self.municipios = Municipios()
        self.municipio = Municipio('4219507')
        self.municipio_por_uf = MunicipioPorUF('14')

    def test_contagem_de_regioes(self):
        self.assertEqual(self.regioes.count(), 5)

    def test_contagem_de_estados(self):
        self.assertEqual(self.estados.count(), 27)

    def test_contagem_de_municipios(self):
        self.assertEqual(self.municipios.count(), 5570)

    def test_contagem_do_municipio(self):
        self.assertEqual(self.municipio.count(), 1)

    def test_nome_do_municipio_do_ibge_4219507(self):
        self.assertEqual(self.municipio.getNome(), 'Xanxerê')

    def test_uf_do_municipio_do_ibge_uf(self):
        self.assertEqual(self.municipio.getUF(), 'SC')

    def test_contagem_do_municipio_por_uf(self):
        self.assertEqual(self.municipio_por_uf.count(), 15)


if __name__ == '__main__':
    unittest.main()
