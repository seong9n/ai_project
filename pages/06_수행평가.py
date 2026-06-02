from pathlib import Path
import pandas as pd

base = Path("/mnt/data")

# Generate sample large dataset: 17 regions x 10 restaurants
regions = ["서울","부산","대구","인천","광주","대전","울산","세종","경기","강원","충북","충남","전북","전남","경북","경남","제주"]
rows = []
for r in regions:
    for i in range(1,11):
        rows.append({
            "지역": r,
            "맛집": f"{r} 맛집 {i}",
            "소개": f"{r} 지역에서 인기 있는 맛집 {i}번입니다.",
            "추천메뉴": f"대표메뉴 {i}",
            "추천대상": "학생, 가족, 친구 모임",
            "붐비는시간": "12:00~13:30, 18:00~20:00",
            "가격대": "10000~20000원",
            "평점": round(4.0 + (i % 10)/10, 1),
            "위도": 37.5 + i*0.001,
            "경도": 127.0 + i*0.001,
        })

df = pd.DataFrame(rows)
csv_path = base / "restaurants.csv"
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

app_code = r'''import streamlit as st
import pandas as pd

st.set_page_config(page_title="대한민국 맛집 추천", page_icon="🍜", layout="wide")

st.title("🍜 대한민국 지역별 맛집 TOP10")

df = pd.read_csv("restaurants.csv")

region = st.selectbox("📍 지역 선택", sorted(df["지역"].unique()))
region_df = df[df["지역"] == region]

st.subheader(f"🏆 {region} 맛집 TOP10")

restaurant = st.selectbox("🍽️ 맛집 선택", region_df["맛집"].tolist())

info = region_df[region_df["맛집"] == restaurant].iloc[0]

st.markdown("### 📖 맛집 소개")
st.info(info["소개"])

c1, c2 = st.columns(2)
with c1:
    st.write("🍽️ 추천 메뉴:", info["추천메뉴"])
    st.write("👤 추천 대상:", info["추천대상"])
    st.write("⭐ 평점:", info["평점"])
with c2:
    st.write("⏰ 붐비는 시간:", info["붐비는시간"])
    st.write("💰 가격대:", info["가격대"])

st.markdown("### 🗺️ 위치")
st.map(pd.DataFrame({"lat":[info["위도"]],"lon":[info["경도"]]}), zoom=14)

st.markdown("### 📋 지역 전체 맛집 목록")
st.dataframe(region_df[["맛집","추천메뉴","평점"]], use_container_width=True, hide_index=True)
'''
app_path = base / "app.py"
app_path.write_text(app_code, encoding="utf-8")

req_path = base / "requirements.txt"
req_path.write_text("streamlit\npandas\n", encoding="utf-8")

print({"app": str(app_path), "csv": str(csv_path),
