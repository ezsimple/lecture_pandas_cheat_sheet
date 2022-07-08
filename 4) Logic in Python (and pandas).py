#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "a": [4, 5, np.nan, 6, 6],
        "b": [7, np.nan, 8, 9, 9],
        "c": [10, 11, 12, 12, np.nan],
    },
    index=pd.MultiIndex.from_tuples(
        [("d", 1), ("d", 2), ("e", 2), ("e", 3), ("e", 4)], names=["n", "v"]
    ),
)
df = df.drop_duplicates()
df

# %%
df[df["b"] > 7]

# %%
# 컬럼에 특정값이 있는 지 여부 확인
df[df.a.isin([4])]

# %%
# not null 여부 확인
pd.notnull(df.a)

# %%
# ~ : df의 not 연산
~df.any(axis=1)

# %%
df[(df.b == 7) | (df.a == 5)]

# %%
# fractional 분획의 ... 비율(0~1)을 나타냅니다.
df.sample(frac=0.5)
