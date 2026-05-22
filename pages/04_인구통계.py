import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 불러오기
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="euc-kr")

# 컬럼명 수정
df.rename(columns={"10~20세": "20~29세"}, inplace=True)

# 제목
st.title("📊 서울시의 인구통계")

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

# 행정구 선택
districts = df["행정구역"].tolist()

selected = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택 데이터
selected_data = df[df["행정구역"] == selected]

# 꺾은선 그래프용 데이터
chart_df = pd.DataFrame({
    "연령대": age_columns,
    "인구수": selected_data[age_columns].values.flatten()
})

# 꺾은선 그래프
fig = px.line(
    chart_df,
    x="연령대",
    y="인구수",
    markers=True,
    title="서울시의 인구통계"
)

# 그래프 스타일
fig.update_traces(line_color="red")

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

# ---------------------------------------
# 연령대별 많은 구 찾기
# ---------------------------------------

st.subheader("🏆 연령대별 인구가 많은 자치구")

selected_age = st.selectbox(
    "연령대를 선택하세요",
    age_columns
)

# 정렬
top_df = df[["행정구역", selected_age]].sort_values(
    by=selected_age,
    ascending=False
)

# TOP 10
top10 = top_df.head(10)

# 막대그래프
bar_fig = px.bar(
    top10,
    x="행정구역",
    y=selected_age,
    title=f"{selected_age} 인구가 많은 자치구 TOP10"
)

# 스타일
bar_fig.update_traces(marker_color="red")

bar_fig.update_layout(
    paper_bgcolor="#E6D5FF",
    plot_bgcolor="#F3E8FF",
    font=dict(
        family="Malgun Gothic",
        size=14
    )
)

# 출력
st.plotly_chart(bar_fig, use_container_width=True)
