#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
# https://github.com/corazzon/cracking-the-pandas-cheat-sheet/blob/master/seoul-covid-19-02-eda-output.ipynb
from timeit import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 한글화 작업
plt.figure(dpi=600) # 그래프를 선명하게
plt.rc('font', family = 'NanumGothic') # 시스템에 폰트설치후, 시스템 재시작
plt.rc('axes', unicode_minus = False) # 한글 폰트 사용시 마이너스 폰트가 깨지는 문제 해결
plt.style.use('fivethirtyeight') # 스타일을 사용해 봅니다.

# %%
# retina 디스플레이가 지원되는 환경에서 시각화 폰트가 좀 더 선명해 보입니다.
# from IPython.display import set_matplotlib_formats
# set_matplotlib_formats('retina')

# %%
# 데이터를 로드 합니다.
file_name = f'./seoul-covid19_6_30_.csv'
df = pd.read_csv(file_name)
df.head()

# %%
# 연번으로 정렬
df.sort_values(by='연번', ascending=True)
df.head()

# %%
# 데이터 타입을 변경해서 날짜형태로 변환합니다.
# 판다스의 to_datetime 을 사용해서 날짜 타입으로 변경할 수 있습니다.
# 연도가 없기 때문에 2020년을 날짜에 추가하고 "-" 문자로 날짜를 연결해 줍니다.

df["확진일자"] = pd.to_datetime("2020-"+ df["확진일"].str.replace(".", "-"))
df[["확진일", "확진일자"]].head()

# %%
# 월만 추출합니다.
df["월"] = df["확진일자"].dt.month
df[["확진일", "확진일자", "월"]].tail()

# %%
# 해당 연도의 몇번째 "주"인지 추출합니다.
df["주"] = df["확진일자"].dt.week
df[["확진일", "확진일자", "월", "주"]].head()

# %%
# 확진일자로 선그래프를 그립니다.
df["확진일자"].value_counts().sort_index().plot(figsize=(15, 4))
plt.axhline(30, color="red", linestyle=":")

# %%
# 일자별 확진자수를 선그래프로 그립니다.
# 연도는 모두 2020년이기 때문에 월일만 표기되도록 슬라이싱을 사용해 "월일" 컬럼을 만듭니다.
df["월일"] = df["확진일자"].astype(str).map(lambda x : x[-5:])
day_count = df["월일"].value_counts().sort_index()
day_count.iloc[2]

# %%
g = day_count.plot(figsize=(15, 4))
for i in range(len(day_count)):
    case_count = day_count.iloc[i]
    if case_count > 20:
        g.text(x=i, y=case_count, s=case_count)

# %%
# describe 를 통해 일자별 확진자수를 describe를 통해 요약해 봅니다.
day_count.describe()

# %%
# 확진자가 가장 많았던 날을 찾습니다.
day_count[day_count == day_count.max()]

# %%
# 확진자가 가장 많았던 날의 발생이력을 찾습니다.
df[df["월일"] == "03-10"].head()

# %%
# 선그래프로 그렸던 그래프를 막대그래프로 그립니다.
day_count.plot.bar(figsize=(30, 4))

# %%
# 슬라이싱을 통해 최근 데이터만 그립니다.
g = day_count[-50:].plot.bar(figsize=(15, 4))
g.axhline(day_count.median(), linestyle=":", color="red")
for i in range(50):
    case_count = day_count[-50:].iloc[i]
    if case_count > 10:
        g.text(x=i-0.5, y=case_count, s=case_count)

# %%
# 월별 확진자수에 대한 빈도수를 구해서 시각화 합니다.
month_case = df["월"].value_counts().sort_index()
g = month_case.plot.bar(rot=0)
for i in range(len(month_case)):
    g.text(x=i-0.2, y=month_case.iloc[i]+10, s=month_case.iloc[i])


# %%
# 주별로 빈도수를 구합니다.
weekly_case = df["주"].value_counts().sort_index()
weekly_case.plot(figsize=(15, 4))

# %%
# 주단위 빈도수 막대그래프로 그리기
weekly_case.plot.bar(figsize=(15, 4), rot=0)

