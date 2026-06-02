
import streamlit as st

st.set_page_config(page_title="🍜 지역별 맛집 추천", page_icon="🍔")

st.title("🍜 지역별 맛집 추천")
st.write("지역을 선택하면 추천 맛집 2곳을 알려줄게!")

# 맛집 데이터
restaurants = {
    "서울": [
        {
            "name": "한강버거 🍔",
            "target": "친구들과 수다 떨면서 맛있는 햄버거 먹고 싶은 사람",
            "time": "12:00~13:30 / 18:00~20:00",
            "menu": "치즈버거 세트 🧀"
        },
        {
            "name": "명동칼국수 🍜",
            "target": "든든한 한 끼를 원하는 사람",
            "time": "11:30~13:00",
            "menu": "칼국수 + 만두 🥟"
        }
    ],
    "부산": [
        {
            "name": "광안리회센터 🐟",
            "target": "신선한 해산물을 좋아하는 사람",
            "time": "18:00~21:00",
            "menu": "모둠회 🦐"
        },
        {
            "name": "돼지국밥집 🍲",
            "target": "가성비 좋은 든든한 식사를 원하는 사람",
            "time": "12:00~14:00",
            "menu": "돼지국밥 🐷"
        }
    ],
    "대구": [
        {
            "name": "동성로 떡볶이 🌶️",
            "target": "매운 음식을 좋아하는 사람",
            "time": "16:00~19:00",
            "menu": "치즈 떡볶이 🧀"
        },
        {
            "name": "막창거리 🔥",
            "target": "고기를 좋아하는 사람",
            "time": "18:00~21:00",
            "menu": "소막창 🥩"
        }
    ],
    "인천": [
        {
            "name": "차이나타운 짜장면 🍜",
            "target": "중식 좋아하는 사람",
            "time": "12:00~14:00",
            "menu": "유니짜장 🥢"
        },
        {
            "name": "송도 브런치카페 ☕",
            "target": "사진 찍기 좋아하는 사람",
            "time": "11:00~13:00",
            "menu": "팬케이크 세트 🥞"
        }
    ],
    "광주": [
        {
            "name": "상무지구 고깃집 🥩",
            "target": "고기 러버",
            "time": "18:00~20:30",
            "menu": "삼겹살 🐷"
        },
        {
            "name": "광주 비빔밥 🍚",
            "target": "한식 좋아하는 사람",
            "time": "12:00~13:30",
            "menu": "육회비빔밥 🥩"
        }
    ]
}

region = st.selectbox(
    "📍 지역 선택",
    list(restaurants.keys())
)

st.divider()

st.subheader(f"✨ {region} 추천 맛집")

for i, place in enumerate(restaurants[region], start=1):
    with st.container():
        st.markdown(f"## {i}. {place['name']}")
        st.write(f"👤 **추천 대상** : {place['target']}")
        st.write(f"⏰ **평균 붐비는 시간** : {place['time']}")
        st.write(f"🍽️ **추천 메뉴** : {place['menu']}")
        st.divider()

st.success("😋 맛있는 식사하고 좋은 추억 만들자!")
