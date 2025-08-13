import streamlit as st

# --- 1. 페이지 설정 및 기본 테마 꾸미기 (화려함 추가!) ---
st.set_page_config(
    page_title="💖 나의 MBTI 짝꿍 찾기! 💖",
    page_icon="✨",
    layout="centered", # 앱 콘텐츠가 중앙에 넓게 표시되도록 설정
    initial_sidebar_state="expanded" # 사이드바를 기본으로 열어둠
)

# --- 2. 커스텀 CSS (더 화려하게 꾸미고 싶을 때 사용!) ---
# 배경 이미지, 버튼 색상, 글꼴 등을 변경하여 더욱 화려하게 꾸밀 수 있습니다.
# (Tip: 웹에서 저작권 걱정 없는 예쁜 배경 이미지를 찾아 URL을 변경해 보세요!)
st.markdown(
    """
    <style>
    /* 전체 앱 배경 설정 */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1510972527921-ce1300079447?q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1920&h=1080"); /* 예시 이미지, 원하시는 이미지 URL로 변경 가능 */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* 배경 스크롤 안 되게 고정 */
        color: #333; /* 기본 텍스트 색상 */
    }

    /* 제목 및 부제목 스타일 */
    h1 {
        color: #FF69B4; /* 핫핑크 */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* 그림자 효과 */
        text-align: center;
    }
    h3 {
        color: #FF69B4; /* 핫핑크 */
        text-align: center;
    }
    h2 {
        color: #8A2BE2; /* 보라색 */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* Streamlit selectbox (선택 상자) 배경 및 테두리 */
    div[data-testid="stSelectbox"] > div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.7); /* 투명한 흰색 */
        border-radius: 10px;
        border: 2px solid #FFC0CB; /* 연한 핑크 테두리 */
        padding: 5px;
    }
    div[data-testid="stSelectbox"] > label {
        color: #4B0082; /* 남색 */
        font-weight: bold;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FFD700; /* 황금색 */
        color: #8B0000; /* 어두운 빨강 */
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #FF69B4; /* 핫핑크 테두리 */
        padding: 10px 25px;
        transition: all 0.3s ease; /* 호버 효과 부드럽게 */
        box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #FFC0CB; /* 연한 핑크로 변경 */
        color: #A52A2A; /* 갈색으로 변경 */
        border: 2px solid #8B0000; /* 어두운 빨강 테두리 */
        transform: translateY(-3px); /* 살짝 위로 뜨는 효과 */
        box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
    }

    /* 결과 메시지 (st.info, st.success, st.warning, st.error) */
    .stAlert {
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        font-size: 1.1em;
        line-height: 1.6;
        box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease-out; /* 페이드인 애니메이션 */
    }
    .stAlert.st-dg { /* info (기본 하늘색) */
        background-color: rgba(220, 240, 255, 0.9); /* 연한 하늘색 투명 */
        border: 2px solid #6495ED; /* 콘플라워 블루 */
    }
    .stAlert.st-dn { /* success (기본 초록색) */
        background-color: rgba(220, 255, 220, 0.9); /* 연한 초록색 투명 */
        border: 2px solid #3CB371; /* 미디움 씨 그린 */
    }
    .stAlert.st-d { /* warning (기본 주황색) */
        background-color: rgba(255, 250, 220, 0.9); /* 연한 노랑색 투명 */
        border: 2px solid #FFD700; /* 황금색 */
    }
    .stAlert.st-dx { /* error (기본 빨강색) */
        background-color: rgba(255, 220, 220, 0.9); /* 연한 빨강색 투명 */
        border: 2px solid #DC143C; /* 크림슨 레드 */
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 3. MBTI 유형 정의 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI 유형별 설명 (st.expander 활용 예정)
mbti_descriptions = {
    "ISTJ": "청렴결백한 논리주의자 (세상의 소금형)",
    "ISFJ": "용감한 수호자 (임금 뒤편의 권력형)",
    "INFJ": "선의의 옹호자 (예언자형)",
    "INTJ": "전략가 (과학자형)",
    "ISTP": "만능 재주꾼 (백과사전형)",
    "ISFP": "호기심 많은 예술가 (성인군자형)",
    "INFP": "열정적인 중재자 (잔다르크형)",
    "INTP": "논리적인 사색가 (아이디어 뱅크형)",
    "ESTP": "모험을 즐기는 사업가 (수완 좋은 활동가형)",
    "ESFP": "자유로운 영혼의 연예인 (사교적인 유형)",
    "ENFP": "재기발랄한 활동가 (스파크형)",
    "ENTP": "논쟁을 즐기는 변론가 (발명가형)",
    "ESTJ": "엄격한 관리자 (사업가형)",
    "ESFJ": "사교적인 외교관 (친선 도모형)",
    "ENFJ": "정의로운 사회 운동가 (언변능숙형)",
    "ENTJ": "대담한 통솔자 (지도자형)"
}

# --- 4. MBTI 궁합 로직 (아주 간단한 예시! 이 부분을 화려하게 채워나가세요!) ---
# 실제 MBTI 궁합은 매우 다양하고 복잡하므로, 아래는 앱의 재미를 위한 단순화된 예시입니다.
# 더 많은 궁합 정보를 추가하거나, 정교한 로직을 만들 수 있어요!
def get_mbti_compatibility(mbti1, mbti2):
    # 같은 MBTI
    if mbti1 == mbti2:
        return {
            "level": "perfect",
            "title": f"💖 환상의 데칼코마니! {mbti1}-{mbti2} 💖",
            "message": f"같은 유형이라서 누구보다 서로를 잘 이해할 수 있어요! 취미와 가치관이 비슷해서 안정적이고 편안한 관계를 만들어갈 수 있습니다.",
            "emoji": "🌟🌟🌟"
        }

    # 천생연분 궁합 (예시)
    # 실제 MBTI 궁합표를 기반으로 '최고의 궁합'을 직접 설정할 수 있습니다.
    best_matches = {
        frozenset({"ENFP", "INFJ"}), frozenset({"ENFJ", "INFP"}),
        frozenset({"ENTJ", "INTP"}), frozenset({"ESTJ", "ISTP"}),
        frozenset({"ESFJ", "ISFP"}), frozenset({"ESFP", "ISTJ"}),
        frozenset({"ENFP", "INTJ"}), frozenset({"ESTP", "INFJ"}), # 추가 궁합
    }
    
    # 두 MBTI 유형을 정렬하여 frozenset으로 만들어 비교 (양방향 체크 위함)
    current_pair = frozenset({mbti1, mbti2})

    if current_pair in best_matches:
        return {
            "level": "perfect",
            "title": f"😍 천생연분 케미! {mbti1}-{mbti2} 최고의 조합! 😍",
            "message": "서로의 부족한 부분을 완벽하게 채워주는 궁합이에요! 환상적인 시너지를 발휘하며 함께 성장할 수 있습니다. 깊은 이해와 존중이 관계를 더욱 빛나게 할 거예요!",
            "emoji": "💖💞✨"
        }
    
    # "성장 가능성 높은" 궁합 (예시: 한두 글자만 다른 경우)
    diff_count = 0
    for i in range(4):
        if mbti1[i] != mbti2[i]:
            diff_count += 1

    if diff_count <= 1: # 1글자만 다른 경우 (예: INFJ vs INFP)
         return {
            "level": "good",
            "title": f"👍 찰떡궁합! {mbti1}-{mbti2} 서로 배우는 이상적인 궁합! 👍",
            "message": "비슷하면서도 다른 매력으로 서로에게 새로운 시야를 열어줄 수 있어요. 서로를 존중하고 이해하려 노력한다면 더욱 단단한 관계로 발전할 수 있습니다!",
            "emoji": "🤝😊🌱"
        }

    # 상호 보완적인 궁합 (예시: 첫 글자(E/I)만 다르고 나머지 3글자가 같을 때)
    if (mbti1[1:] == mbti2[1:]) and (mbti1[0] != mbti2[0]):
        return {
            "level": "good",
            "title": f"💫 반대 매력에 끌린다! {mbti1}-{mbti2} 흥미로운 균형 궁합! 💫",
            "message": "외향형과 내향형의 만남으로 서로 다른 에너지를 교환하며 균형을 이룰 수 있습니다. 때로는 차이점이 매력이 될 수 있어요!",
            "emoji": "☯️✨"
        }

    # "노력 필요" 궁합 (예시: 상대적으로 충돌 가능성이 높은 경우)
    challenging_pairs = {
        frozenset({"ENTP", "ISFJ"}), frozenset({"ESFP", "INTJ"}),
        frozenset({"INFP", "ESTJ"}), frozenset({"ISTP", "ENFJ"}),
        frozenset({"ENTP", "ISTJ"}) # 추가
    }
    if current_pair in challenging_pairs:
        return {
            "level": "needs_effort",
            "title": f"😅 노력하면 괜찮아! {mbti1}-{mbti2} 신기한 매력 궁합! 😅",
            "message": "서로 너무 달라서 처음엔 어려울 수 있어요. 하지만 차이점을 이해하고 존중하려는 노력이 있다면 서로에게 좋은 자극이 될 수 있답니다! 대화와 인내가 중요해요.",
            "emoji": "💪🧐"
        }

    # 일반적인 궁합 (위에 해당하지 않는 모든 경우)
    return {
        "level": "average",
        "title": f"😊 {mbti1}-{mbti2} 평범하지만 특별한 가능성의 궁합! 😊",
        "message": "MBTI 궁합은 어디까지나 참고일 뿐, 가장 중요한 건 서로를 알아가고 이해하려는 마음이죠! 두 분의 아름다운 스토리를 직접 만들어나가세요.",
        "emoji": "🌈💖"
    }

# --- 5. 메인 타이틀 ---
st.title("💖 나의 MBTI 짝꿍 찾기! ✨")
st.markdown("### 나의 MBTI 유형과 가장 잘 어울리는 짝꿍은 누구일까?! 💌")

st.write("---") # 구분선

# --- 6. 사용자 입력 (컬럼을 사용하여 레이아웃 분할!) ---
col1, col2 = st.columns(2) # 2개의 컬럼 생성

with col1:
    st.header("나의 MBTI", divider="violet") # 헤더에 구분선 추가!
    my_mbti = st.selectbox(
        "당신의 MBTI 유형을 선택해주세요.",
        mbti_types,
        index=mbti_types.index("ENFP"), # 기본값 설정
        key="my_mbti_select"
    )
    with st.expander(f"✨ {my_mbti} 유형은?"):
        st.write(mbti_descriptions.get(my_mbti, "설명 없음"))


with col2:
    st.header("짝꿍 MBTI", divider="violet")
    partner_mbti = st.selectbox(
        "짝꿍의 MBTI 유형을 선택해주세요.",
        mbti_types,
        index=mbti_types.index("INFJ"), # 기본값 설정
        key="partner_mbti_select"
    )
    with st.expander(f"✨ {partner_mbti} 유형은?"):
        st.write(mbti_descriptions.get(partner_mbti, "설명 없음"))

st.write("") # 빈 줄로 여백

# --- 7. 궁합 확인 버튼 ---
if st.button("💖 궁합 확인하기! 뿅! 💖"):
    # 궁합 로직 호출
    compatibility_result = get_mbti_compatibility(my_mbti, partner_mbti)
    
    st.markdown("---") # 결과 구분선

    # --- 8. 결과 출력 (화려하게!) ---
    st.balloons() # 궁합 확인 시 풍선 효과! 🎉

    result_level = compatibility_result["level"]
    result_title = compatibility_result["title"]
    result_message = compatibility_result["message"]
    result_emoji = compatibility_result["emoji"]

    if result_level == "perfect":
        st.success(f"""
        ## {result_title}
        ### {my_mbti} 💖 {partner_mbti}
        {result_message}
        ## {result_emoji * 3}
        """, icon="✅")
    elif result_level == "good":
        st.info(f"""
        ## {result_title}
        ### {my_mbti} 🤝 {partner_mbti}
        {result_message}
        ## {result_emoji * 3}
        """, icon="ℹ️")
    elif result_level == "average":
        st.info(f"""
        ## {result_title}
        ### {my_mbti} ↔️ {partner_mbti}
        {result_message}
        ## {result_emoji * 3}
        """, icon="✨")
    elif result_level == "needs_effort":
        st.warning(f"""
        ## {result_title}
        ### {my_mbti} ↔️ {partner_mbti}
        {result_message}
        ## {result_emoji * 3}
        """, icon="⚠️")
    else: # 기타 상황에 대한 기본 처리 (여기에 다른 'level'을 추가할 수도 있습니다)
        st.error(f"""
        ## {result_title}
        ### {my_mbti} 💥 {partner_mbti}
        {result_message}
        ## {result_emoji * 3}
        """, icon="❌")

    st.subheader("💡 MBTI는 재미로만! 💡", divider="blue")
    st.write(f"MBTI는 사람의 성격을 완벽하게 설명해주지 않아요. 그래도 함께 알아가니 정말 즐겁죠? 서로를 이해하고 존중하는 마음이 가장 중요하답니다! 😊")
    st.toast("💖 궁합 결과가 나왔어요!", icon="🎉") # 작은 팝업 메시지

# --- 9. 사이드바 ---
st.sidebar.header("앱 정보", divider="blue")
st.sidebar.markdown("""
이 앱은 **Streamlit**을 사용하여 개발된 MBTI 짝꿍 찾기 앱입니다.
선택한 두 MBTI 유형의 궁합을 재미있게 알려드려요! 
""")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Myers-Briggs_Type_Indicator_logo.svg/langko-800px-Myers-Briggs_Type_Indicator_logo.svg.png", width=150) # MBTI 로고나 관련 이미지 추가 (투명 배경 권장)
st.sidebar.write("---")
st.sidebar.write("개발자: gg와 함께하는 즐거운 코딩 프로젝트!")
st.sidebar.info("MBTI 결과는 재미로만 즐겨주세요! 😊", icon="💡")
