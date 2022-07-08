#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

def smp(x):
  # 뒤에서 3번째까지의 문자를 가져오는 함수
  x = x[-3:]
  return x

# lamda를 사용한 익명함수 적용
df['species+3'] = df['species'].apply(lambda x: x[:3])

# 정의한 함수를 적용
df['species-3'] = df['species'].apply(smp)

df