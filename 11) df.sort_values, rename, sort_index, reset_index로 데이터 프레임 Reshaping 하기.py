#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
'col2': [2, 1, 9, 8, 7, 4],
'col3': [0, 1, 9, 4, 2, 3],
'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})

df

# %%
df.sort_values(by=['col1'])

# %%
df.sort_values(by=['col1', 'col2'])

# %%
df.rename(columns = {'col1':'column1', 'col2':'column2'})
# %%
df.sort_index()
# %%
# 인덱스를 새로 만들고 싶을 경우
df = df.reset_index()
df

# %%
df = df.drop(columns = ['level_0'])
df
