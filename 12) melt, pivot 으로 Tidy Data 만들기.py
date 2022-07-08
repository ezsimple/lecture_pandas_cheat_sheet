#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# jupyter notebook pd.melt? 예제

df = pd.DataFrame({
  'A': {0: 'a', 1: 'b', 2: 'c'},
  'B': {0: 1, 1: 3, 2: 5},
  'C': {0: 2, 1: 4, 2: 6}})
df


# %%
# melt은 열을 기준으로 행을 개별적으로 분할하는 함수
pd.melt(df, id_vars=['A'], value_vars=['A', 'B', 'C']).rename(columns = {'variable':'column'})

# %%
# df.pivot?
df = pd.DataFrame({
  'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
  'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
  'baz': [1, 2, 3, 4, 5, 6],
  'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df

# %%
df.pivot(index='foo', columns='bar')['baz']

# %%
df2 = df.pivot(index='foo', columns='bar', values='baz')

# %%
df2.reset_index()

# %%
df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])


# %%
df = pd.DataFrame({
  "lev1": [1, 1, 1, 2, 2, 2],
  "lev2": [1, 1, 2, 1, 1, 2],
  "lev3": [1, 2, 1, 2, 1, 2],
  "lev4": [1, 2, 3, 4, 5, 6],
  "values": [0, 1, 2, 3, 4, 5]})
df

# %%
df.pivot(index='lev1', columns=['lev2', 'lev3'], values='values')

# %%
df.pivot(index=["lev1", "lev2"], columns=["lev3"],values="values")