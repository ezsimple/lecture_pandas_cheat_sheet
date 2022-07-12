#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 한글화 작업
plt.rcParams['font.family'] = 'NanumGothic' # 시스템에 폰트설치후, 시스템 재시작
mpl.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 폰트가 깨지는 문제 해결

# %%
file_name = f'./seoul-covid19-11_11_.csv'
df = pd.read_csv(file_name)
df.head()

# %%
# 연번으로 정렬
df.sort_values(by='연번', ascending=True)
df.head()

# %%
# df[df.loc[df['퇴원현황']] == '퇴원'].head()
df['퇴원현황'].value_counts(dropna=True)




# %%
# 시각화 분석
df.plot(kind='line', x='연번', y='환자', figsize=(10, 6))