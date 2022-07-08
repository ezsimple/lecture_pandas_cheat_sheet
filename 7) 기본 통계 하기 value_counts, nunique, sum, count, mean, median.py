#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
from xml.etree.ElementInclude import include
import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()
df.shape

# %%
# 변수의 각 고유 값이 있는 행 개수 계산 (중요)
df['petal_width'].value_counts()

# %%
# number of rows in DataFrame
# df.shape[0] 과 동일합니다.
len(df)

# %%
# 열에 있는 고유 값의 수
df['petal_width'].nunique()

# %%
# 각 열(또는 GroupBy)에 대한 기본 설명 및 통계 (중요)
# 수치형 데이터에 대한 통계를 보여줍니다.
# include, exclude 옵션을 사용하여 컬럼을 선택할 수 있습니다.
df.describe(include='all')

# %%
df.describe(include=[np.object])

# %%
'''
sum() : 전체 데이터의 합
min() : 최소값
count() : 고유 값의 수
max() : 최대값
mean() : 평균
median() : 중앙값
var() : variance (편차)
quantile() : 표준정규분포의 확률에 해당하는 값
std() : 표준편차
apply() : 전체 데이터에 대한 함수 적용
'''

df.quantile([0.25, 0.75])