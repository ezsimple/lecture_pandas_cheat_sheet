#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import seaborn as sns
import numpy as np


# %%
# pd.concat을 하게 되면, 기본적으로 기존 index를 가져와서 합칩니다.
# pd.concat(..., ignore_index=True)로 하면, index를 새로 만들어서 합칩니다.
# union 기능과 비교해서 생각해 봅시다.
# 위아래로 합칠때
