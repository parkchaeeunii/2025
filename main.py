import streamlit as st

# MBTI 별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 사이언티스트", "🔬 연구원"],
    "ENTP": ["🚀 창업가", "🎯 마케팅 디렉터", "💡 벤처 투자자"],
    "INFJ": ["💖 상담사", "📖 작가", "👩‍🏫 교육자"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "📺 광고 기획자"],
    "ISTJ": ["📚 회계사", "🛡️ 군인", "⚖️ 법률 전문가"],
    "ENFP": ["🎨 디자이너", "📢 홍보 담당자", "✈️ 여행 가이드"],
}

# 페이지 꾸미기
st.set_page_config(page_title="MBTI 직업 추천 💖", page_icon="🌸", layout="centered")

# 헤더
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌸 MBTI 기반 직업 추천 🌸</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFB6C1;'>당신의 성격에 맞는 ✨반짝반짝✨ 직업을 찾아보세요 💕</h3>", unsafe_allow_html=True)

# MBTI 선택
mbti = st.selectbox("💌 당신의 MBTI를 선택해주세요:", options=list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.markdown(f"<h2 style='color: #FF1493;'>💎 {mbti} 유형에게 어울리는 직업은... 💎</h2>", unsafe_allow_html=True)
    for job in job_recommendations[mbti]:
        st.markdown(f"<p style='font-size:18px;'>✨ {job}</p>", unsafe_allow_html=True)

# 하단 메시지
st.markdown("<br><hr><p style='text-align:center; color:#FF69B4;'>💘 당신의 미래는 언제나 반짝반짝 빛날 거예요 ✨</p>", unsafe_allow_html=True)
