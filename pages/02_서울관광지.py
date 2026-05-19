import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

# 제목
st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("Folium 지도로 서울의 대표 관광지를 확인해보세요!")

# 서울 중심 지도 생성
seoul_map = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "location": [37.5796, 126.9770],
        "description": "조선 시대의 대표 궁궐"
    },
    {
        "name": "명동",
        "location": [37.5636, 126.9827],
        "description": "쇼핑과 길거리 음식 명소"
    },
    {
        "name": "남산서울타워",
        "location": [37.5512, 126.9882],
        "description": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을",
        "location": [37.5826, 126.9830],
        "description": "전통 한옥 체험 가능"
    },
    {
        "name": "홍대거리",
        "location": [37.5563, 126.9220],
        "description": "젊은 문화와 버스킹 거리"
    },
    {
        "name": "롯데월드타워",
        "location": [37.5131, 127.1025],
        "description": "대한민국 최고층 랜드마크"
    },
    {
        "name": "인사동",
        "location": [37.5740, 126.9850],
        "description": "전통 문화 거리"
    },
    {
        "name": "DDP",
        "location": [37.5665, 127.0092],
        "description": "동대문디자인플라자"
    },
    {
        "name": "한강공원",
        "location": [37.5206, 126.9408],
        "description": "서울 대표 휴식 공간"
    },
    {
        "name": "코엑스",
        "location": [37.5125, 127.0588],
        "description": "별마당도서관으로 유명"
    }
]

# 지도에 마커 추가
for idx, place in enumerate(places, start=1):
    folium.Marker(
        location=place["location"],
        popup=f"""
        <b>{idx}. {place['name']}</b><br>
        {place['description']}
        """,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(seoul_map)

# 지도 출력
st_folium(seoul_map, width=1200, height=600)

# 관광지 리스트
st.subheader("📍 관광지 목록")

for idx, place in enumerate(places, start=1):
    st.write(f"{idx}. {place['name']} - {place['description']}")