# %%
# 월-주 함께 그리기
# groupby 를 통해 "월", "주" 로 그룹화 하여 빈도수를 계산합니다.
month_weekly_case = df.groupby(["월", "주"])["연번"].count()
month_weekly_case

# %%
# 월-주 를 함께 그래프에 표현하기
month_weekly_case.plot.bar(figsize=(15, 4), rot=30)

# %%
# 첫 확진일 부터 마지막 확진일까지 가져옵니다.
# 데이터프레임의 첫번째 날짜는 first_day 에 마지막 날짜는 last_day 에 담습니다.
first_day = df.iloc[-1, 7]
last_day = df.iloc[0, 7]

# %%
# pd.date_range 를 통해 시작하는 날짜부터 끝나는 날짜까지의
# DatetimeIndex 를 만들고 days 라는 변수에 저장합니다.
days = pd.date_range(first_day, last_day)
days[:5]

# %%
# days 변수의 값으로 "연월일" 이라는 컬럼이름을 갖는 데이터프레임을 만듭니다.
# days.to_frame()
df_days =  pd.DataFrame({"확진일자": days})
df_days.head()

# %%
# 확진일자별로 빈도수 구하기
daily_case = df["확진일자"].value_counts()
daily_case.head()

# %%
# 확진일자별로 빈도수 구한 내용을 데이터프레임으로 변환하기
df_daily_case = daily_case.to_frame()
df_daily_case.head()

# %%
# value_counts 결과의 컬럼명을 "확진수" 로 바꾸기
df_daily_case.columns = ["확진수"]
df_daily_case.head()

# %%
# merge 를 통해 전체 확진 일자 만들기
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/08_combine_dataframes.html#join-tables-using-a-common-identifier
# 확진자가 없는 날도 일자에 표현이 되도록 전체 일자와 확진 데이터를 merge 로 합쳐줍니다.
# 1321
all_day = df_days.merge(df_daily_case,
                        left_on="확진일자",
                        right_on=df_daily_case.index, how="left")
all_day.head()

# %%
# 누적 확진자 수 구하기
# 확진수를 fillna를 통해 결측치를 0으로 채워주고 누적해서 더해줍니다.
all_day["누적확진"] = all_day["확진수"].fillna(0).cumsum()
all_day

# %%
# 연도를 제외하고 월-일로 "일자" 컬럼 만들기
all_day["일자"] = all_day["확진일자"].astype(str).map(lambda x : x[-5:])
all_day.head()

# %%
# "확진수", "누적확진" 컬럼을 갖는 데이터프레임을 만듭니다.
cum_day = all_day[["일자", "확진수", "누적확진"]]
cum_day = cum_day.set_index("일자")
cum_day.head()

# %%
# 데이터프레임으로 확진수와 누적확진을 선그래프로 그립니다.
cum_day.plot(figsize=(15, 4))

# %%
# 시리즈로 2개의 그래프 그리기
cum_day["확진수"].plot()
cum_day["누적확진"].plot(figsize=(15, 4))

# %%
# 누적확진수와 확진수와 차이가 크면 제대로 보이지 않기 때문에 확진수만 그립니다.
cum_day["확진수"].plot(figsize=(15, 4))

# %%
# 누적확진만 따로 그립니다.
cum_day["누적확진"].plot(figsize=(15, 4))

# %%
# 로그스케일
# 차이가 너무 커서 그래프가 자세히 보이지 않을때, 로그스케일로 표현하면 차이가 큰 값의 스케일을 조정해주게 됩니다.
np.log(cum_day["누적확진"]).plot(figsize=(15, 4))
np.log(cum_day["확진수"]).plot()

# %%
# 확진월과 요일 구하기
all_day["확진월"] = all_day["확진일자"].dt.month
all_day["확진요일"] = all_day["확진일자"].dt.dayofweek
all_day.head()

# %%
# 월별, 요일별 확진수를 groupby로 구하기
all_day_week = all_day.groupby(["확진월", "확진요일"])["확진수"].sum()
all_day_week = all_day_week.unstack().astype(int)
all_day_week

# %%
# 숫자로 표현된 요일을 문자로 바꿔주기 위해 split 을 통해 문자를 리스트로 변경합니다.
dayofweek = "월 화 수 목 금 토 일"
dayofweek = dayofweek.split()
dayofweek

