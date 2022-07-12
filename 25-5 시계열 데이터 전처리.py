#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
from timeit import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 한글화 작업
plt.rc('font', family = 'NanumGothic') # 시스템에 폰트설치후, 시스템 재시작
plt.rc('axes', unicode_minus = False) # 한글 폰트 사용시 마이너스 폰트가 깨지는 문제 해결
plt.style.use('fivethirtyeight')

# retina 디스플레이가 지원되는 환경에서 시각화 폰트가 좀 더 선명해 보입니다.
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# %%
file_name = f'./seoul-covid19-11_11_.csv'
df = pd.read_csv(file_name)
df.head()

# %%
# 연번으로 정렬
df.sort_values(by='연번', ascending=True)
df.head()

# %%
# 확진일을 'yyyy-mm-dd' 형식으로 변환
df['확진일자'] = pd.to_datetime("2020-"+df['확진일'].str.replace(".", "-"))
df[['확진일', '확진일자']].head()

# %%
# 확진일자를 월, 일, 요일로 분리하여 저장
df['월'] = df['확진일자'].dt.month
df['일'] = df['확진일자'].dt.day
df['요일'] = df['확진일자'].dt.dayofweek
df['주차'] = df['확진일자'].dt.week

df[['월', '일', '요일', '주차']].head()

# %%
# 라인 그래프 그리기
# df['확진일자'].value_counts().sort_index().plot(title='코로나19 확진일자별 추이',kind='line', figsize=(10, 6))
# mean = df['확진자'].mean()

values = df['퇴원현황'].value_counts(dropna=False).keys().to_list()
count = df['퇴원현황'].value_counts(dropna=False).to_list()
value_dict = dict(zip(values, count))
value_dict

df['퇴원'] = df['퇴원현황'].values.__eq__('퇴원')
df
# df['퇴원현황'].count()
# total = len(df)

# plt.axhline(y=30, color='red', linestyle='--')
# %%
# 평균 감염자수 계산
df["월일"] = df["확진일자"].astype(str).map(lambda x : x[-5:])
day_count = df["월일"].value_counts().sort_index()

sum = 0
for i in range(len(day_count)):
    case_count = day_count.iloc[i]
    sum += case_count
    print(case_count)
mean1 = (sum/len(day_count))

mean2 = day_count.describe()['mean']

# %%
g = day_count.plot(title='2020년 코로나19 감염 추이', figsize=(15, 4))
g.axhline(y=mean2, color='red', linestyle=':')
# 선그래프에 값 표시하기
for i in range(len(day_count)):
    case_count = day_count.iloc[i]
    if case_count > 45:
        g.text(x=i, y=case_count, s=case_count)

# %%
day_count.describe()


# %%
# 최근 데이터만 슬라이싱으로 나누어 그리기
g = day_count[-30:].plot.bar(figsize=(15, 4), rot=30, title='2020년 코로나19 감염 추이')
g.axhline(day_count[-30:].median(), linestyle=":", color="red")

for i in range(30):
    case_count = day_count[-30:].iloc[i]
    if case_count > 10:
        g.text(x=i-0.5, y=case_count, s=case_count)

# %%
# 월별 확진자수에 대한 빈도수를 구해서 시각화 합니다.

month_case = df["월"].value_counts().sort_index()
g = month_case.plot.bar(rot=0)

for i in range(len(month_case)):
    g.text(x=i-0.2, y=month_case.iloc[i]+10, s=month_case.iloc[i])

# %%
# 주차별로 빈도수를 구합니다.

weekly_case = df["주차"].value_counts().sort_index()
weekly_case.plot(figsize=(15, 4))

# %%
# groupby 를 통해 "월", "주" 로 그룹화 하여 빈도수를 계산합니다.
month_weekly_case = df.groupby(["월", "주차"])["연번"].count()
g = month_weekly_case.plot.bar(figsize=(15, 4), rot=30)
g.axhline(month_weekly_case.median(), linestyle=":", color="red")

# %%
# 모든 날짜를 행에 만들어 주기
# 확진자가 없는 날의 데이터도 만들어 줍니다.
first_day = df.iloc[-1, 7]
print(first_day)
last_day = df.iloc[0, 7]
print(last_day)
days = pd.date_range(start=first_day, end=last_day)
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
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/08_combine_dataframes.html#join-tables-using-a-common-identifier
# 확진자가 없는 날도 일자에 표현이 되도록 전체 일자와 확진 데이터를 merge 로 합쳐줍니다.
# 1321
all_day = df_days.merge(df_daily_case,
                        left_on="확진일자",
                        right_on=df_daily_case.index, how="left")
all_day.head()


# %%
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
# 차이가 너무 커서 그래프가 자세히 보이지 않을때 로그스케일로 표현하면 차이가 큰 값의 스케일을 조정해주게 됩니다.
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

# %%
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
# 이태원 클럽 전파는 5월에 시작되었으나 6월에도 확진자가 있습니다.
# 6월에 이태원 클럽관련 확진자를 찾아봅니다.
df[df["접촉력"].str.contains("이태원") & (df["월"] == 6)]


# %%
# 감염경로 불명
# "접촉력" 이 "확인 중"인 데이터만 구합니다.
df_unknown = df[df["접촉력"] == "확인 중"]
df_unknown.head()

# %%
# 감염경로 불명이 어느정도인지 봅니다.
unknown_weekly_case = df_unknown.groupby(["월", "주차"])["연번"].count()
unknown_weekly_case.plot.bar(title='감염경로불명',figsize=(15, 4), rot=30)


# %%
# 전체 확진수를 value_counts 로 구하고 데이터프레임 형태로 만듭니다.
all_weekly_case = df["주차"].value_counts().to_frame()
all_weekly_case.columns = ["전체확진수"]
all_weekly_case.head()

# %%
# 전체 확진수를 value_counts 로 구하고 데이터프레임 형태로 만듭니다.
unknown_weekly_case = df_unknown["주차"].value_counts().to_frame()
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