#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from pandas.plotting import scatter_matrix

# %%
# Scatter matrix plot
# kde : 커널밀도함수
df = pd.DataFrame(np.random.randn(1000, 4), columns=list('abcd'))
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')

# %%
# Density plot
data = pd.Series(np.random.randn(1000), name='Density Plot')
data.plot.kde()

# %%
# Andrews curves
from pandas.plotting import andrews_curves
data = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv')
data.head()

# %%
andrews_curves(data, "Name")

# %%
# Parallel coordinates
from pandas.plotting import parallel_coordinates

data = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv')
parallel_coordinates(data, "Name")

# %%
# Lag plot
from pandas.plotting import lag_plot
spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing), name='Lag Plot')
lag_plot(data)


# %%
# Autocorrelation plot
from pandas.plotting import autocorrelation_plot
spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)
data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(spacing), name='Autocorrelation Plot')
autocorrelation_plot(data)


# %%
# Bootstrap plot
from pandas.plotting import bootstrap_plot
data = pd.Series(np.random.randn(1000), name='Bootstrap Plot')
bootstrap_plot(data, size=50, samples=500)


# %%
# RadViz
from pandas.plotting import radviz
data = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv')
radviz(data, 'Name')