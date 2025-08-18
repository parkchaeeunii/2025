import streamlit as st
import random

# 🎉 9월 13일 생일 유명인 데이터
celebrities = {
    "아이돌": [
        "Yeonjun (TXT) 🎤",
        "Sungchan (RIIZE) 🌟"
    ],
    "해외 스타": [
        "Playboi Carti (래퍼) 🎵",
        "Niall Horan (가수, One Direction) 🎸",
        "Lili Reinhart (배우) 🌸",
        "Tyler Perry (프로듀서) 🎥",
        "Fiona Apple (싱어송라이터) 🎶",
        "Jacqueline Bisset (배우) 💃",
        "Peter Cetera (Chicago 보컬) 🎼",
        "Ben Savage (배우) 📺"
    ],
    "유튜버/크리에이터": [
        "Corey Scherer (댄스 유튜버) 💃",
        "Shion Kaji (유튜버) 🎥",
        "Brizzy Voices (보이스 유튜버) 🎭",
        "Gongsam Table (요리 유튜버) 🍽️",
        "Ben Skinner (유튜버) 📹",
        "Risabae (뷰티 유튜버) 💄"
    ],
    "인플루언서": [
        "Alanna Lisia Herbert (TikTok 스타) 📱",
        "Nicky Champa (TikTok 인플루언서) 🎵"
    ]
}

# 🌟 페이지 꾸미기
st.set_page_config(page_title="🎂 9월 13일 스타 생일 파티 🎂", page_icon="🎉", layout="centered")

# 🎊 헤더 - 파티 느낌
st.markdown(
    """
    <h1 style='text-align: center; color: #FF1493; font-size: 50px;'>
    🎂🥳 HAPPY BIRTHDAY PARTY 🎉🎈
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h3 style='text-align: center; color: #FF69B4;'>✨ 9월 13일, 오늘은 세상에서 제일 특별한 날! ✨</h3>",
    unsafe_allow_html=True,
)

# 🎉 효과 (풍선 + 눈 내리기)
st.balloons()
st.snow()

# 🎂 랜덤 파티 메시지
party_messages = [
    "🎊 케이크 불 끄고 소원 빌기! 🎂",
    "🎁 선물 잔뜩 받아가는 하루 💝",
    "🥂 모두 모여 건배~ ✨",
    "🎶 음악과 함께 춤추는 파티타임 🎧",
    "🌈 반짝반짝 당신의 날을 축하해요!"
]
st.markdown(f"<h4 style='text-align:center; color:#FF4500;'>{random.choice(party_messages)}</h4>", unsafe_allow_html=True)

# 🎀 카테고리 선택
category = st.selectbox("💖 어떤 스타들이 함께 태어났을까요?", list(celebrities.keys()))

# 🎇 결과 출력
if category:
    st.subheader(f"🎉 {category} 라인업 🎉")
    for celeb in celebrities[category]:
        st.markdown(
            f"<p style='font-size:22px; color:#FF69B4;'>✨ {celeb}</p>",
            unsafe_allow_html=True,
        )

# 🎊 푸터
st.markdown(
    "<hr><p style='text-
