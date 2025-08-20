import streamlit as st
import random

# --- 1. ✨ 페이지 기본 설정 및 화려한 스타일 ✨ ---
st.set_page_config(
    page_title="✨ 냉장고가 다 해줄게! 💖", # 앱 제목 변경 및 이모티콘 추가
    page_icon="🍳", # 페이지 아이콘
    layout="wide" # 넓은 화면 사용
)

# HTML/CSS로 귀여운 디자인과 애니메이션 효과 추가
st.markdown("""
<style>
    /* 전체 배경색 */
    .main {
        background-color: #FFF5E4; /* 연한 노랑색 계열로 따뜻한 느낌 */
        font-family: 'Nanum Gothic', sans-serif; /* 예쁜 폰트 (설치 필요, 없으면 기본 폰트) */
    }
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FFD1D1; /* 연한 분홍색 */
        color: #594545; /* 어두운 갈색 글씨 */
        border-radius: 25px; /* 더 둥근 모서리 */
        border: none; /* 테두리 없음 */
        padding: 12px 25px; /* 패딩 증가 */
        font-size: 19px; /* 글씨 크기 증가 */
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease; /* 부드러운 전환 효과 */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* 그림자 효과 추가 */
    }
    .stButton>button:hover {
        background-color: #FF9494; /* 마우스 오버 시 진한 분홍색 */
        color: white;
        transform: translateY(-3px) scale(1.02); /* 살짝 위로 뜨고 커지는 효과 */
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3); /* 그림자 더 강조 */
    }
    /* 제목 스타일 */
    h1, h2, h3 {
        color: #D2691E; /* 좀 더 따뜻한 색상의 제목 */
        text-align: center; /* 가운데 정렬 */
        margin-bottom: 25px; /* 아래 여백 추가 */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1); /* 제목 그림자 */
    }
    /* 레시피 카드 스타일 */
    .recipe-card {
        background-color: white;
        border-radius: 20px; /* 더 둥근 모서리 */
        padding: 30px; /* 패딩 증가 */
        margin: 15px 0;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* 그림자 효과 강조 */
        transition: transform 0.2s ease-in-out; /* 카드에 마우스 오버 시 효과 */
    }
    .recipe-card:hover {
        transform: translateY(-5px); /* 마우스 오버 시 살짝 위로 뜨는 효과 */
    }
    /* 재료 태그 스타일 */
    .ingredient-tag {
        background-color: #FFECB3; /* 밝은 노랑 태그 */
        color: #8B4513; /* 갈색 글씨 */
        padding: 6px 12px;
        border-radius: 15px; /* 더 둥근 태그 */
        margin: 4px;
        display: inline-block;
        font-weight: 600;
        border: 1px solid #FFCC80; /* 테두리 추가 */
    }
    /* 인풋 필드 */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #FFD1D1;
        padding: 10px;
    }
    .stMultiSelect>div>div {
        border-radius: 10px;
        border: 2px solid #FFD1D1;
        padding: 5px;
    }
</style>
""", unsafe_allow_html=True)


# --- 2. 💖 레시피 데이터베이스 (이모티콘으로 표현) 💖 ---
# 실제 앱에서는 이 데이터를 파일이나 DB에서 불러오겠죠?
RECIPES_DB = {
    "김치볶음밥": {
        "재료": ["김치", "밥", "계란", "파", "식용유"],
        "조리법": "1. 김치를 잘게 썰어요.\n2. 팬에 식용유 두르고 김치를 달달 볶아요. 🍳\n3. 밥을 넣고 신나게 볶아요! 🍚\n4. 계란을 넣고 살짝 더 볶으면 완성! 🥚\n5. 파를 솔솔 뿌려주면 더 맛있어요. 🌱",
        "난이도": "아주 쉬움",
        "시간": "15분",
        "아이콘": "🍚"
    },
    "계란말이": {
        "재료": ["계란", "파", "당근", "소금", "식용유"],
        "조리법": "1. 계란을 풀고 소금을 넣어 잘 섞어요. 🥣\n2. 파와 당근을 잘게 썰어 넣어요. 🥕\n3. 프라이팬에 식용유를 두르고 계란물을 부어 익혀요. 🔥\n4. 돌돌 말면 귀여운 계란말이 완성! 🥢",
        "난이도": "쉬움",
        "시간": "10분",
        "아이콘": "🍳"
    },
    "참치마요덮밥": {
        "재료": ["참치캔", "마요네즈", "밥", "김"],
        "조리법": "1. 참치캔의 기름을 쪽 빼요. 🥫\n2. 참치에 마요네즈를 듬뿍 넣어 섞어요. 💖\n3. 따뜻한 밥 위에 참치마요를 쓱쓱 올려요. 🍚\n4. 김 가루를 솔솔 뿌려주면 침샘 자극! 🤤",
        "난이도": "세상 쉬움",
        "시간": "5분",
        "아이콘": "🐟"
    },
    "된장찌개": {
        "재료": ["된장", "두부", "애호박", "양파", "파", "고추", "물"],
        "조리법": "1. 야채들을 먹기 좋게 썰어주세요. 🔪\n2. 냄비에 물 붓고 된장을 풀어 끓여요. 🥘\n3. 손질한 야채와 두부를 넣고 팔팔 끓여주세요. ♨️\n4. 마지막으로 파와 고추를 넣으면 구수한 된장찌개 완성! 😋",
        "난이도": "보통",
        "시간": "25분",
        "아이콘": "🍲"
    }
}

