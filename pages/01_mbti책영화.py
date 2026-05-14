import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천 ✨",
    page_icon="📚",
    layout="centered"
)

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "books": [
            {
                "title": "사피엔스 🧠",
                "desc": "인류의 역사와 미래를 깊게 생각하게 만드는 책!",
                "personality": "논리적이고 생각 많은 사람 😎"
            },
            {
                "title": "데미안 🌙",
                "desc": "자아를 찾아가는 성장 이야기!",
                "personality": "혼자 생각하는 걸 좋아하는 사람 ✨"
            }
        ],
        "movies": [
            {
                "title": "인터스텔라 🚀",
                "desc": "우주와 과학, 감동까지 다 담긴 영화!",
                "personality": "상상력 많고 분석적인 사람 🌌"
            },
            {
                "title": "인셉션 🌀",
                "desc": "꿈 속 세계를 다루는 반전 영화!",
                "personality": "복잡한 스토리 좋아하는 사람 🔍"
            }
        ]
    },

    "INFP": {
        "books": [
            {
                "title": "어린 왕자 👑",
                "desc": "감성과 따뜻한 메시지가 담긴 명작!",
                "personality": "감수성이 풍부한 사람 💖"
            },
            {
                "title": "미드나잇 라이브러리 📚",
                "desc": "인생의 선택에 대해 생각하게 되는 이야기!",
                "personality": "상상력 많고 공감 잘하는 사람 🌈"
            }
        ],
        "movies": [
            {
                "title": "라라랜드 🎹",
                "desc": "꿈과 사랑을 담은 감성 영화!",
                "personality": "예술 감성 좋아하는 사람 🎨"
            },
            {
                "title": "코코 🎸",
                "desc": "가족과 꿈의 소중함을 느끼게 해주는 영화!",
                "personality": "따뜻한 이야기 좋아하는 사람 🌼"
            }
        ]
    },

    "ENTP": {
        "books": [
            {
                "title": "넛지 🧩",
                "desc": "사람 심리를 재밌게 알려주는 책!",
                "personality": "호기심 많고 아이디어 넘치는 사람 💡"
            },
            {
                "title": "트렌드 코리아 📈",
                "desc": "요즘 유행과 미래 트렌드를 알 수 있는 책!",
                "personality": "새로운 걸 좋아하는 사람 🔥"
            }
        ],
        "movies": [
            {
                "title": "아이언맨 🤖",
                "desc": "재치와 천재성이 폭발하는 히어로 영화!",
                "personality": "유머 있고 자유로운 사람 😆"
            },
            {
                "title": "셜록 홈즈 🔍",
                "desc": "빠른 추리와 두뇌 싸움이 매력적인 영화!",
                "personality": "머리 쓰는 거 좋아하는 사람 🧠"
            }
        ]
    },

    "ESFP": {
        "books": [
            {
                "title": "불편한 편의점 🏪",
                "desc": "사람 냄새 나는 따뜻한 이야기!",
                "personality": "친구 좋아하고 공감 잘하는 사람 😊"
            },
            {
                "title": "아몬드 🌰",
                "desc": "감정을 배우는 특별한 성장 이야기!",
                "personality": "감정 표현에 관심 많은 사람 💛"
            }
        ],
        "movies": [
            {
                "title": "위대한 쇼맨 🎤",
                "desc": "노래와 퍼포먼스가 멋진 영화!",
                "personality": "흥 많고 에너지 넘치는 사람 ✨"
            },
            {
                "title": "겨울왕국 ❄️",
                "desc": "우정과 가족 이야기가 감동적인 영화!",
                "personality": "밝고 감성적인 사람 ☃️"
            }
        ]
    }
}

# 모든 MBTI
all_mbti = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

# 없는 MBTI 기본 데이터 생성
for mbti in all_mbti:
    if mbti not in mbti_data:
        mbti_data[mbti] = {
            "books": [
                {
                    "title": "베스트셀러 책 📘",
                    "desc": "재밌게 읽을 수 있는 인기 책!",
                    "personality": "새로운 걸 좋아하는 사람 😎"
                },
                {
                    "title": "성장 소설 🌱",
                    "desc": "마음이 따뜻해지는 이야기!",
                    "personality": "감성적인 사람 💖"
                }
            ],
            "movies": [
                {
                    "title": "인기 영화 🎬",
                    "desc": "몰입감 넘치는 재미있는 영화!",
                    "personality": "영화 보는 걸 좋아하는 사람 🍿"
                },
                {
                    "title": "감동 영화 🌟",
                    "desc": "여운이 오래 남는 작품!",
                    "personality": "감정 이입 잘하는 사람 😊"
                }
            ]
        }

# 제목
st.title("✨ MBTI 책 & 영화 추천 ✨")
st.write("너의 MBTI에 어울리는 책 📚 과 영화 🎬 를 추천해줄게!")

# 선택창
selected_mbti = st.selectbox(
    "🧠 MBTI를 골라봐!",
    all_mbti
)

# 버튼
if st.button("🔍 추천 보기"):
    data = mbti_data[selected_mbti]

    st.header(f"🌟 {selected_mbti} 추천 결과")

    # 책 추천
    st.subheader("📚 추천 책")
    for book in data["books"]:
        st.markdown("---")
        st.header(book["title"])
        st.write(f"📖 설명: {book['desc']}")
        st.write(f"💖 추천 성격: {book['personality']}")

    # 영화 추천
    st.subheader("🎬 추천 영화")
    for movie in data["movies"]:
        st.markdown("---")
        st.header(movie["title"])
        st.write(f"🍿 설명: {movie['desc']}")
        st.write(f"✨ 추천 성격: {movie['personality']}")

    st.success("😆 재밌게 참고해봐! 취향 찾기에 도움 될 거야 ✨")
