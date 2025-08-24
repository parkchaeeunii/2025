# sentiment_app.py

import streamlit as st
from sklearn.feature_extraction.text import 
from sklearn.naive_bayes import MultinomialNB

# 1. 간단한 학습 데이터 준비
train_texts = [
    "나는 오늘 기분이 너무 좋아", "정말 행복한 하루야", "이 영화 최고였어",
    "너무 짜증나고 화난다", "완전 최악이야", "기분이 우울해"
]
train_labels = ["positive", "positive", "positive", "negative", "negative", "negative"]

# 2. 벡터화 + 모델 학습
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_texts)

model = MultinomialNB()
model.fit(X_train, train_labels)

# 3. Streamlit UI
st.title("📝 간단 감정 분석기")
st.write("문장을 입력하면 AI가 긍정/부정을 판별해줍니다!")

user_input = st.text_input("문장을 입력하세요:", "")

if user_input:
    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)[0]
    
    if prediction == "positive":
        st.success("😊 이 문장은 **긍정적**이에요!")
    else:
        st.error("😡 이 문장은 **부정적**이에요!")
