import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# CSV 불러오기 (한글 인코딩 해결)
# -----------------------------
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="euc-kr")

# 컬럼명 수정
df.rename(columns={"10~20세": "20~29세"}, inplace=True)

# 행정구 목록
districts = df["행정구역"].tolist()

# 제목
st.title("📊 서울시의 인구통계")

# 행정구 선택
selected = st.selectbox(
    "행정구를 선택하세요",
    districts
)

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

# 선택 데이터
selected_data = df[df["행정구역"] == selected]

# 그래프용 데이터
chart_df = pd.DataFrame({
    "연령대": age_columns,
    "인구수": selected_data[age_columns].values.flatten()
})

# 그래프 생성
fig = px.line(
    chart_df,
    x="연령대",
    y="인구수",
    markers=True,
    title="서울시의 인구통계"
)

# 빨간색 그래프
fig.update_traces(line_color="red")

# 연한 보라색 배경
fig.update_layout(
    paper_bgcolor="#E6D5FF",
    plot_bgcolor="#F3E8FF",
    font=dict(
        family="Malgun Gothic",
        size=14
    )
)

# 출력
st.plotly_chart(fig, use_container_width=True)
