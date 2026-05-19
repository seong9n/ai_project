import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="centered"
)

# 제목
st.title("🇰🇷 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("서울의 인기 관광지를 지도와 함께 확인해보세요!")

# 서울 지도 생성
seoul_map = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 관광지 데이터
places = {
    "경복궁": {
        "location": [37.5796, 126.9770],
        "station": "경복궁역 (3호선)",
        "description": """
- 조선 시대 왕궁으로 한국 전통 건축을 볼 수 있는 대표 관광지입니다.
- 한복을 입고 사진을 찍는 외국인 관광객들이 많습니다.
- 근처 국립민속박물관과 광화문도 함께 구경할 수 있습니다.
- 야간 개장 시 아름다운 조명이 켜져 더욱 인기가 많습니다.
"""
    },

    "명동": {
        "location": [37.5636, 126.9827],
        "station": "명동역 (4호선)",
        "description": """
- 서울 최고의 쇼핑 거리 중 하나입니다.
- 길거리 음식과 화장품 매장이 특히 유명합니다.
- 밤이 되면 화려한 간판과 분위기를 즐길 수 있습니다.
- 외국인 관광객들이 가장 많이 방문하는 장소입니다.
"""
    },

    "남산서울타워": {
        "location": [37.5512, 126.9882],
        "station": "명동역 (4호선)",
        "description": """
- 서울 야경을 한눈에 볼 수 있는 전망대입니다.
- 케이블카를 타고 올라가는 재미도 있습니다.
- 사랑의 자물쇠 명소로 커플들에게 인기가 많습니다.
- 밤에는 더욱 아름다운 서울의 풍경을 감상할 수 있습니다.
"""
    },

    "북촌한옥마을": {
        "location": [37.5826, 126.9830],
        "station": "안국역 (3호선)",
        "description": """
- 한국 전통 한옥이 모여 있는 마을입니다.
- 골목길을 걸으며 한국의 옛 분위기를 느낄 수 있습니다.
- 전통 카페와 공방 체험도 가능합니다.
- 사진 찍기 좋은 장소로 유명합니다.
"""
    },

    "홍대거리": {
        "location": [37.5563, 126.9220],
        "station": "홍대입구역 (2호선)",
        "description": """
- 젊은 문화와 버스킹 공연으로 유명한 거리입니다.
- 맛집과 카페, 다양한 쇼핑 공간이 많습니다.
- 밤에는 활기찬 분위기를 즐길 수 있습니다.
- 외국인 관광객들이 한국 문화를 체험하기 좋은 장소입니다.
"""
    },

    "롯데월드타워": {
        "location": [37.5131, 127.1025],
        "station": "잠실역 (2호선)",
        "description": """
- 대한민국에서 가장 높은 건물입니다.
- 전망대 서울스카이에서 멋진 경치를 볼 수 있습니다.
- 대형 쇼핑몰과 아쿠아리움도 함께 있습니다.
- 가족 단위 관광객들에게 인기가 많습니다.
"""
    },

    "인사동": {
        "location": [37.5740, 126.9850],
        "station": "안국역 (3호선)",
        "description": """
- 전통 기념품과 한식 맛집이 많은 거리입니다.
- 한국 전통 문화를 느끼기 좋은 장소입니다.
- 찻집과 전통 공예품 가게가 유명합니다.
- 외국인 관광객들이 많이 찾는 문화 거리입니다.
"""
    },

    "DDP": {
        "location": [37.5665, 127.0092],
        "station": "동대문역사문화공원역 (2호선)",
        "description": """
- 미래적인 디자인의 건축물로 유명합니다.
- 패션 행사와 전시회가 자주 열립니다.
- 밤에는 LED 장미정원이 아름답습니다.
- 사진 촬영 명소로 인기가 많습니다.
"""
    },

    "한강공원": {
        "location": [37.5206, 126.9408],
        "station": "여의나루역 (5호선)",
        "description": """
- 서울 시민들의 대표 휴식 공간입니다.
- 자전거와 피크닉을 즐길 수 있습니다.
- 밤에는 한강 야경이 매우 아름답습니다.
- 치킨과 라면을 먹으며 휴식을 즐기는 사람이 많습니다.
"""
    },

    "코엑스": {
        "location": [37.5125, 127.0588],
        "station": "삼성역 (2호선)",
        "description": """
- 쇼핑과 전시, 문화생활을 함께 즐길 수 있는 공간입니다.
- 별마당도서관이 특히 유명합니다.
- 주변에 맛집과 카페가 많습니다.
- 실내 관광지라 날씨와 상관없이 방문하기 좋습니다.
"""
    }
}

# 파란색 마커 추가
for name, info in places.items():
    folium.Marker(
        location=info["location"],
        popup=name,
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(seoul_map)

# 지도 출력 (60% 크기 느낌으로 축소)
st_folium(seoul_map, width=700, height=450)

st.divider()

# 관광지 선택
selected_place = st.selectbox(
    "📍 관광지를 선택하세요",
    list(places.keys())
)

# 선택 정보 출력
st.subheader(f"✨ {selected_place}")

st.write(f"🚇 가장 가까운 전철역: {places[selected_place]['station']}")

st.markdown("### 🎈 놀거리 및 특징")
st.write(places[selected_place]["description"])