# %%
# 컬럼의 이름을 한글요일명으로 변경해 줍니다.
all_day_week.columns = dayofweek
all_day_week

# %%
# style.background_gradient 로 색상을 표현합니다.
all_day_week.style.background_gradient(cmap="Blues")

# %%
# 거주지(구별) 확진자의 빈도수를 구하고 시각화 합니다.
gu_count = df["거주지"].value_counts()
gu_count.head()

# %%
# 구별 확진자의 수를 시각화 합니다.
gu_count.sort_values().plot.barh(figsize=(10, 12))

# %%
# 서울에서 확진판정을 받은 데이터이기 때문에 거주지가 서울이 아닐 수도 있습니다.
# 거주지 별로 서울시에 해당되는 데이터만 따로 가져옵니다.
gu = gu_count[:25].index
gu

# %%
# 거주지가 서울이 아닌 지역을 따로 추출합니다.
set(gu_count.index) - set(gu)

# %%
# 구를 전처리 하기 쉽게 컬럼으로 변환하기 위해 reset_index 로 변환합니다.
df_gu = gu_count.reset_index()
df_gu.columns = ["구", "확진수"]
df_gu.head()

df_gu[~df_gu["구"].isin(gu)]

# %%
# 서울에서 확진 받은 사람 중 서울 vs 타지역을 비교해 보기 위해
# "지역"이라는 새로운 컬럼을 만들어 서울지역이 아니라면 "타지역" 이라는 값을 넣어줍니다.
# .loc[행인덱스]
# .loc[행, 열]
# .loc[조건, 열]
df.loc[df["거주지"].isin(gu), "지역"] = df["거주지"]
# df.loc[~df["거주지"].isin(gu)]
# df.loc[df["지역"].isnull(), "지역"] = "타지역"
df["지역"] = df["지역"].fillna("타지역")
df["지역"].unique()

# %%
# 위의 방법으로 할수도 있고 아래의 방법으로 만들수도 있습니다.
# 함수 혹은 익명함수를 사용하는 방법으로 "타지역" 값을 만들 수도 있습니다.
df["지역"] = df["거주지"].map(lambda x : x if x in gu else "타지역")
df[["거주지", "지역"]].head()

# %%
# "지역" 컬럼으로 확진자 빈도수를 구합니다.
gu_etc_count = df["지역"].value_counts()
gu_etc_count

# %%
# 위에서 구한 빈도수를 막대그래프로 그립니다.
gu_etc_count.sort_values().plot.barh(figsize=(8, 10))

# %%
# 접촉력
# 접촉력 빈도수를 구합니다.
df["접촉력"].value_counts().head(20)

# %%
# 접촉력의 unique 값만 구합니다.
df["접촉력"].unique()

# %%
# "확인" 이 들어가는 접촉력만 찾습니다.
df.loc[df["접촉력"].str.contains("확인"), "접촉력"].unique()

# %%
# '확인 중', '확인중' => "확인 중" 으로 변경합니다.
df.loc[df["접촉력"].str.contains("확인"), "접촉력"] = "확인 중"

# %%
# "확인" 이 들어가는 접촉력만 찾습니다.
df.loc[df["접촉력"].str.contains("확인"), "접촉력"].unique()

# %%
# 접촉력 빈도수를 시각화 합니다.
contact_count = df["접촉력"].value_counts()
contact_count_top = contact_count.sort_values().tail(30)
contact_count_top.plot.barh(figsize=(10, 12))

# %%
# 상위 15개만 구합니다.
top_contact = contact_count_top.tail(15)
top_contact

# %%
# 접촉력 빈도수가 높은 목록에 대한 index 값을 구해옵니다.
top_contact.index

# %%
# 위에서 구한 top_contact 에 해당되는 데이터만 isin 으로 가져옵니다.
top_group = df[df["접촉력"].isin(top_contact.index)]
top_group.head()

# %%
# 접촉력, 월별 빈도수를 groupby 로 구합니다.
top_group.groupby(["접촉력", "월"])["연번"].count().unstack().fillna(0).astype(int)

