#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd

df = pd.DataFrame(
    {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}, index=["k0", "k1", "k2"]
)
df.dtypes
# df.loc["k1", "A"]
