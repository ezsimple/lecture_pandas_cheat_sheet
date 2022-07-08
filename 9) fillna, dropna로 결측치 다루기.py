#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                  "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                  "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]})
df

# %%
# 결측치 제거 (컬럼별로 제거)
df.dropna()


# %%
# Replace all NA/null data with value.
# 모든 NA/null 데이터를 값으로 바꿉니다
values = df['born'].median()
df.fillna(value=values)
