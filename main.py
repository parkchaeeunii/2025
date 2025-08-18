import streamlit as st

# 🎉 9월 13일 생일 연예인/아이돌 리스트
celebrities = {
    "아이돌": [
        "태연 (소녀시대) 💖",
        "장원영 (IVE) 🌸",
        "조슈아 (SEVENTEEN) 🎶",
        "휘인 (마마무) 🎤",
        "리쿠 (NiziU) 🌈",
        "정성찬 (RIIZE) 🌟"  # ✅ 추가
    ],
    "배우/연예인": [
        "신민아 🎬",
        "박해진 🎭",
        "홍수아 💎"
    ],
    "해외 유명인": [
        "릴 야티 (래퍼) 🎧",
        "벤 사플렉 (배우) 🎥"
    ]
}

# 🌟 페이지 꾸미기
st.set_page_config(page_title="9월 13일 생일 연예인 🎂", page_icon="🎉", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎂 9월 13일 생일 연예인/아이돌 찾기 🎂</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFB6C1;'>당신과 같은 날 태어난 스타는 누구일까요? ✨</h3>", unsafe_allow_html=True)

# 카테고리 선택
category = st.radio("🌟 카테고리를 선택하세요:", list(celebrities.keys()))

# 결과 출력
if category:
    st.subheader(f"✨ {category} ✨")
    for celeb in celebrities[category]:
        st.write(f"- {celeb}")

# 🎈 풍선 이벤트
st.balloons()

# 하단 메시지
st.markdown("<hr><p style='text-align:center; color:#FF69B4;'>🌸 당신의 생일은 특별해요! 같은 날 태어난 스타들도 함께 축하합니다 🎉</p>", unsafe_allow_html=True)
