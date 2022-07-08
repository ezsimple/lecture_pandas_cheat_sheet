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
df = pd.DataFrame({
  'a': np.random.randn(1000)+1,
  'b': np.random.randn(1000),
  'c': np.random.randn(1000)-1},
  columns=['a', 'b', 'c']
)

# %%
# bins는 구간 갯수를 정하는 것이다.
sns.histplot(df, bins=10)