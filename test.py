import streamlit as st
import random

# 별자리 데이터 (시즌 정보 포함)
constellations = {
    "오리온자리": {"season": "겨울", "img": "orion.jpg"},
    "전갈자리": {"season": "여름", "img": "scorpius.jpg"},
    "사자자리": {"season": "봄", "img": "leo.jpg"},
    "페가수스자리": {"season": "가을", "img": "pegasus.jpg"},
}

st.title("🌌 오늘의 별자리 퀴즈")

# 랜덤으로 오늘의 별자리 선택
today_constellation = random.choice(list(constellations.keys()))
data = constellations[today_constellation]

st.subheader("오늘의 별자리!")
st.image(data["img"], caption=f"이 별자리는 언제 보일까요? 🤔", use_column_width=True)

# 사용자 선택
answer = st.radio("계절을 골라보세요!", ["봄", "여름", "가을", "겨울"])

# 확인 버튼
if st.button("정답 확인"):
    if answer == data["season"]:
        st.success(f"정답! ✅ {today_constellation}는 {data['season']}에 보이는 별자리예요 🌟")
    else:
        st.error(f"아쉽네요 ❌ {today_constellation}는 {data['season']}에 잘 보이는 별자리랍니다.")

