import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 💼",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "job": "데이터 분석가 📊",
            "major": "데이터사이언스과, 컴퓨터공학과",
            "personality": "논리적이고 계획적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "건축가 🏛️",
            "major": "건축학과",
            "personality": "창의적이면서 전략적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "INTP": [
        {
            "job": "프로그래머 💻",
            "major": "컴퓨터공학과",
            "personality": "호기심 많고 분석적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "연구원 🔬",
            "major": "생명과학과, 물리학과",
            "personality": "탐구심이 강한 사람",
            "salary": "평균 연봉 약 4,600만원"
        }
    ],
    "ENTJ": [
        {
            "job": "기업 CEO 🏢",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력 있는 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "마케팅 기획자 📈",
            "major": "광고홍보학과",
            "personality": "도전적이고 아이디어가 많은 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ENTP": [
        {
            "job": "광고 기획자 🎨",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 말 잘하는 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "유튜버 🎥",
            "major": "미디어학과",
            "personality": "창의적이고 활동적인 사람",
            "salary": "수익 차이가 매우 큼"
        }
    ],
    "INFJ": [
        {
            "job": "상담사 💖",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "작가 ✍️",
            "major": "문예창작과",
            "personality": "감수성이 풍부한 사람",
            "salary": "수입 차이가 있음"
        }
    ],
    "INFP": [
        {
            "job": "일러스트레이터 🎨",
            "major": "디자인학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "작곡가 🎵",
            "major": "실용음악과",
            "personality": "감성적이고 창의적인 사람",
            "salary": "수입 차이가 있음"
        }
    ],
    "ENFJ": [
        {
            "job": "교사 🍎",
            "major": "교육학과",
            "personality": "사람들을 잘 이끄는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "HR 담당자 🤝",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ENFP": [
        {
            "job": "방송인 🎤",
            "major": "방송연예과",
            "personality": "밝고 에너지 넘치는 사람",
            "salary": "수입 차이가 큼"
        },
        {
            "job": "여행 플래너 ✈️",
            "major": "관광경영학과",
            "personality": "활동적이고 사람 만나는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "ISTJ": [
        {
            "job": "공무원 🏛️",
            "major": "행정학과",
            "personality": "책임감이 강한 사람",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "job": "회계사 💰",
            "major": "회계학과",
            "personality": "꼼꼼하고 정확한 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사 🏥",
            "major": "간호학과",
            "personality": "배려심이 깊은 사람",
            "salary": "평균 연봉 약 4,700만원"
        },
        {
            "job": "사회복지사 🌷",
            "major": "사회복지학과",
            "personality": "도움을 주는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "ESTJ": [
        {
            "job": "경찰관 🚓",
            "major": "경찰행정학과",
            "personality": "책임감 있고 리더십 있는 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "관리자 📋",
            "major": "경영학과",
            "personality": "체계적이고 추진력 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "승무원 ✈️",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "호텔리어 🏨",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 3,900만원"
        }
    ],
    "ISTP": [
        {
            "job": "자동차 정비사 🔧",
            "major": "자동차공학과",
            "personality": "손재주 좋고 현실적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "파일럿 🛫",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 좋은 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ISFP": [
        {
            "job": "플로리스트 🌸",
            "major": "원예학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 3,400만원"
        },
        {
            "job": "패션디자이너 👗",
            "major": "패션디자인학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ESTP": [
        {
            "job": "스포츠 트레이너 🏋️",
            "major": "체육학과",
            "personality": "활동적이고 에너지 넘치는 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "영업직 💼",
            "major": "경영학과",
            "personality": "사람과 소통을 잘하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ESFP": [
        {
            "job": "셰프 🍳",
            "major": "조리학과",
            "personality": "밝고 창의적인 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "배우 🎬",
            "major": "연극영화과",
            "personality": "표현력이 뛰어난 사람",
            "salary": "수입 차이가 큼"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천 서비스 ✨")
st.write("너의 MBTI에 어울리는 직업을 추천해줄게 😎")

# MBTI 선택
selected_mbti = st.selectbox(
    "💡 MBTI를 선택해봐!",
    list(career_data.keys())
)

# 버튼
if st.button("🔍 진로 추천 보기"):
    st.subheader(f"🌟 {selected_mbti} 추천 진로")

    careers = career_data[selected_mbti]

    for career in careers:
        st.markdown("---")
        st.header(career["job"])
        st.write(f"🎓 추천 학과: {career['major']}")
        st.write(f"🧠 잘 맞는 성격: {career['personality']}")
        st.write(f"💰 평균 연봉: {career['salary']}")

    st.success("✨ 미래 진로 선택에 참고해봐! ✨")
