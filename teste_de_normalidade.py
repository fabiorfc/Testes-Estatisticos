#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    TESTES DE NORMALIDADE
H0:  A amostra apresenta distribuição normal
"""


"""----------------------------------------------------------------------------
    Importando as libraries
"""
import pandas as pd
from scipy.stats import normaltest
import matplotlib.pyplot as plt


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
    Aplicando o teste
"""
# Separando os dados
diagnostico_m = df.query("diagnosis == 'M'")

# Verificação gráfica
plt.hist(diagnostico_m["mean_radius"], bins = 20)

# APlicando o teste
stat, p = normaltest(diagnostico_m["mean_radius"])
print("p-valor: {}".format(round(p,2)))
print("Estatística do teste: {}".format(round(stat)))




