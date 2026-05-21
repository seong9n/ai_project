import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="🌍 MBTI TOP 10 국가",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# 데이터 불러오기
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# -------------------------------------------------
# 제목
# -------------------------------------------------
st.title("🧠 MBTI 유형별 TOP 10 국가")
st.markdown("### 🌎 MBTI를 선택하면 비율이 높은 나라 TOP 10을 보여줘요!")

# -------------------------------------------------
# MBTI 선택
# -------------------------------------------------
mbti_columns = df.columns[1:]

selected_mbti = st.selectbox(
    "✨ MBTI 선택",
    mbti_columns
)

# -------------------------------------------------
# TOP 10 국가 추출
# -------------------------------------------------
country_col = df.columns[0]

top10 = (
    df[[country_col, selected_mbti]]
    .sort_values(by=selected_mbti, ascending=False)
    .head(10)
)

top10.columns = ["국가", "비율"]

# -------------------------------------------------
# 색상 설정
# 1등 빨간색
# 나머지 파란색
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
    "#172554"
]

for i in range(len(top10)):
    if i == 0:
        colors.append("#ef4444")
    else:
        colors.append(blue_gradient[i - 1])

# -------------------------------------------------
# 그래프 생성
# -------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top10["국가"],
        y=top10["비율"],
        marker_color=colors,
        text=[f"{v:.2%}" for v in top10["비율"]],
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
    title=f"🏆 {selected_mbti} 비율 TOP 10 국가",
    template="plotly_white",
    height=650,
    xaxis_title="국가",
    yaxis_title="비율",
    yaxis=dict(
        tickformat=".0%"
    ),
    font=dict(
        size=15
    ),
    title_font=dict(
        size=28
    )
)

# -------------------------------------------------
# 출력
# -------------------------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# 표 출력
# -------------------------------------------------
st.subheader("📄 TOP 10 데이터")

table_df = top10.copy()
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
st.markdown("💡 Streamlit + Plotly 인터랙티브 차트")
