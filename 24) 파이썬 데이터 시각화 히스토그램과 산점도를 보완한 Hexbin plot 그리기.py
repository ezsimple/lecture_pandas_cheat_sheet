#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl


# %%
df = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
df["b"] = df["b"] + np.arange(1000)
df.plot.hexbin(x="a", y="b", gridsize=15);

# %%
df['z'] = np.random.uniform(0, 3, 1000)


# %%
# histogram과 산점도를 보완한 hexbin plot 그리기
# reduce_C_function에 np.max, mean, median, min 등을 사용할 수 있다.
# 최대값, 평균, 중앙값, 최소값에 대한 binning 챠트를 그릴 수 있다.
df.plot.hexbin(x="a", y="b", C='z', reduce_C_function=np.max, gridsize=15)