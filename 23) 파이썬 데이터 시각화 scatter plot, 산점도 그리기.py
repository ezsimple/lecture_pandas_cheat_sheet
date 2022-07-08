#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl


# %%
df = pd.DataFrame(np.random.randn(50, 4), columns=list('abcd'))

# %%
plt.figure(figsize=(12, 12))
ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1')
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax)

# %%
df.plot.scatter(x='a', y='b', s=df['c'] * 200)