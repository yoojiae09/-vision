import streamlit as st
import random

# ---------------------
# 앱 설정
# ---------------------
st.set_page_config(
    page_title="MBTI 전체 추천 활동 🎁",
    page_icon="🧠",
    layout="wide"
)

st.title("🎯 MBTI별 오늘 뭐 하지?")
st.markdown("MBTI 유형별로 오늘 하면 좋을 활동들을 한 번에 추천해드릴게요! 😊")

# ---------------------
# MBTI별 활동 데이터 (16유형)
# ---------------------
mbti_activities = {
    "INTJ": [
        ("📊 미래 계획 세우기", "https://images.unsplash.com/photo-1584697964199-80f3544f0d3f"),
        ("📖 SF 소설 읽기", "https://images.unsplash.com/photo-1512820790803-83ca734da794"),
        ("🧩 복잡한 전략 게임 즐기기", "https://images.unsplash.com/photo-1614852205023-9b88c3ff2717")
    ],
    "INTP": [
        ("🧠 철학 유튜브 보기", "https://images.unsplash.com/photo-1503676260728-1c00da094a0b"),
        ("🔍 위키 탐험하기", "https://images.unsplash.com/photo-1617088608971-0b2122d7c20d"),
        ("💻 새로운 프로그래밍 언어 공부", "https://images.unsplash.com/photo-1584697964361-2a7f573ddc1a")
    ],
    "ENTJ": [
        ("📈 목표 정리 & 계획표 작성", "https://images.unsplash.com/photo-1581090700227-1e8d64b26c98"),
        ("📚 리더십 관련 책 읽기", "https://images.unsplash.com/photo-1520975918108-7b5866eb374e"),
        ("💼 커리어 로드맵 만들기", "https://images.unsplash.com/photo-1526378722484-df4ec42729ef")
    ],
    "ENTP": [
        ("🎤 친구와 토론하기", "https://images.unsplash.com/photo-1600880292089-90e6a561a8ad"),
        ("💡 스타트업 아이디어 정리", "https://images.unsplash.com/photo-1556155092-8707de31f9c4"),
        ("📺 흥미로운 다큐 보기", "https://images.unsplash.com/photo-1495020689067-958852a7765e")
    ],
    "INFJ": [
        ("🌌 별 보며 산책", "https://images.unsplash.com/photo-1534338580013-382cf0b02233"),
        ("📓 자기 성찰 일기 쓰기", "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70"),
        ("🎧 감성 음악 감상", "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4")
    ],
    "INFP": [
        ("📝 감성 글 쓰기", "https://images.unsplash.com/photo-1529236183243-06ae9910f9f1"),
        ("🎬 힐링 영화 보기", "https://images.unsplash.com/photo-1581905764498-9d7e0cfca4f3"),
        ("📓 일기장 꾸미기", "https://images.unsplash.com/photo-1495446815901-a7297e633e8d")
    ],
    "ENFJ": [
        ("📞 친구에게 안부 전화", "https://images.unsplash.com/photo-1587560699334-bea93391dcef"),
        ("🫂 봉사활동 알아보기", "https://images.unsplash.com/photo-1518611012118-f2434f0bcd40"),
        ("📅 스케줄 정리", "https://images.unsplash.com/photo-1588776814546-6c2b9cd3565d")
    ],
    "ENFP": [
        ("🎒 즉흥 여행 계획", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
        ("🖌️ 취미로 그림 그리기", "https://images.unsplash.com/photo-1616627986075-36f8c08c3430"),
        ("🤣 랜덤 유튜브 탐험", "https://images.unsplash.com/photo-1587691592099-4fbdc7f3b9b0")
    ],
    "ISTJ": [
        ("🧹 집 정리 정돈", "https://images.unsplash.com/photo-1592840747390-9efbbd24b366"),
        ("📋 할 일 목록 정리", "https://images.unsplash.com/photo-1580894894512-fdbcdcca6cb6"),
        ("📘 문서 정리 or 공부", "https://images.unsplash.com/photo-1515777315835-281b94c9589a")
    ],
    "ISFJ": [
        ("💌 편지 쓰기", "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5"),
        ("📸 사진 앨범 정리", "https://images.unsplash.com/photo-1549924231-f129b911e442"),
        ("👨‍👩‍👧 가족과 시간 보내기", "https://images.unsplash.com/photo-1607746882042-944635dfe10e")
    ],
    "ESTJ": [
        ("🧾 가계부 정리하기", "https://images.unsplash.com/photo-1554224154-22dec7ec8818"),
        ("📑 생산성 앱 정리", "https://images.unsplash.com/photo-1554774853-d50fbc4f2d1d"),
        ("📈 투자 계획 세우기", "https://images.unsplash.com/photo-1518544883024-df98df43b72f")
    ],
    "ESFJ": [
        ("🍽️ 친구들과 식사 약속 잡기", "https://images.unsplash.com/photo-1504674900247-0877df9cc836"),
        ("📞 오래된 지인에게 연락하기", "https://images.unsplash.com/photo-1587560699334-bea93391dcef"),
        ("🍪 홈베이킹 도전", "https://images.unsplash.com/photo-1606755962773-3524a2ff9d09")
    ],
    "ISTP": [
        ("🔧 DIY 조립하기", "https://images.unsplash.com/photo-1607623814075-8f27b62b6e87"),
        ("🚗 드라이브 나가기", "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023"),
        ("🎮 기계식 게임 즐기기", "https://images.unsplash.com/photo-1621784564114-6503c59f347f")
    ],
    "ISFP": [
        ("🎨 감성 드로잉", "https://images.unsplash.com/photo-1513364776144-60967b0f800f"),
        ("🎧 음악 감상하며 누워있기", "https://images.unsplash.com/photo-1534921605974-02dc6b12f80c"),
        ("🌿 자연 속 산책", "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0")
    ],
    "ESTP": [
        ("🏋️‍♂️ 운동하러 가기", "https://images.unsplash.com/photo-1558611848-73f7eb4001b7"),
        ("🎮 실시간 게임하기", "https://images.unsplash.com/photo-1603468622562-2b8a5f7d35c5"),
        ("🕺 방에서 클럽처럼 춤추기", "https://images.unsplash.com/photo-1596464716121-624d9e278579")
    ],
    "ESFP": [
        ("🎤 노래방 가기", "https://images.unsplash.com/photo-1585386959984-a4155223f289"),
        ("🛍️ 쇼핑하기", "https://images.unsplash.com/photo-1521334884684-d80222895322"),
        ("💃 친구와 파티하기", "https://images.unsplash.com/photo-1554284126-aa88f22d8b74")
    ]
}

# ---------------------
# 버튼 클릭 시 전체 출력
# ---------------------
if st.button("🎁 모든 MBTI 유형 추천 보기"):
    for mbti, activities in mbti_
