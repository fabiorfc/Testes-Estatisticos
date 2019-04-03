#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
    TESTES ESTATISTICO PARA DUAS AMOSTRAS

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
    TESTE Z
Hzero = As medias sao iguais (mu_1 = mu_2)
"""
diagnostico_m = df.query("diagnosis == 'M'")
diagnostico_b = df.query("diagnosis == 'B'")

# Efetuando o Zteste para a comparacao entre as médias
ztest(diagnostico_m["mean_radius"], diagnostico_b["mean_radius"])

# Calculo do intervalo de confianca para a diferenca entre as medis
zconfint(diagnostico_m["mean_radius"], diagnostico_b["mean_radius"])


"""----------------------------------------------------------------------------
    TESTE T
Hzero = As medias sao iguais (mu_1 = mu_2)
"""
diagnostico_m = df.query("diagnosis == 'M'")
diagnostico_b = df.query("diagnosis == 'B'")

# Efetuando o Zteste para a comparacao entre as médias
ztest(diagnostico_m["mean_radius"], diagnostico_b["mean_radius"])

# Calculo do intervalo de confianca para a diferenca entre as medis
descr_stats_m = DescrStatsW(diagnostico_m["mean_radius"])
descr_stats_b = DescrStatsW(diagnostico_b["mean_radius"])
resultado = descr_stats_m.get_compare(descr_stats_b)
print(resultado.summary(use_t = True))


