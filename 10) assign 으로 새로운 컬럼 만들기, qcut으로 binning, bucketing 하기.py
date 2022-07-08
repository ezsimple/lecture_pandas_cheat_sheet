#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({'temp_c': [17.0, 25.0]},
  index=['Portland', 'Berkeley'])
df.head()

# df = df.assign 과 df['뉴컬럼명'] 이 동일한 결과 입니다.
df = df.assign(temp_f=df.temp_c * 9 / 5 + 32)
df['temp_f2'] = df.temp_c * 9 / 5 + 32
df

# %%
df = pd.DataFrame({'A': range(1,11), 'B': np.random.randn(10)})
df

# %%
# 5개의 값을 4개의 구간으로 나눠라.
pd.DataFrame(pd.qcut(range(5), 4))

# %%
# 3개의 버킷수로 나누어라 (binning, bucketing)
pd.DataFrame(pd.qcut(range(5), 3, labels=["good", "medium", "bad"]))


# %%
# 열(index), 컬럼의 최고값, 최저값 axis=0, axis=1
df.min(axis=1) # 열(index)의 최저값
df.max(axis=0) # 컬럼의 최고값
# df

df = pd.DataFrame({'A': range(1,11), 'B': np.random.randn(10) * 10})
df

# %%
# lower, upper는 threshold 의 최소값과 최대값을 의미합니다.
df.A.clip(lower=5, upper=10)


# %%
df.abs()