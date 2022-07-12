#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

mpl.rcParams['axes.unicode_minus'] = False


# %%
data = pd.Series(np.random.randn(1000))

# %%
data.plot.kde()

# %%
# kde plot
sns.kdeplot(data)