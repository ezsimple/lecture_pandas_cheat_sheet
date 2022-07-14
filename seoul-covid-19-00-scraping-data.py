#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# %%
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"
table = pd.read_html(url)
# print(len(table))
df = table[3]


# %%
# 11월 중순 이후 데이터 공개방식 변경
# f-string
url = "https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw=1"
# url = f"{url}&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc"
url = f"{url}&start=0&length=100"
# "&search%5Bvalue%5D=&search%5Bregex%5D=true&_=1606633538547"
url

# %%
response = requests.get(url)
data_json = response.json()
# pd.DataFrame(data_json["data"])

records_total = data_json['recordsTotal']
records_total

end_page = round(records_total / 100) + 1
end_page

data = data_json["data"]

def get_seoul_covid19_100(page_no):
    """
    page_no : 입력값으로 페이지 번호를 입력하면 해당 번호의 데이터를 가져옴
    start_no : 입력받은 page_no로 시작 번호를 의미
    """
    start_no = (page_no - 1) * 100
    url = f"https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw={page_no}"
    url = f"{url}&order%5B0%5D%5Bdir%5D=desc&start={start_no}&length=100"
    response = requests.get(url)
    data_json = response.json()
    return data_json


# %%
# time.sleep 으로 시차를 두기 위해
import time
# tqdm : 진행상태를 표시하기 위해
from tqdm import trange

# # 주석처리 : ctrl + /
# page_list = []
# for page_no in trange(1, 4):
#     one_page = get_seoul_covid19_100(page_no)
#     if len(one_page["data"]) > 0:
#         one_page = pd.DataFrame(one_page["data"])
#         page_list.append(one_page)
#         time.sleep(0.5)
#     else:
#         break

# page_list

# pd.concat(page_list)

# 전체 페이지를 가져오기 전에 일부 페이지만 실행
page_list = []
# 데이터가 제대로 로드 되는지 앞부분 3페이지 정도만 확인하고 전체페이지를 가져오록 합니다.
# 처음부터 전체 페이지를 수집하면 중간에 오류가 나도 찾기가 어렵습니다.
# 일부만 우선 가져와 보고 잘 동작한다면 전체를 가져오도록 합니다.
all_page = 3
for page_no in trange(all_page + 1):
    one_page = get_seoul_covid19_100(page_no)
    one_page = pd.DataFrame(one_page["data"])
    page_list.append(one_page)
    # 서버에 한번에 너무 많은요청을 보내면 서버에 부담이 됩니다.
    # 서버에 부담을 주지 않기 위애 0.5초씩 쉬었다 가져옵니다.
    time.sleep(0.5)

# 가져온 데이터가 맞는지 확인 너무 많을 수 있기 때문에 슬라이싱으로 잘라서 보기
# 리스트를 하나로 합치는 것이 좋다.
df_all_doc = pd.concat(page_list)
type(df_all_doc)
# %%

def get_multi_page_list(start_page, end_page = 80):
    # 데이터가 제대로 로드 되는지 앞부분 3페이지 정도만 확인하고 전체페이지를 가져오록 합니다.

    page_list = []
    for page_no in trange(start_page, end_page + 1):
        one_page = get_seoul_covid19_100(page_no)
        if len(one_page["data"]) > 0:
            one_page = pd.DataFrame(one_page["data"])
            page_list.append(one_page)
            # 서버에 한번에 너무 많은요청을 보내면 서버에 부담이 됩니다.
            # 서버에 부담을 주지 않기 위애 0.5초씩 쉬었다 가져옵니다.
            time.sleep(0.5)
        else:
            # 수집된 값이 없다면 False를 반환합니다.
            # False 반환 시 수집한 리스트를 반환하도록 합니다.
            return page_list
    return page_list

# 따로 설정하지 않으면 end_page 변수에 들어있는 숫자가 마지막 페이지가 됩니다.
end_page

# 시작페이지와 끝페이지를 꼭 확인해 주세요.
start_page = 1
# end_page = 88
page_list = get_multi_page_list(start_page, end_page)
# 데이터가 너무 많기 때문에 슬라이싱으로 1개만 미리보기
page_list[:1]

page_list

# %%
# concat을 통해 하나의 데이터프레임으로 합쳐줍니다.
df_all = pd.concat(page_list)
df_all.head()

# %%
# read_html 로 읽어온 3번째 테이블의 컬럼명을 수집한 데이터의 컬럼으로 사용합니다.
cols = df.columns.tolist()
cols

# %%
import re
def extract_number(num_string):
    if type(num_string) == str:
        num_string = num_string.replace("corona19", "")
        num = re.sub("[^0-9]", "", num_string)
        num = int(num)
        return num
    else:
        return num_string


num_string = "<p class='corona19_no'>7625</p>"
extract_number(num_string)

# class='corona19_no' 의 값을 추출합니다.
df_all["연번"] = df_all[0].map(extract_number)

df_all["연번"].head()

# %%
def extract_hangeul(origin_text):
    subtract_text = re.sub("[^가-힣]", "", origin_text) # 한글만 추출
    return subtract_text

extract_hangeul("<b class='status1'>퇴원</b>")

extract_hangeul("<b class='status2'>사망</b>")

extract_hangeul("<b class=''></b>")

# 정규표현식으로 변경하는 방법도 있고 str.contains를 사용하는 방법도 있습니다.
# df_all["퇴원현황"] = df_all["퇴원현황"].map(extract_hangeul)
# df_all["퇴원현황"].value_counts()

df_all["퇴원현황"].value_counts()

df_all.loc[df_all["퇴원현황"].str.contains("퇴원"), "퇴원현황"] = "퇴원"
df_all.loc[df_all["퇴원현황"].str.contains("사망"), "퇴원현황"] = "사망"
df_all.loc[~df_all["퇴원현황"].str.contains("퇴원|사망"), "퇴원현황"] = np.nan
df_all["퇴원현황"].value_counts()

last_date = df_all.iloc[0]["확진일"]
last_date

# 마지막 확진일을 파일명에 써주기 위해 . 을 _ 로 변경합니다.
# 확장자와 구분이 쉽게 되도록 _ 로 변경합니다.

date = last_date.replace(".", "_")
date

# 파일명을 만들어 줍니다.
# file_name

file_name = f"seoul-covid19-{date}.csv"
file_name

# csv 파일로 저장합니다.
df_all.to_csv(file_name, index=False)

# 제대로 저장되었는지 확인합니다.
pd.read_csv(file_name)

