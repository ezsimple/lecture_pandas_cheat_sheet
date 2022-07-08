#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
df = sns.load_dataset('mpg')
df.head()

# %%
df.groupby(by='origin').size()

df['origin'].value_counts()

# %%
df.groupby(by=['origin', 'cylinders'])['mpg'].mean()


# %%
# df.pivot_table? 확인하기

df.head()

# shift의 경우 결측치을 채우는 방법을 선택할 수 있다.
df['mpg'].shift(-1).head()

# rank(pct=True) 는 비율이 몇번째 인지 알려준다.

# cumsum 는 누적합을 구한다

# cumprod 누적곱을 구한다
