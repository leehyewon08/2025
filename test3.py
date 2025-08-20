import streamlit as st
import random

# --- 1. ✨ 페이지 설정 및 화려한 스타일 ✨ ---
st.set_page_config(
    page_title="냉장고가 다 해줄게! 🪄", # 앱 제목
    page_icon="🧊", # 페이지 아이콘
    layout="wide" # 넓은 화면 사용
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
        "조리법": "1. 참치캔의 기름을 최대한 빼주세요. 🥫\n2. 볼에 참치와 마요네즈를 넣고 잘 섞어줍니다. 💖\n3. 따뜻한 밥 위에 만들어둔 참치마요 믹스를 듬뿍 올려요. 🍚\n4. 김 가루를 솔솔 뿌려주면 침샘 자극하는 참치마요덮밥 완성! 🤤",
        "난이도": "세상 쉬움 ✨",
        "시간": "5분 ⏰"
    },
    "된장찌개 🍲": {
        "재료": ["된장", "두부", "애호박", "양파", "파", "고추", "물"],
        "조리법": "1. 애호박, 양파, 고추 등 야채들을 먹기 좋게 썰어 준비합니다. 🔪\n2. 냄비에 물을 붓고 된장을 풀어 넣은 후 끓여주세요. 🥘\n3. 물이 끓으면 손질한 야채와 두부를 넣고 팔팔 끓여줍니다. ♨️\n4. 마지막으로 파와 고추를 넣고 한소끔 더 끓여내면 구수한 된장찌개 완성! 😋",
        "난이도": "보통 😉",
        "시간": "25분 ⏰"
    }
}

# --- 3. 👨‍🍳 도우미 함수들 (코드를 깔끔하게 나누는 비법!) ---

