import streamlit as st
import random

# --- 1. ✨ 페이지 기본 설정 및 화려한 스타일 ✨ ---
st.set_page_config(
    page_title="냉장고가 다 해줄게! 🪄", 
    page_icon="🧊",
    layout="wide"
)

# 사용자 경험을 위한 커스텀 CSS (귀여움 + 실용성)
st.markdown("""
<style>
    /* 전체 배경색과 폰트 */
    .main {
        background-color: #FDF7EC; /* 부드러운 미색 배경 */
        font-family: 'Nanum Gothic', sans-serif; /* 폰트 설정 (설치 필요, 없으면 기본 폰트) */
    }
    /* 제목 스타일 */
    h1, h2, h3 {
        color: #D65A31; /* 따뜻한 오렌지 계열 색상 */
        text-align: center;
        margin-bottom: 20px;
    }
    /* 모든 버튼 스타일 */
    .stButton>button {
        background-color: #FFC94A; /* 활기찬 노랑색 버튼 */
        color: #393E46; /* 진한 회색 글씨 */
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.2s ease-in-out; /* 부드러운 전환 효과 */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.15); /* 버튼 그림자 */
    }
    .stButton>button:hover {
        background-color: #FFA500; /* 오버 시 오렌지색 */
        color: white;
        transform: translateY(-2px); /* 살짝 위로 뜨는 효과 */
        box-shadow: 3px 3px 8px rgba(0,0,0,0.25); /* 그림자 강조 */
    }
    /* 레시피 요약 카드 스타일 (검색 결과 리스트) */
    .recipe-summary-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s ease-in-out; /* 살짝 커지는 효과 */
    }
    .recipe-summary-card:hover {
        transform: scale(1.02);
    }
    /* 레시피 상세 카드 스타일 */
    .recipe-detail-card {
        background-color: white;
        border-radius: 15px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    /* 재료 태그 스타일 */
    .ingredient-tag {
        background-color: #FFEBCC; /* 연한 살구색 태그 */
        color: #8D6E63; /* 진한 갈색 글씨 */
        padding: 5px 10px;
        border-radius: 8px;
        margin: 3px;
        display: inline-block;
        font-size: 0.9em;
    }
    /* 부족한 재료 태그 스타일 */
    .missing-tag {
        background-color: #FFCDD2; /* 연한 빨강 태그 */
        color: #B71C1C; /* 진한 빨강 글씨 */
        padding: 5px 10px;
        border-radius: 8px;
        margin: 3px;
        display: inline-block;
        font-size: 0.9em;
        font-weight: bold;
    }
    /* 진행바 컨테이너 (일치율) */
    .progress-container {
        display: flex;
        align-items: center;
        margin-top: 10px;
    }
    .progress-bar-text {
        font-weight: bold;
        color: #D65A31;
        margin-left: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. 🍲 레시피 데이터베이스 (난이도, 시간 추가) ---
RECIPES_DB = {
    "김치볶음밥 🍚": {
        "재료": ["김치", "밥", "계란", "파", "식용유"],
        "조리법": "1. 김치를 잘게 썰어 준비합니다.\n2. 프라이팬에 식용유를 두르고 김치를 달달 볶아요. 🍳\n3. 밥을 넣고 골고루 섞어가며 신나게 볶습니다! 🍚\n4. 마지막으로 계란을 넣고 살짝 더 볶아 마무리하면 완성! 🥚\n5. 취향에 따라 파를 송송 썰어 뿌려주면 더 맛있어요. 🌱",
        "난이도": "아주 쉬움 👍",
        "시간": "15분 ⏰"
    },
    "계란말이 🍳": {
        "재료": ["계란", "파", "당근", "소금", "식용유"],
        "조리법": "1. 계란을 깨트려 소금을 넣고 잘 풀어주세요. 🥣\n2. 파와 당근을 잘게 썰어 계란물에 섞습니다. 🥕\n3. 프라이팬에 식용유를 살짝 두르고 계란물을 얇게 부어 익힙니다. 🔥\n4. 계란이 적당히 익으면 돌돌 말아주면 귀여운 계란말이 완성! 🥢",
        "난이도": "쉬움 😊",
        "시간": "10분 ⏰"
    },
    "참치마요덮밥 🐟": {
        "재료": ["참치캔", "마요네즈", "밥", "김"],
        "조리법": "1. 참치캔의 기름을 최대한 빼주세요. 🥫\n2. 볼에 참치와 마요네즈를 넣고 잘 섞어줍니다. 💖\n3. 따뜻한 밥 위에 만들어둔 참치마요 믹스를 듬뿍 올려요. 🍚\n4. 김 가루를 솔솔
