import streamlit as st
import random

# ------------------------------
# 🎯 MBTI별 추천 활동 딕셔너리
# ------------------------------
mbti_activities = {
    "INTJ": ["미래 계획 세우기", "SF 소설 읽기", "퍼즐 게임 풀기"],
    "INTP": ["유튜브 강의 보기", "재미있는 이론 분석하기", "실험적인 코드 짜기"],
    "ENTJ": ["비즈니스 아이디어 정리", "생산성 앱 테스트", "전략 게임 플레이"],
    "ENTP": ["스타트업 아이디어 생각해보기", "새로운 취미 도전", "친구와 토론하기"],
    "INFJ": ["자기 성찰 일기 쓰기", "잔잔한 음악 듣기", "조용한 산책"],
    "INFP": ["시 쓰기", "일기 쓰기", "감성적인 영화 보기"],
    "ENFJ": ["친구에게 안부 전화", "봉사 활동 알아보기", "계획 정리"],
    "ENFP": ["랜덤 유튜브 영상 탐험", "즉흥 여행 계획 세우기", "감성 글귀 만들기"],
    "ISTJ": ["청소나 정리하기", "계획 점검", "다큐멘터리 보기"],
    "ISFJ": ["가족과 대화하기", "사진 정리", "편지 쓰기"],
    "ESTJ": ["일정 정리", "생산성 챌린지", "계획표 작성"],
    "ESFJ": ["친구와 통화하기", "SNS 정리", "쿠킹 클래스 찾기"],
    "ISTP": ["도구 만지기", "드라이브", "기계 분해"],
    "ISFP": ["그림 그리기", "음악 듣기", "조용히 산책"],
    "ESTP": ["운동하기", "게임하기", "SNS에서 새 트렌드 찾기"],
    "ESFP": ["노래방 가기", "친구 만나기", "쇼핑하기"]
}

# ------------------------------
# 🌟 Streamlit 앱 UI
# ------------------------------
st.set_page_config(page_title="MBTI 추천", page_icon="🎯", layout="centered")

st.title("😎 MBTI별 심심할 때 추천 활동")

# 사용자가 MBTI를 선택
selected_mbti = st.selectbox("당신의 MBTI는?", [""] + list(mbti_activities.keys()))

# 추천 버튼
if st.button("추천 받기"):
    if selected_mbti:
        activity = random.choice(mbti_activities[selected_mbti])
        st.success(f"✅ 추천 활동: **{activity}**")
    else:
        st.warning("⚠️ 먼저 MBTI를 선택해주세요!")

# 추가 디자인 요소
st.markdown("---")
st.caption("🧠 만든이: 당신! | ❤️ Powered by Streamlit")
