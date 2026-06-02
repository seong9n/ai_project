import streamlit as st

st.set_page_config(page_title="🍜 지역별 맛집 TOP10", page_icon="🍔")

st.title("🍜 지역별 맛집 TOP10")

restaurants = {
    "서울": {
        "명동교자": {
            "소개": "1966년부터 운영된 칼국수 전문점으로 진한 육수와 만두가 유명해요.",
            "추천메뉴": "칼국수 🍜",
            "추천대상": "든든한 한식을 좋아하는 사람"
        },
        "을밀대": {
            "소개": "평양냉면 맛집으로 담백한 육수와 쫄깃한 면발이 특징이에요.",
            "추천메뉴": "평양냉면 ❄️",
            "추천대상": "깔끔한 맛을 좋아하는 사람"
        },
        "우래옥": {
            "소개": "서울을 대표하는 전통 평양냉면 맛집이에요.",
            "추천메뉴": "물냉면 🥢",
            "추천대상": "전통 맛집 탐방을 좋아하는 사람"
        }
    },

    "부산": {
        "쌍둥이돼지국밥": {
            "소개": "부산 대표 돼지국밥 맛집으로 현지인들도 많이 찾는 곳이에요.",
            "추천메뉴": "돼지국밥 🍲",
            "추천대상": "가성비 좋은 식사를 원하는 사람"
        },
        "해운대암소갈비": {
            "소개": "부드러운 갈비와 특별한 양념으로 유명한 부산 명소예요.",
            "추천메뉴": "생갈비 🥩",
            "추천대상": "고기 좋아하는 사람"
        },
        "개미집": {
            "소개": "매콤한 낙곱새로 유명한 부산 대표 맛집이에요.",
            "추천메뉴": "낙곱새 🌶️",
            "추천대상": "매운 음식 좋아하는 사람"
        }
    }
}

region = st.selectbox(
    "📍 지역 선택",
    list(restaurants.keys())
)

restaurant = st.selectbox(
    "🍽️ 맛집 선택",
    list(restaurants[region].keys())
)

info = restaurants[region][restaurant]

st.markdown("---")
st.subheader(f"✨ {restaurant}")

st.write(f"📖 **맛집 소개**")
st.info(info["소개"])

st.write(f"🍽️ **추천 메뉴**")
st.success(info["추천메뉴"])

st.write(f"👤 **추천 대상**")
st.warning(info["추천대상"])
