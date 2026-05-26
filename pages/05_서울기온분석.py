import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# 페이지 설정
st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

# 제목
st.title("🌡️ 날짜별 기온분석")

# CSV 읽기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 날짜 변환
df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')

# 오류 제거
df = df.dropna(subset=['날짜'])

# 연도/월/일 생성
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# 월 선택
month = st.selectbox(
    "월 선택",
    sorted(df['월'].unique())
)

# 일 선택
day = st.selectbox(
    "일 선택",
    sorted(df[df['월'] == month]['일'].unique())
)

# 필터링
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

# 필요한 컬럼 선택
graph_df = filtered[
    ['연도', '최고기온(℃)', '최저기온(℃)']
].dropna()

# 그래프 생성
fig, ax = plt.subplots(figsize=(14, 6))

# 최고기온
ax.plot(
    graph_df['연도'],
    graph_df['최고기온(℃)'],
    color='hotpink',
    linewidth=2,
    label='최고기온'
)

# 최저기온
ax.plot(
    graph_df['연도'],
    graph_df['최저기온(℃)'],
    color='lightblue',
    linewidth=2,
    label='최저기온'
)

# 제목
ax.set_title(
    f"{month}월 {day}일 날짜별 기온분석",
    fontsize=20
)

# 축
ax.set_xlabel("연도", fontsize=13)
ax.set_ylabel("온도(℃)", fontsize=13)

# 범례
ax.legend()

# 격자
ax.grid(True)

# 출력
st.pyplot(fig)

# 데이터 보기
st.subheader("📋 데이터 보기")
st.dataframe(graph_df.reset_index(drop=True))
