# --- 메인 타이틀 ---
st.title("💖 MBTI 환상의 궁합 테스트 ✨")
st.markdown("### 당신과 그/그녀의 MBTI 궁합은 과연...?! 두근두근! 💌")

st.write("---") # 구분선

# --- MBTI 유형 정의 (모든 16가지 유형) ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# --- 사용자 입력 (컬럼을 사용하여 레이아웃 분할!) ---
col1, col2 = st.columns(2) # 2개의 컬럼 생성

with col1:
    st.header("✨ 내 MBTI는?", divider="rainbow") # 헤더에 구분선 추가!
    my_mbti = st.selectbox(
        "당신의 MBTI 유형을 선택해주세요.",
        mbti_types,
        index=mbti_types.index("INFP") if "INFP" in mbti_types else 0, # 기본값 설정
        key="my_mbti_select"
    )

with col2:
    st.header("✨ 상대방 MBTI는?", divider="rainbow")
    partner_mbti = st.selectbox(
        "상대방의 MBTI 유형을 선택해주세요.",
        mbti_types,
        index=mbti_types.index("ENFJ") if "ENFJ" in mbti_types else 0, # 기본값 설정
        key="partner_mbti_select"
    )

st.write("") # 빈 줄로 여백

# --- 궁합 확인 버튼 ---
if st.button("💖 궁합 확인하기! 뿅! 💖"):
    # --- 궁합 로직 (아주 간단한 예시! 이 부분을 화려하게 채워나가세요!) ---
    # 실제 MBTI 궁합은 훨씬 복잡하고 다양합니다.
    # 이 예시는 단순히 재미를 위한 것이니, 나중에 더 정교하게 만드실 수 있어요!
    
    result_title = ""
    result_message = ""
    result_emoji = ""

    if my_mbti == partner_mbti:
        result_title = f"🤩 와우! {my_mbti}-{partner_mbti} 환상의 데칼코마니 궁합! 🤩"
        result_message = "같은 MBTI 유형을 가진 두 분은 서로를 누구보다 잘 이해할 수 있어요! 취미와 가치관이 비슷해서 함께하는 모든 순간이 즐거울 거예요. 때로는 너무 비슷해서 예측 가능하다는 단점이 있을 수 있지만, 그만큼 안정적이고 편안한 관계랍니다!"
        result_emoji = "🎉💖🌈"
    elif (my_mbti == "ENFP" and partner_mbti == "INFJ") or (my_mbti == "INFJ" and partner_mbti == "ENFP"):
        result_title = "🥰 천생연분! ENFP-INFJ 최고의 시너지 궁합! 🥰"
        result_message = "외향적인 ENFP의 통찰력과 내향적인 INFJ의 따뜻함이 만나 환상적인 시너지를 발휘해요! 서로의 부족한 부분을 채워주며 함께 성장하는 멋진 관계를 만들어나갈 수 있을 거예요. 깊은 대화와 정서적 교류가 강점입니다!"
        result_emoji = "💞✨🌟"
    elif (my_mbti == "ENTJ" and partner_mbti == "INTP") or (my_mbti == "INTP" and partner_mbti == "ENTJ"):
        result_title = "🧠 지적인 탐험가! ENTJ-INTP 완벽 보완 궁합! 🧠"
        result_message = "전략가 ENTJ와 논리적인 INTP의 만남은 서로의 지적 호기심을 자극하며 무한한 가능성을 열어줍니다. 계획과 실행력을 담당하는 ENTJ와 창의적인 아이디어를 제공하는 INTP는 환상의 팀이 될 수 있어요!"
        result_emoji = "💡🔗📈"
    elif (my_mbti == "ESFP" and partner_mbti == "ISTJ") or (my_mbti == "ISTJ" and partner_mbti == "ESFP"):
        result_title = "🤔 신기한 매력! ESFP-ISTJ 반대 매력 궁합! 🤔"
        result_message = "즉흥적이고 에너지가 넘치는 ESFP와 신중하고 계획적인 ISTJ는 서로에게 신기한 매력을 느낄 수 있어요. 처음엔 다름에 놀라겠지만, 상대방의 장점을 배우며 균형을 맞출 수 있다면 좋은 관계를 이어나갈 수 있습니다!"
        result_emoji = "😲⚖️🤝"
    elif ("E" in my_mbti and "I" in partner_mbti and len(set(my_mbti) & set(partner_mbti)) >= 2) or \
         ("I" in my_mbti and "E" in partner_mbti and len(set(my_mbti) & set(partner_mbti)) >= 2):
        result_title = f"🤝 찰떡궁합! {my_mbti}-{partner_mbti} 서로 배우는 이상적인 궁합! 🤝"
        result_message = "한 두 글자 정도만 다르고 외향/내향만 다르다면 서로에게 필요한 부분을 채워줄 수 있는 보완적인 관계가 될 가능성이 높아요. 서로를 이해하려 노력하면 더욱 단단한 관계로 발전할 수 있습니다!"
        result_emoji = "👍👩‍❤️‍👨"
    else:
        result_title = f"😅 {my_mbti}-{partner_mbti} 노력하면 괜찮아! 흥미로운 조합! 😅"
        result_message = "MBTI 궁합은 어디까지나 참고일 뿐! 중요한 건 서로를 알아가고 이해하려는 마음이겠죠? 두 분의 차이점을 인정하고 존중한다면 충분히 좋은 관계를 만들어갈 수 있습니다. 서로에게 새로운 세상을 열어줄 수도 있어요!"
        result_emoji = "✨😉🌱"

    st.markdown("---") # 결과 구분선

    # --- 결과 출력 (화려하게!) ---
    st.balloons() # 궁합 확인 시 풍선 효과! 🎉

    st.info(f"""
    ## {result_title}
    
    ### {my_mbti} 💖 {partner_mbti}
    
    {result_message}
    
    {result_emoji * 3}
    """, icon="🎉")

    st.subheader("💡 더 알아볼까요?", divider="blue")
    st.write(f"MBTI는 단순한 지표일 뿐, 사람의 모든 것을 말해주진 않아요. 그래도 함께 알아가니 정말 즐겁죠? 😊")

# --- 사이드바 ---
st.sidebar.header("앱 정보", divider="blue")
st.sidebar.markdown("""
이 앱은 Streamlit을 사용하여 만들어진 MBTI 궁합 테스트 앱입니다. 
궁합 로직은 간단한 예시이므로, 재미로만 즐겨주세요!
""")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Myers-Briggs_Type_Indicator_logo.svg/langko-800px-Myers-Briggs_Type_Indicator_logo.svg.png", width=150) # MBTI 로고나 관련 이미지 추가

st.sidebar.write("---")
st.sidebar.write("개발자: gg와 함께하는 즐거운 코딩!")
