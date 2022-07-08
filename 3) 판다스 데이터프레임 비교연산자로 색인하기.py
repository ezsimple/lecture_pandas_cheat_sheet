#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6, 6], "b": [7, 8, 9, 9], "c": [10, 11, 12, 12]},
    index=pd.MultiIndex.from_tuples(
        [("d", 1), ("d", 2), ("e", 2), ("e", 3)], names=["n", "v"]
    ),
)
df


# %%
df[df.b > 7]
df[df["c"] >= 11]

# %%
df.loc[("d", 1), "a"]

# %%
df = df.drop_duplicates()
df
