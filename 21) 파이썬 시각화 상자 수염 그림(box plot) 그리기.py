#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
from inspect import stack
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# %%
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))

# %%
# min, 25%(1사분위수), 50%(2사분위수), 75%(3사분위수), max
df.describe()

# %%
plt.grid(True)
bp = df.plot.box()

# %%
color = {'boxes': 'DarkGreen', 'whiskers': 'DarkOrange', 'medians': 'DarkBlue', 'caps': 'Gray'}
bp = df.plot.box(color=color, sym='r+')


# %%
plt.figure()
bp = sns.boxplot(data=df, palette='Set2')
