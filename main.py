import streamlit as st

# MBTI 별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["전략 컨설턴트", "데이터 사이언티스트", "연구원"],
    "ENTP": ["창업가", "마케팅 디렉터", "벤처 투자자"],
    "INFJ": ["상담사", "작가", "교육자"],
    "ESFP": ["배우", "이벤트 플래너", "광고 기획자"],
    "ISTJ": ["회계사", "군인", "법률 전문가"],
    "ENFP": ["디자이너", "홍보 담당자", "여행 가이드"],
    # 필요시 더 추가 가능
}

# 웹앱 제목
st.title("MBTI 기반 직업 추천 사이트 🎯")
st.write("당신의 MBTI를 선택하면 적절한 직업을 추천해드려요!")

# MBTI 선택 박스
mbti = st.selectbox("당신의 MBTI를 선택하세요:", options=list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.subheader(f"✅ {mbti} 유형 추천 직업")
    for job in job_recommendations[mbti]:
        st.write(f"- {job}")
