#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"a": [1, 10, 8, 11, -1], "b": list("abcde"), "c": [1.0, 2.0, np.nan, 3.0, 4.0]}
)
df
# %%
df.iloc[20:]

# %%
# 특정 비율과 갯수로 데이터를 샘플링 하기
df.sample(frac=0.5)

# %%
# Randomly select n rows.
df.sample(n=3)

# %%
# 특정 컬럼에서 가장 큰 값과 작은 값 가져오기
df.nlargest(2, "a")

# %%
# 특정 컬럼에서 가장 큰 값과 작은 값 가져오기
df.nsmallest(2, "a")

# %%
# 인덱스의 순서로 데이터를 색인해 오기
df.iloc[1:3]

# %%

df = pd.read_csv("/mnt/c/Users/INSoft/OneDrive/문서/아이엔소프트_직원연락망 (22.01.14)(20)-new.csv")
df = df.drop_duplicates()
df.head()

# %%
df.iat[0, 0]

# %%
df.query(f'이름.str.contains("퇴사")', engine="python")

# %%
df.query(f'이메일.str.contains("mhlee", na=False)')

# %%
df[df['이메일'].str.contains("mhlee", na=False)]