# --- 3. 👩‍🍳 도우미 함수들 👨‍🍳 ---

# 레시피 상세 정보를 보여주는 카드 함수
def display_recipe_card(name, recipe_info):
    st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
    st.markdown(f"<h2>{recipe_info['아이콘']} {name} </h2>", unsafe_allow_html=True) # 더 큰 아이콘과 제목
    
    st.markdown("<h4 style='color: #6A5ACD;'>필요한 재료들: 👇</h4>", unsafe_allow_html=True) # 재료 강조
    ingredients_html = "".join([f"<span class='ingredient-tag'>{ing}</span>" for ing in recipe_info["재료"]])
    st.markdown(ingredients_html, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True) # 여백 추가

    st.markdown("<h4 style='color: #2E8B57;'>만드는 방법: 🧑‍🍳</h4>", unsafe_allow_html=True) # 조리법 강조
    st.write(recipe_info["조리법"])
    
    st.markdown(f"<p style='font-size: 1.1em; color: #800080;'><strong>⏱️ 난이도:</strong> {recipe_info['난이도']} | <strong>⏰ 조리 시간:</strong> {recipe_info['시간']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 재료에 맞는 레시피를 찾아주는 함수
def find_matching_recipes(user_ingredients_list):
    st.markdown("<h3>✨ 레시피 검색 결과 🔍</h3>", unsafe_allow_html=True)
    
    found_recipes = []
    user_ingredients_set = set(user_ingredients_list) # 사용자 재료를 set으로 변환

    for recipe_name, recipe_info in RECIPES_DB.items():
        recipe_ingredients_set = set(recipe_info["재료"])
        
        matching_count = len(recipe_ingredients_set.intersection(user_ingredients_set))
        missing_ingredients = recipe_ingredients_set - user_ingredients_set
        
        # 일치율 계산 (0으로 나누는 오류 방지)
        if len(recipe_ingredients_set) > 0:
            match_percentage = (matching_count / len(recipe_ingredients_set)) * 100
        else:
            match_percentage = 0 
            
        if matching_count > 0: # 하나라도 일치하면 후보에 추가
            found_recipes.append({
                "name": recipe_name,
                "info": recipe_info,
                "percentage": match_percentage,
                "missing": list(missing_ingredients)
            })
    
    # 일치율이 높은 순서로 정렬
    found_recipes.sort(key=lambda x: x["percentage"], reverse=True)

    if found_recipes:
        for recipe in found_recipes:
            st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
            st.markdown(f"<h4>{recipe['info']['아이콘']} {recipe['name']} (일치율: {recipe['percentage']:.0f}%)</h4>", unsafe_allow_html=True)
            
            st.progress(int(recipe['percentage']) / 100) # 진행바
            
            st.markdown("<p><strong>재료 목록:</strong> " + "".join([f"<span class='ingredient-tag'>{ing}</span>" for ing in recipe['info']['재료']]) + "</p>", unsafe_allow_html=True)
            
            if recipe['missing']:
                st.markdown("<p style='color: #E66767;'><strong>⚠️ 부족한 재료:</strong> " + ", ".join(recipe['missing']) + "</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color: #62A87C;'>🥳 모든 재료가 충분해요! 바로 만들 수 있어요!</p>", unsafe_allow_html=True)
            
            # 상세 레시피 보기 버튼
            if st.button(f"'{recipe['name']}' 상세 레시피 보기 📖", key=f"detail_{recipe['name']}"):
                st.session_state['selected_recipe'] = recipe['name']
                st.session_state['page'] = 'detail'
                st.rerun() # 페이지 전환
            
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("💡 아쉽지만 입력하신 재료로는 추천할 만한 레시피가 없어요. 😢 다른 재료를 입력해보시거나, '오늘의 추천 메뉴'를 확인해 보세요! ✨")

# --- 4. 🚀 메인 애플리케이션 흐름 🚀 ---
def main():
    # 세션 상태 초기화 (페이지 전환 관리)
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    if 'selected_ingredients' not in st.session_state:
        st.session_state['selected_ingredients'] = []

    # 홈 화면: 시작하기 버튼
    if st.session_state['page'] == 'home':
        st.markdown("<h1>✨ 냉장고가 다 해줄게! 💖</h1>", unsafe_allow_html=True)
        # 이미지는 원하는 귀여운 캐릭터 이미지 URL로 교체하세요! (예: 직접 그린 냉장고 캐릭터)
        st.image("https://images.unsplash.com/photo-1542838132-92c53f40776b?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="뚝딱! 레시피가 나올 거예요. 🍽️", use_column_width=True)
        st.markdown("<p style='text-align: center; font-size: 1.4em; font-weight: bold; color: #4B0082;'>냉장고 속 남은 재료로 쉽고 맛있게 요리해요! 🪄</p>", unsafe_allow_html=True)
        
        # 시작 버튼을 가운데 정렬하기
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2: # 중앙 컬럼에 버튼 배치
            if st.button("🚀 요리 시작하기! 🚀", key="start_app_button"):
                st.session_state['page'] = 'main_app'
                st.rerun()

    # 메인 앱 화면: 레시피 검색/추천 탭
    elif st.session_state['page'] == 'main_app':
        st.markdown("<h1>어떤 도움이 필요하신가요? 🥕</h1>", unsafe_allow_html=True)

        # 탭 UI
        tab1, tab2 = st.tabs(["재료로 레시피 찾기 🥦", "오늘의 추천 메뉴 🎁"])
        
        with tab1:
            st.markdown("<h3>🧊 냉장고 속 재료를 알려주세요! 👇</h3>", unsafe_allow_html=True)
            # 모든 레시피 재료 옵션 (중복 제거 후 정렬)
            all_possible_ingredients = sorted(list(set(ing for r in RECIPES_DB.values() for ing in r['재료'])))

            # 멀티셀렉트로 재료 선택
            current_selected = st.multiselect(
                "✔ 냉장고에 있는 재료를 선택해주세요:",
                all_possible_ingredients,
                default=st.session_state['selected_ingredients'], # 이전에 선택된 재료 유지
                key="ingredient_selector"
            )
            # 선택된 재료를 세션 상태에 저장하여 재실행 시 유지되도록 함
            st.session_state['selected_ingredients'] = current_selected

            # 직접 재료 추가 입력창 (Enter로 추가 가능)
            new_ingredient_text = st.text_input("💡 목록에 없는 재료가 있다면 직접 입력 후 엔터를 누르세요:", key="new_ingredient_text")
            
            # 새 재료 추가 로직
            if st.session_state['new_ingredient_text'] and st.session_state['new_ingredient_text'] not in st.session_state['selected_ingredients']:
                st.session_state['selected_ingredients'].append(st.session_state['new_ingredient_text'])
                st.success(f"🎉 '{st.session_state['new_ingredient_text']}' 재료가 추가되었습니다! 목록에서 선택하거나 추가할 수 있습니다.")
                st.session_state['new_ingredient_text'] = "" # 입력 필드 초기화 (필요시)
                st.rerun() # 변경사항 반영을 위해 앱 다시 실행

            # 레시피 찾기 버튼
            if st.button("🔎 이 재료로 레시피 찾기!", key="find_recipe_button"):
                if st.session_state['selected_ingredients']:
                    find_matching_recipes(st.session_state['selected_ingredients'])
                else:
                    st.warning("⚠️ 재료를 하나 이상 선택하거나 입력해주세요! 그래야 레시피를 찾아볼 수 있어요. 🥺")

        with tab2:
            st.markdown("<h3>오늘 뭐 먹지? 😋 랜덤 메뉴 추천! 🎁</h3>", unsafe_allow_html=True)
            st.write("재료 고민은 그만! 제가 오늘 뭐 먹을지 딱 정해드릴게요! (재료 입력 없이 랜덤으로 추천)")
            if st.button("🎲 오늘의 메뉴 추천받기!", key="random_menu_button"):
                random_recipe_name = random.choice(list(RECIPES_DB.keys()))
                display_recipe_card(random_recipe_name, RECIPES_DB[random_recipe_name])
                st.markdown("<br>", unsafe_allow_html=True) # 공백 추가
                # 다른 메뉴 추천 버튼을 한 번 더 누를 수 있도록 함
                if st.button("🔄 다른 메뉴 추천받기", key="another_random_button"):
                    st.rerun() 
        
        st.markdown("---") # 구분선
        # 홈으로 돌아가기 버튼
        if st.button("🏠 처음 화면으로 돌아가기", key="back_to_home"):
            st.session_state['page'] = 'home'
            st.session_state['selected_ingredients'] = [] # 재료 목록 초기화
            st.rerun()

    # 레시피 상세 페이지
    elif st.session_state['page'] == 'detail':
        selected_recipe_name = st.session_state.get('selected_recipe')
        if selected_recipe_name and selected_recipe_name in RECIPES_DB:
            display_recipe_card(selected_recipe_name, RECIPES_DB[selected_recipe_name])
        else:
            st.error("앗! 레시피 정보를 찾을 수 없습니다. 😱")
        
        st.markdown("<br>", unsafe_allow_html=True) # 여백
        if st.button("◀️ 목록으로 돌아가기", key="back_to_main_app"):
            st.session_state['page'] = 'main_app'
            st.rerun()

# --- 5. ✨ 앱 실행 ✨ ---
if __name__ == "__main__":
    main()
