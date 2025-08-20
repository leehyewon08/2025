import streamlit as st
import random

# --- 1. 페이지 기본 설정 및 스타일 ---
st.set_page_config(
    page_title="냉장고를 부탁해!",
    page_icon="🍳",
    layout="wide" # 넓은 화면 사용
)

st.markdown("""
<style>
    /* 전체 배경색 */
    .main {
        background-color: #FFF5E4; /* 연한 노랑색 계열 */
    }
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FFD1D1; /* 연한 분홍색 */
        color: #594545; /* 어두운 갈색 글씨 */
        border-radius: 20px; /* 둥근 모서리 */
        border: none; /* 테두리 없음 */
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer; /* 마우스 오버 시 커서 변경 */
        transition: all 0.3s ease; /* 부드러운 전환 효과 */
    }
    .stButton>button:hover {
        background-color: #FF9494; /* 마우스 오버 시 진한 분홍색 */
        color: white; /* 글씨색 흰색으로 변경 */
        transform: translateY(-2px); /* 살짝 위로 뜨는 효과 */
    }
    /* 제목 스타일 */
    h1, h2, h3 {
        color: #594545; /* 어두운 갈색 */
        text-align: center; /* 가운데 정렬 */
    }
    /* 레시피 카드 스타일 */
    .recipe-card {
        background-color: white; /* 흰색 배경 */
        border-radius: 15px; /* 둥근 모서리 */
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 그림자 효과 */
    }
    /* 재료 태그 스타일 */
    .ingredient-tag {
        background-color: #FFD1D1; /* 연한 분홍색 */
        color: #594545; /* 어두운 갈색 글씨 */
        padding: 5px 10px;
        border-radius: 10px;
        margin: 3px;
        display: inline-block; /* 한 줄에 여러 개 표시 */
    }
</style>
""", unsafe_allow_html=True)


# --- 2. 레시피 데이터베이스 (아주 간단하게 구성) ---
# 이미지 대신 귀여운 이모지를 사용합니다.
RECIPES_DB = {
    "김치볶음밥": {
        "재료": ["김치", "밥", "계란", "파", "식용유"],
        "조리법": "1. 김치를 잘게 썬다.\n2. 팬에 식용유 두르고 김치 볶기.\n3. 밥 넣고 볶기.\n4. 계란 넣고 더 볶기.\n5. 파 뿌려 완성!",
        "난이도": "쉬움",
        "시간": "15분",
        "아이콘": "🍚"
    },
    "계란말이": {
        "재료": ["계란", "파", "당근", "소금", "식용유"],
        "조리법": "1. 계란 풀어 소금 넣고 섞기.\n2. 파, 당근 잘게 썰어 넣기.\n3. 팬에 식용유 두르고 계란물 부어 익히기.\n4. 익으면 말아 완성!",
        "난이도": "쉬움",
        "시간": "10분",
        "아이콘": "🍳"
    },
    "참치마요덮밥": {
        "재료": ["참치캔", "마요네즈", "밥", "김"],
        "조리법": "1. 참치캔 기름 빼기.\n2. 참치에 마요네즈 넣어 섞기.\n3. 밥 위에 참치마요 올리기.\n4. 김 가루 뿌려 완성!",
        "난이도": "아주 쉬움",
        "시간": "5분",
        "아이콘": "🐟"
    },
    "된장찌개": {
        "재료": ["된장", "두부", "애호박", "양파", "파", "고추", "물"],
        "조리법": "1. 야채 썰기.\n2. 냄비에 물 붓고 된장 풀기.\n3. 야채와 두부 넣고 끓이기.\n4. 파, 고추 넣고 마무리.",
        "난이도": "보통",
        "시간": "25분",
        "아이콘": "🍲"
    }
}

# --- 3. 도우미 함수 ---

