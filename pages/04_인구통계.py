import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 한글 깨짐 방지
# -----------------------------
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv")

# 컬럼명 수정
df.rename(columns={"10~20세": "20~29세"}, inplace=True)

# 행정구 목록
districts = df["행정구역"].tolist()

# -----------------------------
# 제목
# -----------------------------
st.title("📊 서울시의 인구통계")

# -----------------------------
# 행정구 선택
# -----------------------------
selected = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택 데이터
selected_data = df[df["행정구역"] == selected]

# 연령대 컬럼
age_columns = [
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70~79세",
    "80~89세",
    "90~99세",
    "100세 이상"
]

# 인구 데이터
population = selected_data[age_columns].values.flatten()

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# 배경색
fig.patch.set_facecolor("#E6D5FF")
ax.set_facecolor("#F3E8FF")

# 꺾은선 그래프
ax.plot(
    age_columns,
    population,
    color="red",
    marker="o",
    linewidth=3
)

# 제목
ax.set_title("서울시의 인구통계", fontsize=18)

# 축 제목
ax.set_xlabel("연령대")
ax.set_ylabel("인구수")

# 격자
ax.grid(True, linestyle="--", alpha=0.5)

# x축 글자 회전
plt.xticks(rotation=20)

# 출력
st.pyplot(fig)
