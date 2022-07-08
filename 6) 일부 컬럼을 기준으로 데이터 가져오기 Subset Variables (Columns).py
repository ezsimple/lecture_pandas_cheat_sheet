#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
df

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df[columns].head()

# %%
df['sepal_length']

# %%
# 특정 컬럼명 필터링 하기
df.filter(regex='_').head()

# %%
# 특정 컬럼을 제외하고 가져오기
df.filter(regex='^(?!species$).*').head()

# %%
# 컬럼명A ~ 컬럼명B 까지 가져오기
# df.loc[:, '컬럼명A':'컬럼명B']
df.loc[:, 'sepal_length':'petal_width'].head()

# %%
# 컬럼0~ 컬럼2까지의 데이터 가져오기
df.iloc[:, 0:2].head()

# %%
df.iloc[:, [1, 2, 4]].head()