# %%
# 이태원 클럽 관련
# 이태원 클럽 전파는 5월에 시작되었으나, 6월에도 확진자가 있습니다.
# 6월에 이태원 클럽관련 확진자를 찾아봅니다.
df[df["접촉력"].str.contains("이태원") & (df["월"] == 6)]

# %%
# 감염경로 불명
# "접촉력" 이 "확인 중"인 데이터만 구합니다.
df_unknown = df[df["접촉력"] == "확인 중"]
df_unknown.head()

# %%
# 감염경로 불명이 어느정도인지 봅니다.
unknown_weekly_case = df_unknown.groupby(["월", "주"])["연번"].count()
unknown_weekly_case.plot.bar(figsize=(15, 4))

# %%
# 전체 확진수를 value_counts 로 구하고 데이터프레임 형태로 만듭니다.
all_weekly_case = df["주"].value_counts().to_frame()
all_weekly_case.columns = ["전체확진수"]
all_weekly_case.head()

# %%
# 전체 확진수를 value_counts 로 구하고 데이터프레임 형태로 만듭니다.
unknown_weekly_case = df_unknown["주"].value_counts().to_frame()
unknown_weekly_case.columns = ["불명확진수"]
unknown_weekly_case.head()

# %%
# all_weekly_case 와 unknown_weekly_case 를 비교해 봅니다.
unknown_case = all_weekly_case.merge(unknown_weekly_case, left_index=True, right_index=True)
unknown_case = unknown_case.sort_index()
unknown_case.head()

# %%
# 위에서 구한 결과를 시각화 합니다.
unknown_case.plot(figsize=(15, 4))

# %%
# 감염경로 "확인 중"의 주별 비율
unknown_case["확인중비율"] = (unknown_case["불명확진수"] / unknown_case["전체확진수"]) * 100
unknown_case["확인중비율"].plot.bar(figsize=(15, 4))

# %%
## 가장 많은 전파가 일어난 번호
# * [정규 표현식 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D)
# * 파이썬 공식문서 정규표현식 참고하기 :
#    * https://docs.python.org/3.8/library/re.html#re.sub
#
# * 문자열 바꾸기 : re.sub("규칙", "패턴", "데이터")
#    * https://docs.python.org/3.8/library/re.html#text-munging
#
# * 정규표현식 문자열 패턴
#    * https://docs.python.org/3.8/howto/regex.html#matching-characters
#
# * [    ] : 일치시킬 문자 세트의 패턴
# * [가나다] : 가 or 나 or 다 중에 하나를 포함하고 있는지
# * [가-힣] : 한글 가부터 힣까의 문자 중 하나를 포함하고 있는지
# * [0-9] : 0~9까지의 숫자 중 하나를 포함하고 있는지
# * [^0-9] : 숫자를 포함하고 있지 않음
# * [^가-힣] : 한글이 포함되어 있지 않음
# * [가-힣+] : 한글이 하나 이상 포함되는지

import re
# 정규표현식 라이브러리를 불러옵니다.
# 숫자외의 데이터는 제거하는 정규표현식
# #7265 접촉(추정)

# 함수를 통해 숫자외의 문자를 제거하는 get_number 함수를 만듭니다.
def get_number(text):
    return re.sub("[^0-9]", "", text)

get_number("#7265 접촉(추정)")

# %%
# 함수를 map을 통해 접촉번호를 구합니다.
df["접촉번호"] = df["접촉력"].map(get_number)
contact = df["접촉번호"].value_counts().reset_index()
contact.head()

# %%
# 접촉번호가 없는 0번 행은 drop 으로 삭제합니다.
# 한번 drop 한 셀을 다시 drop 하면 이미 삭제를 했는데 다시 삭제하려 하기 때문에 KeyError 가 납니다.
# 다시 실행했을 때 KeyError 가 발생하는 것이 정상입니다.
df_contact = contact.drop(0)
df_contact = df_contact.head(10)
df_contact

# %%
# 상위 10개의 접촉번호를 구해서 top_contact_no 변수에 할당하고 재사용합니다.
top_contact_no = df_contact["index"]

# %%
# contact의 환자번호와 df의 접촉번호를 merge 합니다.
df[df["접촉번호"].isin(top_contact_no)]

