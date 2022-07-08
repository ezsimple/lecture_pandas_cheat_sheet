#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
from inspect import stack
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# %%
df = pd.DataFrame({
  'a': np.random.randn(1000)+1,
  'b': np.random.randn(1000),
  'c': np.random.randn(1000)-1},
  columns=['a', 'b', 'c']
)

# %%
# 차분은 앞열의 값을 뺀 값을 구하는 것이다
df['a_shift'] = df['a'].shift(1)
df['a_diff'] = df['a'].diff()
df[['a', 'a_shift', 'a_diff']].head()
# %%
df['a'].diff().hist(bins=10)
# %%
df.diff().hist(bins=50, alpha=0.5, color='red')

# %%
data = pd.Series(np.random.randn(1000))
data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4))