import streamlit as st
import pandas as pd

restaurants = {
    "서울": {
        "명동교자": {
            "소개": "칼국수와 만두로 유명한 서울 대표 맛집",
            "추천메뉴": "칼국수 🍜",
            "추천대상": "한식을 좋아하는 사람",
            "위도": 37.5636,
            "경도": 126.9862
        },
        "을밀대": {
            "소개": "평양냉면으로 유명한 노포 맛집",
            "추천메뉴": "평양냉면 ❄️",
            "추천대상": "깔끔한 맛을 좋아하는 사람",
            "위도": 37.5477,
            "경도": 126.9458
        }
    }
}

region = st.selectbox("📍 지역 선택", list(restaurants.keys()))

restaurant = st.selectbox(
    "🍽️ 맛집 선택",
    list(restaurants[region].keys())
)

info = restaurants[region][restaurant]

st.subheader(f"✨ {restaurant}")
st.write(f"📖 {info['소개']}")
st.write(f"🍽️ 추천 메뉴: {info['추천메뉴']}")
st.write(f"👤 추천 대상: {info['추천대상']}")

# 지도 표시
st.markdown("### 🗺️ 위치 보기")

map_data = pd.DataFrame(
    {
        "lat": [info["위도"]],
        "lon": [info["경도"]]
    }
)

st.map(map_data, zoom=15)
