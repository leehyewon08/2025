import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(
    page_title="냉장고를 부탁해!",
    page_icon="🍳",
    layout="wide"
)

# 귀여운 스타일 적용
st.markdown("""
<style>
    .main {
        background-color: #FFF5E4;
    }
    .stButton>button {
        background-color: #FFD1D1;
        color: #594545;
        border-radius: 20px;
        font-weight: bold;
    }
    h1, h2 {
        color: #594545;
    }
    .recipe-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 레시피 데이터베이스
recipes_db = {
    "김치볶음밥": {
        "재료": ["김치", "밥", "계란", "파"],
        "조리법": "1. 김치를 잘게 썬다.\n2. 프라이팬에 김치를 볶는다.\n3. 밥을 넣고 함께 볶는다.\n4. 계란을 넣고 살짝 더 볶는다.\n5. 파를 뿌려 완성한다.",
        "난이도": "쉬움",
        "시간": "15분"
    },
    "계란말이": {
        "재료": ["계란", "파", "당근", "소금"],
        "조리법": "1. 계란을 풀어 소금을 넣고 섞는다.\n2. 파와 당근을 잘게 썰어 넣는다.\n3. 프라이팬에 계란물을 부어 익힌다.\n4. 익으면 말아서 완성한다.",
        "난이도": "쉬움",
        "시간": "10분"
    },
    "참치마요덮밥": {
        "재료": ["참치캔", "마요네즈", "밥", "김"],
        "조리법": "1. 참치캔의 기름을 뺀다.\n2. 참치에 마요네즈를 넣고 섞는다.\n3. 밥 위에 참치마요 믹스를 올린다.\n4. 김 가루를 뿌려 완성한다.",
        "난이도": "쉬움",
        "시간": "5분"
    },
    "라면땅콩볶음": {
        "재료": ["라면", "땅콩", "양파", "간장"],
        "조리법": "1. 라면을 삶아서 물기를 뺀다.\n2. 프라이팬에 양파를 볶는다.\n3. 라면과 땅콩을 넣고 간장으로 간을 한다.\n4. 골고루 볶아서 완성한다.",
        "난이도": "보통",
        "시간": "15분"
    }
}

# 메인 함수
def main():
    st.title("🍳 냉장고를 부탁해!")
    st.subheader("냉장고 속 재료로 맛있는 요리를 만들어 보세요!")
    
    # 탭 생성
    tab1, tab2 = st.tabs(["재료로 레시피 찾기", "오늘의 추천 메뉴"])
    
    with tab1:
        st.markdown("### 🧊 냉장고 속 재료 입력하기")
        # 재료 입력 (멀티셀렉트 박스 사용)
        all_ingredients = set()
        for recipe in recipes_db.values():
            all_ingredients.update(recipe["재료"])
        
        user_ingredients = st.multiselect(
            "냉장고에 있는 재료를 선택해주세요:",
            sorted(list(all_ingredients))
        )
        
        # 사용자가 직접 재료 추가할 수 있는 옵션
        custom_ingredient = st.text_input("목록에 없는 재료 직접 입력:")
        add_btn = st.button("재료 추가")
        
        if add_btn and custom_ingredient:
            if custom_ingredient not in user_ingredients:
                user_ingredients.append(custom_ingredient)
                st.success(f"'{custom_ingredient}' 재료가 추가되었습니다!")
        
        # 레시피 찾기 버튼
        if st.button("레시피 찾기", key="find_recipe"):
            if user_ingredients:
                show_matching_recipes(user_ingredients)
            else:
                st.warning("재료를 하나 이상 선택해주세요!")
    
    with tab2:
        st.markdown("### 🍽️ 오늘의 추천 메뉴")
        st.write("재료 입력 없이 맛있는 메뉴를 추천해 드려요!")
        
        if st.button("메뉴 추천받기"):
            # 랜덤으로 레시피 선택
            random_recipe = random.choice(list(recipes_db.keys()))
            display_recipe(random_recipe, recipes_db[random_recipe])

# 재료에 맞는 레시피 찾기
def show_matching_recipes(ingredients):
    st.markdown("### 🔍 검색 결과")
    
    matching_recipes = []
    
    # 각 레시피마다 일치하는 재료 수 계산
    for recipe_name, recipe_info in recipes_db.items():
        recipe_ingredients = set(recipe_info["재료"])
        user_ingredients_set = set(ingredients)
        
        # 일치하는 재료 수 계산
        matching_count = len(recipe_ingredients.intersection(user_ingredients_set))
        
        # 하나 이상 일치하면 결과에 추가
        if matching_count > 0:
            matching_percentage = (matching_count / len(recipe_ingredients)) * 100
            matching_recipes.append({
                "name": recipe_name,
                "info": recipe_info,
                "matching": matching_percentage,
                "missing": recipe_ingredients - user_ingredients_set
            })
    
    # 일치율 기준으로 정렬
    matching_recipes.sort(key=lambda x: x["matching"], reverse=True)
    
    if matching_recipes:
        for recipe in matching_recipes:
            with st.container():
                st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
                st.subheader(f"🍲 {recipe['name']}")
                st.progress(int(recipe["matching"]))
                st.write(f"일치율: {recipe
