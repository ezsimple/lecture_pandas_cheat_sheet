#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from torch import rand


# %%
rand_count = 8200
s = pd.Series(np.random.randn(rand_count), index=pd.date_range('1/1/2000', periods=rand_count))
s.tail()

# %%
# 누적합을 구한다
s = s.cumsum()

# %%
s.plot()


# %%
# 롤링은 이동평균(추새선)을 구하는 기법이다.
# 윈도우 사이즈 만큼 이동해서 이동평균을 구한다.
r = s.rolling(window=30).agg({'mean': np.mean, 'std': np.std})
r.plot()


# %%
df = pd.DataFrame(np.random.randn(rand_count, 4),
  index=pd.date_range('2000-01-01', periods=rand_count), columns=list('ABCD'))
df = df.cumsum()
df.rolling(window=30).sum().plot(subplots=True)

# %%
df.rolling(window=len(df), min_periods=1).mean().plot()# %%

# %%
df.expanding(min_periods=1).mean().plot()

# %%
df2 = pd.DataFrame({"B": [0, 1, 2, np.nan, 4]})
df2.expanding(min_periods=1).mean().plot()

## expanding과 rolling은 시계열 데이터 분석에 유용합니다.
## NaN 데이터가 있을 경우에 유용합니다.