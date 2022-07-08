#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 한글 폰트 사용시 마이너스 폰트가 깨지는 문제 해결
mpl.rcParams['axes.unicode_minus'] = False

# %%
df = pd.DataFrame(np.random.randn(1000, 4),
  index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
df = df.cumsum()
plt.figure(figsize=(12, 8))
df.plot()

# %%
sns.pairplot(df, diag_kind='kde')