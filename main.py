import streamlit as st
import random

# 🎉 9월 13일 생일 유명인 데이터 (얼굴 이미지 포함)
celebrities = {
    "아이돌": [
        {"name": "연준 (Yeonjun, TXT)", "image": "https://link_to_image1.jpg"},
        {"name": "성찬 (Sungchan, RIIZE)", "image": "https://link_to_image2.jpg"},
        {"name": "현재 (Hyunjae, THE BOYZ)", "image": "https://link_to_image3.jpg"}
    ],
    "배우/방송인": [
        {"name": "릴리 라인하트 (Lili Reinhart)", "image": "https://link_to_image4.jpg"},
        {"name": "타일러 페리 (Tyler Perry)", "image": "https://link_to_image5.jpg"},
        {"name": "자클린 비셋 (Jacqueline Bisset)", "image": "https://link_to_image6.jpg"},
        {"name": "벤 새비지 (Ben Savage)", "image": "https://link_to_image7.jpg"}
    ],
    "해외 뮤지션": [
        {"name": "나일 호란 (Niall Horan)", "image": "https://link_to_image8.jpg"},
        {"name": "플레이보이 카르티 (Playboi Carti)", "image": "https://link_to_image9.jpg"},
        {"name": "피오나 애플 (Fiona Apple)", "image": "https://link_to_image10.jpg"},
        {"name": "피터 세테라 (Peter Cetera)", "image": "https://link_to_image11.jpg"}
    ],
    "유튜버/크리에이터": [
        {"name": "Corey Scherer", "image": "https://link_to_image12.jpg"},
        {"name": "Shion Kaji", "image": "https://link_to_image13.jpg"},
        {"name": "Brizzy Voices", "image": "https://link_to_image14.jpg"},
        {"name": "Gongsam Table", "image": "https://link_to_image15.jpg"},
        {"name": "Ben Skinner", "image": "https://link_to_image16.jpg"},
        {"name": "Risabae", "image": "https://link_to_image17.jpg"}
    ],
    "인플루언서": [
        {"name": "Alanna Lisia Herbert", "image": "https://link_to_image18.jpg"},
        {"name": "Nicky Champa", "image": "https://link_to_image19.jpg"}
    ]
}

# 🎀 헤더
st.markdown(
    """
    <h1 style='text-align:center; font-size:52px; color:#FF1493;'>
      🎂🥳 HAPPY BIRTHDAY PARTY 🎉🎈
    </h1>
    <h3 style='text-align:center; color:#FF69B4;'>
      9월 13일, 전세계 스타들과 함께 파티타임! ✨