# %%
# 조치사항
# 조치사항에 대한 빈도수를 세어봅니다.
# value_counts 는 Series 에만 사용할 수 있습니다.
# 단일 변수의 빈도수를 세는데 사용합니다.
df["조치사항"].value_counts()

# %%
# 퇴원, 사망여부
# 조치사항 컬럼을 통해 퇴원과 사망 컬럼을 새로 만듭니다.
# 또, 어느 병원에 조치되었는지도 병원 컬럼을 만들어서 담습니다.
df["퇴원"] = df["조치사항"].str.contains("퇴원")
df["사망"] = df["조치사항"].str.contains("사망")
# 윈도우의 역슬래시는 엔터키 위에 원달러 표시로 있습니다.
df["병원"] = df["조치사항"].str.replace("\(퇴원\)", "")
df["병원"] = df["병원"].str.replace("\(사망\)", "")

# %%
# 데이터 수집 시점에서 퇴원하지 못한 환자수
df["퇴원"].value_counts()

# %%
# 퇴원여부 빈도수에 대한 비율을 구합니다.
df["퇴원"].value_counts(normalize=True)

# %%
# 사망여부에 따른 빈도수를 구합니다.
df["사망"].value_counts()

# %%
# 사망 여부에 따른 빈도수의 비율을 구합니다.
df["사망"].value_counts(normalize=True) * 100

# %%
# 데이터 수집 시점 기준 현재까지 입원해 있는 확진자 중 가장 오래 입원해 있는 확진자
df[(df["퇴원"] == False) & (df["사망"] == False) & (df["지역"] != "타지역")].tail(5)

# %%
# 병원
# describe 로 요약을 합니다.
# count : 빈도수
# unique : 병원수
# top : 가장 많은 빈도로 등장하는 텍스트
# freq : 가장 많은 빈도의 횟수
df["병원"].describe()

# %%
# 병원의 빈도수를 구합니다.
hospital_count = df["병원"].value_counts()
hospital_count.head(10)

# 병원별 빈도수를 막대그래프로 표현합니다.
hospital_count.sort_values().plot.barh(figsize=(8, 12))

# %%
# 입원환자가 많은 병원을 구합니다.
top_hospital_count = hospital_count.head(10)
top_hospital_index = top_hospital_count.index
top_hospital_index

# %%
hospital_gu = df.groupby(["지역", "병원"])["연번"].count().unstack()
hospital_gu.head()


# %%
# iloc로 일부 데이터만 보기
# 전체 데이터를 보기에 너무 많을 수 있기 때문에 iloc 를 사용해서 일부 데이터만 봅니다.
hospital_gu.fillna(0).iloc[:8, :8]

# %%
# loc로 일부 데이터만 보기
# iloc와 loc의 차이점을 비교해 보세요. (중요)
hospital_gu.loc[["강남구", "강서구"], ["강남성심병원", "서울의료원"]]
top_hospital_index
hospital_gu.loc[["강남구", "강서구"], top_hospital_index]

# %%
# pandas style 적용하기
hospital_gu_heatmap = hospital_gu.fillna(0).astype(int)
hospital_gu_heatmap[top_hospital_index].style.background_gradient()

# %%
# 전체 병원이 너무 많기 때문에 환자가 많은 병원만 따로 봅니다.
hospital_gu_heatmap[top_hospital_index].T.style.background_gradient()

# %%
# 여행력
# "해외" 라는 컬럼을 만들어 데이터를 전처리 합니다.
# "여행력"에 "-" 문자가 들어가 있으면 결측치로 처리합니다.
df["해외"] = df["여행력"]
df["해외"] = df["해외"].str.strip()
df["해외"] = df["해외"].replace("-", np.nan)
df["해외"].nunique()

# %%
# describe 로 요약을 합니다.
# count : 빈도수
# unique : 병원수
# top : 가장 많은 빈도로 등장하는 텍스트
# freq : 가장 많은 빈도의 횟수
df["해외"].describe()

# %%
df["해외"].value_counts().head(10)

