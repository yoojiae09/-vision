import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 추천 활동 🎭",
    page_icon="✨",
    layout="centered"
)

# ------------------------
# MBTI별 활동 목록 + 이미지
# ------------------------
mbti_activities = {
    "INTJ": [
        ("📖 SF 소설 읽기", "https://images.unsplash.com/photo-1512820790803-83ca734da794"),
        ("🧩 퍼즐 맞추기", "https://images.unsplash.com/photo-1614852205023-9b88c3ff2717"),
        ("📊 미래 계획 세우기", "https://images.unsplash.com/photo-1584697964199-80f3544f0d3f")
    ],
    "INFP": [
        ("📝 시 쓰기", "https://images.unsplash.com/photo-1529236183243-06ae9910f9f1"),
        ("🎬 감성 영화 보기", "https://images.unsplash.com/photo-1581905764498-9d7e0cfca4f3"),
        ("📓 일기 쓰기", "https://images.unsplash.com/photo-1495446815901-a7297e633e8d")
    ],
    "ENFP": [
        ("🎨 새로운 취미 도전", "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6"),
        ("🎒 즉흥 여행 계획", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
        ("🤣 랜덤 유튜브 탐험", "https://images.unsplash.com/photo-1587691592099-4fbdc7f3b9b0")
    ],
    "ISFJ": [
        ("📸 사진 정리하기", "https://images.unsplash.com/photo-1549924231-f129b911e442"),
        ("💌 편지 쓰기", "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5"),
        ("👨‍👩‍👧 가족과 대화하기", "https://images.unsplash.com/photo-1607746882042-944635dfe10e")
    ],
    "ENTP": [
        ("💡 스타트업 아이디어", "https://images.unsplash.com/photo-1556155092-8707de31f9c4"),
        ("🎤 친구와 토론하기", "https://images.unsplash.com/photo-1600880292089-90e6a561a8ad"),
        ("🔍 흥미로운 다큐 보기", "https://images.unsplash.com/photo-1495020689067-958852a7765e")
    ],
    "ISTP": [
        ("🔧 기계 만지기", "https://images.unsplash.com/photo-1618083703599-7d1c5bdf30c7"),
        ("🚗 드라이브 하기", "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023"),
        ("🪛 조립 장난감", "https://images.unsplash.com/photo-1560169897-fd74a06e3c3a")
    ],
    # 원하는 만큼 MBTI 추가 가능!
}

# 🎉 제목
st.title("😄 MBTI별 심심할 때 추천 활동")
st.markdown("당신의 성격 유형에 맞춰 오늘 뭐하면 좋을지 추천해드릴게요! ✨")

# 👉 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", [""] + list(mbti_activities.keys()))

# 🧠 추천 버튼
if st.button("🎁 추천 받기"):
    if selected_mbti:
        activity, img_url = random.choice(mbti_activities[selected_mbti])
        st.success(f"당신에게 추천하는 활동은... 🎯")
        st.subheader(activity)
        st.image(img_url, use_column_width=True)
    else:
        st.warning("📌 먼저 MBTI를 선택해주세요!")

# 🌈 하단 꾸미기
st.markdown("---")
st.markdown("🧠 *MBTI 기반 추천 알고리즘 v1.0*")
st.caption("✨ Made with Streamlit · 😊 Have fun & take care!")
