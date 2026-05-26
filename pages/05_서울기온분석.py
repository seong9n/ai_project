# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="서울 기온 분석", layout="wide")

st.title("🌡️ 날짜별 기온분석")

# CSV 파일 불러오기
df = pd.read_csv("seoul.csv", encoding='cp949')

# 날짜 데이터 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 연도, 월, 일 분리
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# 월 선택
month = st.selectbox(
    "월을 선택하세요",
    sorted(df['월'].unique())
)

# 일 선택
day = st.selectbox(
    "일을 선택하세요",
    sorted(df[df['월'] == month]['일'].unique())
)

# 선택한 날짜 데이터 필터링
filtered = df[(df['월'] == month) & (df['일'] == day)]

# 필요한 데이터만 선택
graph_df = filtered[['연도', '최고기온(℃)', '최저기온(℃)']].dropna()

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

# 최고기온
ax.plot(
    graph_df['연도'],
    graph_df['최고기온(℃)'],
    color='hotpink',
    label='최고기온',
    linewidth=2
)

# 최저기온
ax.plot(
    graph_df['연도'],
    graph_df['최저기온(℃)'],
    color='lightblue',
    label='최저기온',
    linewidth=2
)

# 그래프 설정
ax.set_title(f"{month}월 {day}일 날짜별 기온분석", fontsize=18)
ax.set_xlabel("연도", fontsize=13)
ax.set_ylabel("온도(℃)", fontsize=13)

ax.legend()
ax.grid(True)

st.pyplot(fig)

# 데이터 표시
st.subheader("📋 선택한 날짜 데이터")
st.dataframe(graph_df.reset_index(drop=True))