# %%
# 여행력이 있는 데이터만 가져와서 서브셋 만들기
# "해외" 컬럼의 값이 결측치가 아닌 데이터만 가져와서
# df_oversea 라는 새로운 데이터프레임에 담습니다.
df_oversea = df[df["해외"].notnull()].copy()
df_oversea.shape

# %%
# 중복되는 지역명이 있는지 확인합니다.
df_oversea["해외"].unique()

# %%
### 텍스트 데이터 다루기
# [Working with text data — pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#testing-for-strings-that-match-or-contain-a-pattern)

# 유럽 지역을 방문했다면 유럽이라고 바꿔주기 위해 국가명을 str.contains 로 검색하기 위한 형태로 만듭니다.
europe = "체코, 헝가리, 오스트리아, 이탈리아, 프랑스, 모로코, 독일, 스페인, 영국, 폴란드, 터키, 아일랜드"
europe = europe.replace(", ", "|")
df_oversea[df_oversea["해외"].str.contains(europe)].head()

# %%
# 남미 지역에 해당되는 국가명을 str.contains 로 검색하기 위한 형태로 만듭니다.
south_america = "브라질, 아르헨티아, 칠레, 볼리비아, 멕시코, 페루"
south_america = south_america.replace(", ", "|")
south_america

# %%
# 중복되는 국가나 지역을 특정 텍스트로 변경해서 그룹화 해서 빈도수를 세어볼 예정입니다.
# .str.contains 와 .loc 를 사용해서 전처리 합니다.
df_oversea.loc[df_oversea["해외"].str.contains(europe), "해외"] = "유럽"
df_oversea.loc[df_oversea["해외"].str.contains(south_america), "해외"] = "남미"
df_oversea.loc[df_oversea["해외"].str.contains("중국|우한"), "해외"] = "중국"
df_oversea.loc[df_oversea["해외"].str.contains("아랍에미리트"), "해외"] = "UAE"
df_oversea.loc[df_oversea["해외"].str.contains("필리핀"), "해외"] = "필리핀"
df_oversea.loc[df_oversea["해외"].str.contains("미국"), "해외"] = "미국"
df_oversea["해외"].value_counts()

# %%
# describe 로 요약을 합니다.
# count : 빈도수
# unique : 병원수
# top : 가장 많은 빈도로 등장하는 텍스트
# freq : 가장 많은 빈도의 횟수
df_oversea["해외"].describe()

# %%
# 확진일자, 해외 별 카운트 수를 구합니다.
day_oversea = df_oversea.groupby(["확진일자", "해외"])["연번"].count()
day_oversea.head()

# %%
# 위에서 구한 값을 바탕으로 지역별 누적 확진수를 구합니다.
day_oversea = day_oversea.groupby(level=[1]).cumsum()
day_oversea

# %%
# 위에서 구한 값을 reset_index() 를 통해 데이터프레임으로 변경하고 "연번" 컬럼을 "확진자수"로 변경합니다.
df_day_oversea = day_oversea.reset_index()
df_day_oversea = df_day_oversea.rename(columns={"연번":"누적확진수"})
df_day_oversea.head()

# %%
# "해외" 컬럼의 빈도수를 구합니다.
oversea_count = df_oversea["해외"].value_counts()

# %%
# 위에서 구한 빈도수를 시각화 합니다.
oversea_count.sort_values().plot.barh(figsize=(10, 12))

# %%
# 일자별 해외 확진자 수를 구합니다
df_day_oversea = df_day_oversea.set_index("확진일자")
df_day_oversea.pivot(columns="해외").plot(figsize=(24, 4), legend=False)

# %%
df_day_oversea.loc[df_day_oversea["해외"] == "미국", "누적확진수"].plot()

# %%
oversea_count_gu = df_oversea["지역"].value_counts()
oversea_count_gu.head()

# %%
# "해외유입 구별 확진자" 시각화 하기
oversea_count_gu.sort_values().plot.barh(figsize=(10, 12))

# %%
# 전체확진자수와 해외유입 확진수 비교
# all_count_gu 변수에 전체 지역의 확진자수 구하기
all_count_gu = df["지역"].value_counts()

# %%
# 데이터프레임으로 변환하고 컬럼명 변경하기
df_all_gu = all_count_gu.to_frame()
df_all_gu.columns = ["전체확진수"]
df_all_gu

