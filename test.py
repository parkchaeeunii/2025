import streamlit as st
import random

# 별자리 데이터 (이름: 이미지 파일명)
constellations = {
    "양자리": "aries.jpg",
    "황소자리": "taurus.jpg",
    "쌍둥이자리": "gemini.jpg",
    "게자리": "cancer.jpg",
    "사자자리": "leo.jpg",
    "처녀자리": "virgo.jpg",
    "천칭자리": "libra.jpg",
    "전갈자리": "scorpius.jpg",
    "사수자리": "sagittarius.jpg",
    "염소자리": "capricorn.jpg",
    "물병자리": "aquarius.jpg",
    "물고기자리": "pisces.jpg",
    "오리온자리": "orion.jpg",
    "페가수스자리": "pegasus.jpg",
    "카시오페이아자리": "cassiopeia.jpg",
    "백조자리": "cygnus.jpg",
}

st.title("🌌 오늘의 별자리 퀴즈")
st.write("사진을 보고 어떤 별자리인지 맞춰보세요!")

# 랜덤으로 별자리 선택
answer_constellation = random.choice(list(constellations.keys()))
img_file = constellations[answer_constellation]

# 이미지 보여주기
st.image(img_file, caption="이 별자리는 무엇일까요? 🤔", use_column_width=True)

# 보기 (랜덤 4지선다)
options = random.sample(list(constellations.keys()), 3)  # 오답 3개 뽑기
options.append(answer_constellation)  # 정답 추가
random.shuffle(options)

choice = st.radio("별자리를 선택하세요:", options)

# 정답 확인 버튼
if st.button("정답 확인"):
    if choice == answer_constellation:
        st.success(f"✅ 정답! 이 별자리는 **{answer_constellation}** 입니다! 🌟")
    else:
        st.error(f"❌ 틀렸습니다! 정답은 **{answer_constellation}** 입니다.")