# 레시피 상세 정보를 보여주는 함수
def display_recipe_card(name, recipe_info):
    st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
    st.markdown(f"<h2>{recipe_info['아이콘']} {name}</h2>", unsafe_allow_html=True)
    st.markdown("<h4>재료</h4>", unsafe_allow_html=True)
    ingredients_html = "".join([f"<span class='ingredient-tag'>{ing}</span>" for ing in recipe_info["재료"]])
    st.markdown(ingredients_html, unsafe_allow_html=True)
    st.markdown("<h4>조리법</h4>", unsafe_allow_html=True)
    st.write(recipe_info["조리법"])
    st.markdown(f"<p><strong>난이도:</strong> {recipe_info['난이도']} | <strong>조리 시간:</strong> {recipe_info['시간']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 재료에 맞는 레시피를 찾아주는 함수
def find_matching_recipes(user_ingredients):
    st.markdown("<h3>🔍 검색 결과</h3>", unsafe_allow_html=True)
    
    found_recipes = []
    user_ingredients_set = set(user_ingredients) # 사용자가 입력한 재료를 set으로 변환 (검색 효율 증대)

    for recipe_name, recipe_info in RECIPES_DB.items():
        recipe_ingredients_set = set(recipe_info["재료"])
        
        # 사용자가 가진 재료와 레시피의 재료 중 겹치는 것
        matching_count = len(recipe_ingredients_set.intersection(user_ingredients_set))
        
        # 레시피에 필요한 재료 중 사용자가 없는 것
        missing_ingredients = recipe_ingredients_set - user_ingredients_set
        
        # 레시피 재료 대비 일치율 계산
        if len(recipe_ingredients_set) > 0:
            match_percentage = (matching_count / len(recipe_ingredients_set)) * 100
        else:
            match_percentage = 0 # 재료 없는 레시피는 없음
            
        # 하나라도 재료가 일치하면 후보에 추가
        if matching_count > 0:
            found_recipes.append({
                "name": recipe_name,
                "info": recipe_info,
                "percentage": match_percentage,
                "missing": list(missing_ingredients) # 다시 list로 변환하여 표시
            })
    
    # 일치율이 높은 순서로 정렬
    found_recipes.sort(key=lambda x: x["percentage"], reverse=True)

    if found_recipes:
        for recipe in found_recipes:
            st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
            st.markdown(f"<h4>{recipe['info']['아이콘']} {recipe['name']} (일치율: {recipe['percentage']:.0f}%)</h4>", unsafe_allow_html=True)
            
            # 진행바 추가
            st.progress(int(recipe['percentage']) / 100) # Streamlit progress bar는 0~1 사이 값
            
            st.markdown("<p><strong>필요한 재료:</strong> " + ", ".join(recipe['info']['재료']) + "</p>", unsafe_allow_html=True)
            
            if recipe['missing']:
                st.markdown("<p style='color: #E66767;'><strong>✨ 부족한 재료:</strong> " + ", ".join(recipe['missing']) + "</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color: #62A87C;'>👍 모든 재료가 충분해요!</p>", unsafe_allow_html=True)
            
            # 상세 레시피 보기 버튼
            if st.button(f"'{recipe['name']}' 상세 레시피 보기", key=f"detail_{recipe['name']}"):
                st.session_state['selected_recipe'] = recipe['name']
                st.session_state['page'] = 'detail'
                st.rerun() # 페이지 전환을 위해 재실행
            
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("💡 아쉽지만 입력하신 재료로는 추천할 만한 레시피가 없어요. 다른 재료를 입력해보시거나, '오늘의 추천 메뉴'를 확인해 보세요! ㅠㅠ")

# --- 4. 메인 애플리케이션 흐름 ---
def main():
    # 세션 상태 초기화 (페이지 전환을 위함)
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    # 첫 화면: 시작하기 버튼
    if st.session_state['page'] == 'home':
        st.markdown("<h1>냉장고를 부탁해! 🍳</h1>", unsafe_allow_html=True)
        st.image("https://raw.githubusercontent.com/streamlit/docs/main/docs/static/streamlit-logo-full-color-black.png", width=200) # 샘플 이미지 (원하는 귀여운 이미지 URL로 교체하세요!)
        st.markdown("<p style='text-align: center; font-size: 1.2em;'>냉장고 속 남은 재료로 맛있는 요리를 만들어 봐요!</p>", unsafe_allow_html=True)
        
        # 가운데 정렬을 위한 꼼수
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("시작하기", key="start_app_button"):
                st.session_state['page'] = 'main_app'
                st.rerun()

    # 메인 앱 화면
    elif st.session_state['page'] == 'main_app':
        st.markdown("<h1>어떤 도움이 필요하신가요? 🥕</h1>", unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["재료로 레시피 찾기", "오늘의 추천 메뉴"])
        
        with tab1:
            st.markdown("<h3>🧊 냉장고 속 재료 입력하기</h3>", unsafe_allow_html=True)
            # 모든 재료 옵션 가져오기
            all_possible_ingredients = sorted(list(set(ing for r in RECIPES_DB.values() for ing in r['재료'])))

            # 멀티셀렉트로 재료 선택
            selected_ingredients = st.multiselect(
                "냉장고에 있는 재료를 선택해주세요:",
                all_possible_ingredients,
                key="ingredient_selector"
            )

            # 직접 재료 추가 입력창 (Enter로 추가 가능)
            new_ingredient_input = st.text_input("목록에 없는 재료를 직접 입력 후 Enter를 누르세요 (예: 고구마)", key="new_ingredient_text")
            
            # 입력된 재료가 있고, 아직 선택 목록에 없으면 추가
            if new_ingredient_input and new_ingredient_input not in selected_ingredients:
                selected_ingredients.append(new_ingredient_input)
                # 스트림릿의 한계로 인해, multiselect 위젯이 이 변경을 바로 반영하지는 않습니다.
                # 그러나 find_matching_recipes 함수에서는 이 모든 selected_ingredients를 활용합니다.
                st.success(f"'{new_ingredient_input}' 재료를 추가했습니다!")

            # 레시피 찾기 버튼
            if st.button("레시피 찾기", key="find_recipe_button"):
                if selected_ingredients:
                    find_matching_recipes(selected_ingredients)
                else:
                    st.warning("재료를 하나 이상 선택하거나 입력해주세요!")

        with tab2:
            st.markdown("<h3>🍽️ 오늘의 추천 메뉴</h3>", unsafe_allow_html=True)
            st.write("재료 입력 없이 맛있는 메뉴를 추천해 드려요! 랜덤으로 하나를 골라드려요.")
            if st.button("메뉴 추천받기", key="random_menu_button"):
                random_recipe_name = random.choice(list(RECIPES_DB.keys()))
                display_recipe_card(random_recipe_name, RECIPES_DB[random_recipe_name])
                st.markdown("<br>", unsafe_allow_html=True) # 공백 추가
                if st.button("다른 메뉴 추천받기", key="another_random_button"):
                    st.rerun() # 버튼 누르면 다시 추천 (페이지 새로고침)
        
        # 홈으로 돌아가기 버튼
        if st.button("🏠 홈으로 돌아가기", key="back_to_home"):
            st.session_state['page'] = 'home'
            st.rerun()

    # 레시피 상세 페이지
    elif st.session_state['page'] == 'detail':
        selected_recipe_name = st.session_state.get('selected_recipe')
        if selected_recipe_name and selected_recipe_name in RECIPES_DB:
            display_recipe_card(selected_recipe_name, RECIPES_DB[selected_recipe_name])
        else:
            st.error("레시피 정보를 찾을 수 없습니다.")
        
        if st.button("◀ 목록으로 돌아가기", key="back_to_main_app"):
            st.session_state['page'] = 'main_app'
            st.rerun()

# --- 5. 앱 실행 ---
if __name__ == "__main__":
    main()