# 레시피 요약 카드를 보여주는 함수 (검색 결과 목록에 사용)
def display_recipe_summary_card(name, recipe_info, user_ingredients_set):
    st.markdown(f"<div class='recipe-summary-card'>", unsafe_allow_html=True)
    
    # 일치하는 재료와 부족한 재료 계산
    recipe_ingredients_set = set(recipe_info["재료"])
    matching_ingredients = recipe_ingredients_set.intersection(user_ingredients_set)
    missing_ingredients = recipe_ingredients_set - user_ingredients_set

    # 일치율 계산
    match_percentage = 0
    if len(recipe_ingredients_set) > 0:
        match_percentage = (len(matching_ingredients) / len(recipe_ingredients_set)) * 100

    # 레시피 이름과 난이도
    st.markdown(f"<h4>{name} <span style='font-size:0.8em; color:#607D8B;'>({recipe_info['난이도']})</span></h4>", unsafe_allow_html=True)
    
    # 진행바 (일치율 표시)
    st.markdown("<div class='progress-container'>", unsafe_allow_html=True)
    st.progress(int(match_percentage) / 100)
    st.markdown(f"<span class='progress-bar-text'>{int(match_percentage)}% 일치!</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 조리 시간 표시
    st.write(f"⏰ 조리 시간: {recipe_info['시간']}")

    # 필요한 재료 목록 표시 (태그 형식)
    st.markdown("<p style='margin-top:10px;'><strong>필요한 재료:</strong>", unsafe_allow_html=True)
    ing_html = "".join([f"<span class='ingredient-tag'>{ing}</span>" for ing in recipe_info['재료']])
    st.markdown(f"{ing_html}</p>", unsafe_allow_html=True)

    # 부족한 재료 표시 (빨간색 태그)
    if missing_ingredients:
        missing_html = "".join([f"<span class='missing-tag'>❌ {ing}</span>" for ing in missing_ingredients])
        st.markdown(f"<p style='color: #E66767;'><strong>⚠️ 부족한 재료:</strong> {missing_html}</p>", unsafe_allow_html=True)
    else:
        st.success("🥳 모든 재료가 충분해요! 바로 만들 수 있어요!")
    
    # 상세 레시피 보기 버튼
    # 버튼 클릭 시 페이지를 'detail_view'로 바꾸고 선택된 레시피 이름을 저장
    if st.button(f"'{name.split(' ')[0]}' 상세 레시피 보기 📖", key=f"view_detail_{name}"):
        st.session_state.page = 'detail_view'
        st.session_state.selected_recipe_name = name
        st.rerun() # 페이지 전환을 위해 Streamlit 앱을 다시 실행

    st.markdown("</div>", unsafe_allow_html=True)

# 레시피 상세 정보를 보여주는 함수 (별도의 '상세 보기' 페이지)
def display_full_recipe_detail(name, recipe_info):
    st.markdown(f"<div class='recipe-detail-card'>", unsafe_allow_html=True)
    st.markdown(f"<h1>{name}</h1>", unsafe_allow_html=True) # 레시피 이름 (이모지 포함)
    
    st.markdown("<h2>재료 🥗</h2>", unsafe_allow_html=True)
    ingredients_html = "".join([f"<span class='ingredient-tag'>{ing}</span>" for ing in recipe_info["재료"]])
    st.markdown(ingredients_html, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True) # 여백

    st.markdown("<h2>조리법 👩‍🍳</h2>", unsafe_allow_html=True)
    st.write(recipe_info["조리법"]) # 조리법은 마크다운으로 깔끔하게 표시
    
    st.markdown(f"<p style='font-size: 1.1em; color: #607D8B;'><strong>난이도:</strong> {recipe_info['난이도']} | <strong>조리 시간:</strong> {recipe_info['시간']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- 4. 🚀 페이지 구성 함수들 (앱의 각 화면을 담당) ---

# 앱의 시작 홈 페이지
def home_page():
    st.title("✨ 냉장고가 다 해줄게! 🪄")
    # 귀여운 이미지 삽입 (Unsplash 예시, 원하는 이미지 URL로 교체 가능!)
    st.image("https://images.unsplash.com/photo-1571432248560-61d02c8427f7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1NzgyMjl8MHwxfHNlYXJjaHwyMHx8Y3V0ZSUyMGZyaWRnZXxlbnwwfHx8fHwxNzIxNzAwOTMyfDA&ixlib=rb-4.0.3&q=80&w=1080", caption="귀요미님의 냉장고가 요리를 도와줄 거예요! 💖", use_column_width=True)
    st.markdown("<h2 style='font-size: 1.5em; color:#607D8B;'>냉장고 속 남은 재료로 쉽고 맛있는 요리를 만들어 봐요! 🥳</h2>", unsafe_allow_html=True)
    
    # "요리 시작하기!" 버튼을 중앙에 배치
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 요리 시작하기!", key="start_app"):
            st.session_state.page = 'main_app' # 버튼 클릭 시 'main_app' 페이지로 전환
            st.rerun()

# 앱의 메인 기능 페이지 (재료 검색, 랜덤 추천)
def main_app_page():
    st.title("어떤 도움이 필요하신가요? 🥕")

    # 모든 레시피에 사용되는 재료들을 목록으로 만듬
    all_possible_ingredients = sorted(list(set(ing for r in RECIPES_DB.values() for ing in r['재료'])))

    # 재료 검색 탭과 랜덤 추천 탭
    tab1, tab2 = st.tabs(["🧊 재료로 레시피 찾기", "🎲 오늘의 메뉴 추천"])
    
    with tab1:
        st.subheader("냉장고 속 재료를 선택해주세요! 👇")
        
        # 선택된 재료 목록을 세션 상태에 저장하여 페이지 이동 시에도 유지되도록 함
        if 'current_ingredients' not in st.session_state:
            st.session_state.current_ingredients = []

        selected_ingredients = st.multiselect(
            "✔ 가지고 있는 재료를 모두 골라주세요:",
            all_possible_ingredients,
            default=st.session_state.current_ingredients, # 이전에 선택된 재료를 기본값으로 설정
            key="ingredient_multiselect"
        )
        st.session_state.current_ingredients = selected_ingredients # 현재 선택된 재료를 세션에 저장

        # 목록에 없는 재료를 사용자가 직접 추가하는 입력창
        new_ingredient = st.text_input("💡 목록에 없는 재료가 있다면 직접 입력 후 Enter:", key="new_ingredient_input")
        if new_ingredient and new_ingredient not in st.session_state.current_ingredients:
            st.session_state.current_ingredients.append(new_ingredient)
            st.success(f"🎉 '{new_ingredient}' 재료를 추가했습니다! 다시 선택 목록을 확인해 주세요.")
            st.rerun() # 재료 목록 업데이트를 위해 앱을 다시 실행 (Streamlit의 특성)

        st.markdown("---") # 구분선

        if st.button("🔍 이 재료로 레시피 찾기!", key="find_recipe_btn"):
            if not st.session_state.current_ingredients: # 선택된 재료가 없으면 경고 메시지
                st.warning("⚠️ 재료를 하나 이상 선택하거나 입력해주세요! 그래야 레시피를 찾아볼 수 있어요. 🥺")
                return # 함수를 여기서 종료하여 더 이상 진행되지 않도록 함

            st.markdown("<h3>✨ 검색 결과</h3>", unsafe_allow_html=True)
            
            user_ingredients_set = set(st.session_state.current_ingredients)
            recipe_candidates = []

            # 모든 레시피를 돌면서 일치하는 재료가 있는 레시피 찾기
            for name, info in RECIPES_DB.items():
                recipe_ingredients_set = set(info["재료"])
                matching_count = len(recipe_ingredients_set.intersection(user_ingredients_set))
                if matching_count > 0: # 하나라도 일치하면 후보에 추가
                    # 일치율 계산
                    match_percentage = (matching_count / len(recipe_ingredients_set)) * 100 if len(recipe_ingredients_set) > 0 else 0
                    recipe_candidates.append((name, info, match_percentage))
            
            # 일치율이 높은 순서로 정렬
            recipe_candidates.sort(key=lambda x: x[2], reverse=True)

            if recipe_candidates: # 찾은 레시피가 있으면 각각의 요약 카드 표시
                for name, info, _ in recipe_candidates:
                    display_recipe_summary_card(name, info, user_ingredients_set)
            else: # 찾은 레시피가 없으면 안내 메시지
                st.info("💡 아쉽지만 입력하신 재료로는 추천할 만한 레시피가 없어요. 😢 다른 재료를 입력해보시거나, '오늘의 메뉴'를 확인해 보세요! ✨")
    
    with tab2:
        st.subheader("오늘 뭐 먹지? 😋 랜덤 메뉴 추천!")
        st.write("재료 고민은 그만! 제가 오늘 뭐 먹을지 딱 정해드릴게요! (재료 입력 없이 랜덤으로 추천합니다.)")
        if st.button("🎲 오늘의 메뉴 추천받기!", key="random_menu_btn"):
            random_recipe_name = random.choice(list(RECIPES_DB.keys())) # 랜덤 레시피 선택
            st.session_state.page = 'detail_view' # 선택된 레시피 상세 보기 페이지로 전환
            st.session_state.selected_recipe_name = random_recipe_name # 레시피 이름 저장
            st.rerun() # 페이지 전환을 위해 앱 다시 실행

    st.markdown("---") # 구분선
    # 메인 앱 페이지에서 홈으로 돌아가는 버튼
    if st.button("🏠 처음 화면으로 돌아가기", key="back_to_home_main"):
        st.session_state.page = 'home'
        st.session_state.current_ingredients = [] # 재료 목록 초기화 (선택했던 것들)
        st.rerun()

# --- 5. ✨ 앱의 메인 실행 흐름 제어 (어떤 페이지를 보여줄지 결정!) ✨ ---
def main():
    # 'page'라는 세션 상태 변수로 현재 보여줄 페이지를 관리
    if 'page' not in st.session_state:
        st.session_state.page = 'home' # 초기값은 'home' 페이지

    # 'page' 값에 따라 해당 페이지 함수를 호출
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'main_app':
        main_app_page()
    elif st.session_state.page == 'detail_view':
        selected_name = st.session_state.get('selected_recipe_name') # 상세 볼 레시피 이름 가져오기
        if selected_name and selected_name in RECIPES_DB:
            display_full_recipe_detail(selected_name, RECIPES_DB[selected_name]) # 상세 레시피 표시
            st.markdown("---")
            # 상세 보기 페이지에서 메인 앱 페이지로 돌아가는 버튼
            if st.button("◀ 목록/이전 화면으로 돌아가기", key="back_from_detail"):
                st.session_state.page = 'main_app'
                st.rerun()
        else: # 레시피 정보를 찾을 수 없을 때
            st.error("앗! 레시피 정보를 찾을 수 없습니다. 😱")
            if st.button("메인으로 돌아가기"):
                st.session_state.page = 'main_app'
                st.rerun()

# Python 스크립트가 직접 실행될 때 main() 함수 호출
if __name__ == "__main__":
    main()
