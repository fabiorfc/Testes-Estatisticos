#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
    TESTES ESTATISTICO PARA UMA AMOSTRA

"""


"""----------------------------------------------------------------------------
    Importando as libraries
"""
import pandas as pd
from statsmodels.stats.weightstats import zconfint, DescrStatsW, ztest


"""----------------------------------------------------------------------------
    Importando os dados
"""
endereco_dos_dados = 'http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
nomes_das_variaveis = ['id','diagnosis',
                       'mean_radius','mean_texture','mean_perimeter','mean_area',
                       'mean_smoothness','mean_compactness','mean_concavity',
                       'mean_concave','mean_symmetry','mean_fractal_dimension',                       
                       'std_radius','std_texture','std_perimeter','std_area',
                       'std_smoothness','std_compactness','std_concavity',
                       'std_concave','std_symmetry','std_fractal_dimension',                       
                       'worst_radius','worst_texture','worst_perimeter','worst_area',
                       'worst_smoothness','worst_compactness','worst_concavity',
                       'worst_concave','worst_symmetry','worst_fractal_dimension']

df = pd.read_csv(endereco_dos_dados, header = None)
df.columns = nomes_das_variaveis
del endereco_dos_dados,nomes_das_variaveis



"""----------------------------------------------------------------------------
    Verificando a base de dados
"""
# Top 5 dos dados
df.head()

# Tipagem dos dados
df.ftypes

# Descrição dos dados
df.describe()




"""----------------------------------------------------------------------------
    Z Test
Pressupõe normalidade

"""
diagnostico_m = df.query("diagnosis == 'M'")
diagnostico_b = df.query("diagnosis == 'B'")


# Efetuando o Zteste para a média (Comparando os resultados)
ztest(diagnostico_m['mean_radius'], value = diagnostico_m['mean_radius'].mean())
ztest(diagnostico_m['mean_radius'], value = diagnostico_b['mean_radius'].mean())


# Gerando o intervalo de confiança
zconfint(diagnostico_m['mean_radius'])
zconfint(diagnostico_b['mean_radius'])


"""----------------------------------------------------------------------------
        T Test
"""
diagnostico_m = df.query("diagnosis == 'M'")
diagnostico_b = df.query("diagnosis == 'B'")

# Aplicando o teste
resultados_m = DescrStatsW(diagnostico_m['mean_radius'])
resultados_b = DescrStatsW(diagnostico_b['mean_radius'])

# Gerando o intervalo de confiança
resultados_m.tconfint_mean()
resultados_b.tconfint_mean()




