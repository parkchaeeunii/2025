# weather_app.py

import streamlit as st

# 미리 준비된 날씨 데이터 (예시)
weather_data = {
    "서울": {"날씨": "맑음 ☀️", "기온": "28°C", "습도": "60%"},
    "부산": {"날씨": "흐림 ☁️", "기온": "25°C", "습도": "70%"},
    "대구": {"날씨": "맑음 ☀️", "기온": "30°C", "습도": "55%"},
    "인천": {"날씨": "비 🌧️", "기온": "24°C", "습도": "80%"},
    "광주": {"날씨": "맑음 ☀️", "기온": "27°C", "습도": "65%"},
}

# 앱 제목
st.title("🌦️ 간단 날씨 정보 조회기")

# 도시 선택
city = st.selectbox("도시를 선택하세요:", list(weather_data.keys()))

# 결과 출력
if city:
    st.subheader(f"📍 {city}의 날씨 정보")
    st.write(f"날씨: {weather_data[city]['날씨']}")
    st.write(f"기온: {weather_data[city]['기온']}")
    st.write(f"습도: {weather_data[city]['습도']}")
