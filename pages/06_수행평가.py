import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🍜 지역별 맛집 TOP10",
    page_icon="🍔",
    layout="wide"
)

st.title("🍜 대한민국 지역별 맛집 TOP10")
st.caption("원하는 지역을 선택하면 인기 맛집 TOP10을 확인할 수 있어요!")

restaurant_data = {
    "서울": [
        "명동교자", "을밀대", "진주회관", "광장시장 육회",
        "삼청동수제비", "하동관", "우래옥", "토속촌",
        "한일관", "진옥화할매닭한마리"
    ],
    "부산": [
        "쌍둥이돼지국밥", "할매가야밀면", "해운대암소갈비",
        "기장손칼국수", "금수복국", "동래할매파전",
        "초량밀면", "본전돼지국밥", "개미집", "원조조방낙지"
    ],
    "대구": [
        "왕거미식당", "진골목식당", "미성당",
        "동인동찜갈비", "봉산찜갈비", "태능집",
        "국일따로국밥", "삼송빵집", "중앙떡볶이", "안지랑곱창"
    ],
    "인천": [
        "신포닭강정", "연경", "차이나타운 만다복",
        "송도갈비", "경인면옥", "강화꽃게집",
        "청라쭈꾸미", "부평시장칼국수", "송도국수", "용현동순대"
    ],
    "광주": [
        "송정떡갈비", "영미오리탕", "무등산보리밥",
        "광주한정식", "상무초밥", "유촌포구횟집",
        "전라도밥상", "남도향토음식", "광주국밥", "금남로분식"
    ],
    "대전": [
        "성심당", "태화장", "오씨칼국수",
        "대선칼국수", "광천식당", "진로집",
        "한밭칼국수", "유성불백", "대전국밥", "은행동분식"
    ]
}

selected_region = st.selectbox(
    "📍 지역 선택",
    list(restaurant_data.keys())
)

st.subheader(f"🏆 {selected_region} 맛집 TOP10")

df = pd.DataFrame({
    "순위": range(1, 11),
    "맛집": restaurant_data[selected_region]
})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.info(
    "💡 Tip : 다른 지역을 선택하면 해당 지역의 맛집 TOP10을 확인할 수 있어요!"
)

st.markdown(
    """
    ### 📊 통계
    - 표시 지역 수 : 6개
    - 맛집 수 : 60개
    - 데이터 형식 : 지역별 Top10
    """
)
