#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import matplotlib.font_manager as fm

# font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
# font_prop = fm.FontProperties(fname=font_path, size=14)

plt.rcParams['font.family'] = 'NanumGothic'
mpl.rcParams['axes.unicode_minus'] = False

print(mpl.get_configdir())
print(mpl.get_cachedir())
print(mpl.matplotlib_fname())
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
for font in font_list:
  font_name = fm.FontProperties(fname=font).get_name()
  if not font_name.startswith("NanumGothic"):
    continue
  # print(font)
  print(fm.FontProperties(fname=font).get_name())
  print()

# %%
url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"
table = pd.read_html(url)

df = table[3]
df.drop(df.columns[:2], axis=1, inplace=True)
df = df.transpose()
df.rename(columns = {0:'총 확진자(A+B)', 1:'PCR검사자', 2:'PCR확진자(A)', 3:'PCR확진율(%)', 4: '전문가용RAT확진자(B)'}, inplace = True)
df.head()

# plt.figure(figsize=(18, 8))
df.plot.bar(stacked=True)


# df.pivot(index='시도명', columns='세부질병코드', values='확진자수')

# %%

# %%
# 11월 중순 이후 데이터 공개방식 변경
import requests

def get_seoul_covid19_data(page_no):
    """
    page_no : 입력값으로 페이지 번호를 입력하면 해당 번호의 데이터를 가져옴
    start_no : 입력받은 page_no로 시작 번호를 의미
    """
    start_no = (page_no - 1) * 100
    url = f"https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw={page_no}"
    url = f"{url}&order%5B0%5D%5Bdir%5D=desc&start={start_no}&length=100"

    response = requests.get(url)
    jsonObj = response.json()

    records_total = jsonObj['recordsTotal']
    records_total

    end_page = round(records_total / 100) + 1
    end_page

    data = jsonObj["data"]
    return data

data = get_seoul_covid19_data()
df = pd.DataFrame(data)
df