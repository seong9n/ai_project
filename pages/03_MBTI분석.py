import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="🌍 MBTI 세계 분석",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# 스타일
# -------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 데이터 불러오기
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -------------------------------------------------
# 제목
# -------------------------------------------------
st.title("🧠 세계 국가별 MBTI 분석")
st.markdown("### 🌎 국가를 선택하면 MBTI 비율을 확인할 수 있어요!")

# -------------------------------------------------
# 국가 선택
# -------------------------------------------------
country_col = df.columns[0]

country = st.selectbox(
    "🌍 국가 선택",
    sorted(df[country_col].unique())
)

# -------------------------------------------------
# 선택한 국가 데이터
# -------------------------------------------------
selected_row = df[df[country_col] == country]

mbti_columns = df.columns[1:]

mbti_values = selected_row[mbti_columns].iloc[0]

chart_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "비율": mbti_values.values
})

# -------------------------------------------------
# 정렬
# -------------------------------------------------
chart_df = chart_df.sort_values(
    by="비율",
    ascending=False
).reset_index(drop=True)

# -------------------------------------------------
# 색상 설정
# 1등 = 빨강
# 나머지 = 파란색 그라데이션
# -------------------------------------------------
colors = []

blue_gradient = [
    "#dbeafe",
    "#bfdbfe",
    "#93c5fd",
    "#60a5fa",
    "#3b82f6",
    "#2563eb",
    "#1d4ed8",
    "#1e40af",
    "#1e3a8a",
    "#172554",
    "#1d4ed8",
    "#2563eb",
    "#3b82f6",
    "#60a5fa",
    "#93c5fd"
]

for i in range(len(chart_df)):
    if i == 0:
        colors.append("#ef4444")  # 빨간색
    else:
        colors.append(blue_gradient[i - 1])

# -------------------------------------------------
# 최고 MBTI
# -------------------------------------------------
top_mbti = chart_df.iloc[0]["MBTI"]
top_value = chart_df.iloc[0]["비율"]

st.success(
    f"🏆 {country}의 대표 MBTI는 "
    f"**{top_mbti}** 입니다! ({top_value:.2%})"
)

# -------------------------------------------------
# Plotly 그래프
# -------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df["MBTI"],
        y=chart_df["비율"],
        marker_color=colors,
        text=[
            f"{v:.2%}" for v in chart_df["비율"]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# -------------------------------------------------
# 그래프 꾸미기
# -------------------------------------------------
fig.update_layout(
    title=f"📊 {country} MBTI 비율",
    height=600,
    template="plotly_white",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    hovermode="x",
    font=dict(
        size=15
    ),
    title_font=dict(
        size=28
    ),
    xaxis=dict(
        tickfont=dict(size=14)
    ),
    yaxis=dict(
        tickformat=".0%",
        gridcolor="lightgray"
    )
)

# -------------------------------------------------
# 그래프 출력
# -------------------------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# 데이터 테이블
# -------------------------------------------------
st.subheader("📄 MBTI 비율 데이터")

table_df = chart_df.copy()
table_df["비율"] = table_df["비율"].apply(
    lambda x: f"{x:.2%}"
)

st.dataframe(
    table_df,
    use_container_width=True
)

# -------------------------------------------------
# 하단
# -------------------------------------------------
st.markdown("---")
st.markdown("💡 Streamlit + Plotly 기반 인터랙티브 시각화")
