#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
from inspect import stack
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
# %%
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# %%
df.plot.line(grid=True)
#df.plot(grid=True)

# %%
df = df.abs() # 컬럼의 값이 양수만 또는 음수만 이어야 한다
df.plot.area(stacked=False, alpha=0.5)
# df.plot.area(stacked=False, grid=True)