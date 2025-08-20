import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="냉장고가 다 해줄게!", page_icon="🍳")

# 간단한 스타일 적용
st.markdown("""
<style>
    .main {background-color: #FFF5E4;}
    h1, h2, h3 {color: #594545; text-align: center;}
    .stButton>button {background-color: #FFD1D1; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# 레시피 데이터베이스 (간단하게 유지)
RECIPES = {
    "김치볶음밥 🍚": {
        "재료": ["김치", "밥", "계란", "파"],
        "조리법": "1. 김치를 썰어 볶기\n2. 밥 넣고 볶기\n3. 계란 넣고 섞기\n4. 파 뿌려 완성!"
    },
    "계란말이 🍳": {
        "재료": ["계란", "파", "당근", "소금"],
        "조리법": "1. 계란 풀어 소금 넣기\n2. 파, 당근 썰어 넣기\n3. 프라이팬에 부어 익히기\n4. 말아서 완성!"
    },
    "참치마요덮밥 🐟": {
        "재료": ["참치캔", "마요네즈", "밥", "김"],
        "조리법": "1. 참치 기름 빼기\n2. 마요네즈 섞기\n3. 밥 위에 올리기\n4. 김 뿌려 완성!"
    }
}

# 앱 메인 함수
def main():
    st.title("✨ 냉장고가 다 해줄게! ✨")
    
    # 탭 생성
    tab1, tab2 = st.tabs(["🧊 재료로 검색", "🎲 랜덤 추천"])
    
    with tab1:
        st.subheader("냉장고 재료 입력하기")
        
        # 모든 재료 목록 생성
        all_ingredients = sorted(list(set(ing for recipe in RECIPES.values() for ing in recipe["재료"])))
        
        # 재료 선택
        selected = st.multiselect("냉장고에 있는 재료:", all_ingredients)
        
        # 레시피 찾기 버튼
        if st.button("레시피 찾기 🔍"):
            if not selected:
                st.warning("⚠️ 재료를 하나 이상 선택해주세요!")
            else:
                find_recipes(selected)
    
    with tab2:
        st.subheader("오늘의 추천 메뉴")
        if st.button("메뉴 추천받기 🎁"):
            recipe_name = random.choice(list(RECIPES.keys()))
            show_recipe(recipe_name, RECIPES[recipe_name])

# 레시피 찾기 함수
def find_recipes(ingredients):
    st.subheader("🔍 검색 결과")
    found = False
    
    for name, recipe in RECIPES.items():
        # 일치하는 재료 수 계산
        matching = [ing for ing in ingredients if ing in recipe["재료"]]
        if matching:
            match_percent = int(len(matching) / len(recipe["재료"]) * 100)
            st.write(f"### {name} - 일치율: {match_percent}%")
            st.progress(match_percent/100)
            
            # 재료 표시
            st.write("**필요한 재료:** " + ", ".join(recipe["재료"]))
            
            # 부족한 재료 표시
            missing = [ing for ing in recipe["재료"] if ing not in ingredients]
            if missing:
                st.write("**부족한 재료:** " + ", ".join(missing))
            else:
                st.success("👍 모든 재료가 있어요!")
                
            # 상세 보기 버튼
            if st.button(f"{name} 상세보기", key=f"btn_{name}"):
                show_recipe(name, recipe)
                
            st.write("---")
            found = True
    
    if not found:
        st.info("💡 입력하신 재료로 만들 수 있는 레시피가 없어요.")

# 레시피 상세 정보 표시 함수
def show_recipe(name, recipe):
    st.subheader(f"🍽️ {name} 레시피")
    st.write("**재료:** " + ", ".join(recipe["재료"]))
    st.write("**조리법:**")
    st.write(recipe["조리법"])

# 앱 실행
if __name__ == "__main__":
    main()
