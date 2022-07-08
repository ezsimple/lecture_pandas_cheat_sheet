#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import seaborn as sns
import numpy as np

adf = pd.DataFrame({
  'x1': ['A', 'B', 'C'],
  'x2': [1, 2, 3]})
adf

# %%
bdf = pd.DataFrame({
  'x1': ['A', 'B', 'D'],
  'x3': ['T', 'F', 'T']})
bdf

# %%
# sql의 join과 유사합니다.
# left, right, inner, outer 옵션을 사용하여 옆으로 합칠 수 있습니다.
pd.merge(adf, bdf, how='left', on='x1')