# %%
# 해외유입확진수 구하기
df_oversea_gu = pd.DataFrame({"해외유입확진수" : oversea_count_gu})

# %%
### merge 를 통해 전체 확진수와 해외유입확진수 비교하기
# * 이미지 출처 및 Pandas 공식문서 보기 : [How to combine data from multiple tables? — pandas documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/08_combine_dataframes.html#join-tables-using-a-common-identifier)
# <img src="https://pandas.pydata.org/pandas-docs/stable/_images/08_merge_left.svg">
# merge 로 합쳐서 전체확진수와 해외유입확진수 비교해 보기
df_all_oversea_case = df_all_gu.merge(df_oversea_gu, left_index=True, right_index=True)
df_all_oversea_case.head()

# %%
# 시각화 하기
df_all_oversea_case.sort_values(by="해외유입확진수").plot.barh(figsize=(15, 8))

# %%
# df_all_oversea_case["해외유입비율"] 구하기
df_all_oversea_case["해외유입비율"] = (df_all_oversea_case["해외유입확진수"] / df_all_oversea_case["전체확진수"]) * 100
df_all_oversea_case.sort_values(by="해외유입비율", ascending=False).head(10)

# %%
# 해외유입 확진자중 퇴원 여부
# oversea_finish_count 해외유입 확진자 중 퇴원 여부 구하기
oversea_finish_count = df_oversea.groupby(["지역", "퇴원"])["연번"].count().unstack()
oversea_finish_count = oversea_finish_count.fillna(0).astype(int)
oversea_finish_count.plot.bar(figsize=(15, 4), rot=30)

# %%
# 월별 해외 확진자 수
oversea_monthly_case = df_oversea["월"].value_counts()
oversea_monthly_case.sort_index().plot()

oversea_monthly_case.sort_index().plot.bar(rot=0)

# %%
### 구와 월별 해외 확진자 수
# * groupby, crosstab, pivot_table 로 같은 결과의 테이블이 나오도록 구합니다.
#### groupby 로 빈도수 구하기
month_gu = df_oversea.groupby(["월", "지역"])["연번"].count().unstack()
month_gu = month_gu.fillna(0).astype(int)
month_gu.style.background_gradient(cmap="Greens")

# %%
# crosstab 으로 빈도수 구하기
month_gu = pd.crosstab(df_oversea["월"], df_oversea["지역"])
month_gu.style.bar()

# %%
# pivot_table 로 빈도수 구하기
pd.options.display.max_columns = 30
month_gu = pd.pivot_table(df_oversea, index="월", columns="지역", values="연번",
               aggfunc="count", fill_value=0)
month_gu

# %%
# 해외유입이 많은 지역(구)
# 해외유입이 많은 상위 10개 지역을 구합니다.
top_oversea_gu = df_oversea["지역"].value_counts().head().index

# %%
# 시각화 하기
g = month_gu[top_oversea_gu].plot(figsize=(15, 4))
g.legend(loc=1)

# %%
# * 범례 위치 조정하기 : [matplotlib.pyplot.legend — Matplotlib 3.1.2 documentation]
# (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html)

# 구별 해외유입 국가 분석하기
# groupby로 구하기
group_oversea_gu = df_oversea.groupby(["해외", "지역"])["연번"].count().unstack()
group_oversea_gu.fillna(0).astype(int)

# %%
# pivot table로 구하기
# groupby로 구한 결과와 같은 결과가 나오게 구합니다.
group_oversea_gu = df_oversea.pivot_table(index="해외", columns="지역", values="연번", aggfunc="count")
group_oversea_gu.style.background_gradient()

# %%
# 일부 구만 따로 보기
# 전체는 너무 많기 때문에 특정 구만 따로 봅니다.
# 강남 3구의 입국자는 해외 어느 지역에서 입국했나?
group_oversea_gu.loc[["미국", "유럽", "남미", "중국"], ["강남구", "서초구", "송파구"]]

# %%
# top_oversea_gu 에 따른 확진수 보기
group_oversea_gu[top_oversea_gu].dropna(how="all").fillna(0).astype(int)

