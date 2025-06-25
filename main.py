const suggestions = {
  INTJ: ["미래 계획 세우기", "SF 소설 읽기", "퍼즐 게임 풀기"],
  INTP: ["유튜브 강의 보기", "재미있는 이론 분석하기", "실험적인 코드 짜기"],
  ENTJ: ["비즈니스 아이디어 정리", "생산성 앱 테스트", "전략 게임 플레이"],
  ENTP: ["스타트업 아이디어 생각해보기", "새로운 취미 도전", "친구와 토론하기"],
  INFJ: ["자기 성찰 일기 쓰기", "잔잔한 음악 듣기", "조용한 산책"],
  INFP: ["시 쓰기", "일기 쓰기", "감성적인 영화 보기"],
  ENFJ: ["친구에게 안부 전화", "봉사 활동 알아보기", "계획 정리"],
  ENFP: ["랜덤 유튜브 영상 탐험", "즉흥 여행 계획 세우기", "감성 글귀 만들기"],
  ISTJ: ["청소나 정리하기", "계획 점검", "다큐멘터리 보기"],
  ISFJ: ["가족과 대화하기", "사진 정리", "편지 쓰기"],
  ESTJ: ["일정 정리", "생산성 챌린지", "계획표 작성"],
  ESFJ: ["친구와 통화하기", "SNS 정리", "쿠킹 클래스 찾기"],
  ISTP: ["도구 만지기", "드라이브", "기계 분해"],
  ISFP: ["그림 그리기", "음악 듣기", "조용히 산책"],
  ESTP: ["운동하기", "게임하기", "SNS에서 새 트렌드 찾기"],
  ESFP: ["노래방 가기", "친구 만나기", "쇼핑하기"]
};

function getSuggestion() {
  const mbti = document.getElementById("mbti").value;
  const output = document.getElementById("suggestion");

  if (!mbti) {
    output.textContent = "먼저 MBTI를 선택해주세요!";
    return;
  }

  const activities = suggestions[mbti];
  const random = Math.floor(Math.random() * activities.length);
  output.textContent = `추천 활동: ${activities[random]}`;
}
