import streamlit as st
import pandas as pd
import random
from PIL import Image
import base64

# 페이지 설정
st.set_page_config(
    page_title="냉장고를 부탁해!",
    page_icon="🍳",
    layout="wide"
)

# 귀여운 배경 이미지와 스타일 설정
def add_bg_and_styling():
    st.markdown("""
    <style>
        .main {
            background-color: #FFF5E4;
            font-family: 'Nanum Gothic', sans-serif;
        }
        .stButton>button {
            background-color: #FFD1D1;
            color: #594545;
            border-radius: 20px;
            border: 2px solid #FFF5E4;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #FF9494;
            color: white;
            transform: scale(1.05);
        }
        h1, h2, h3 {
            color: #594545;
        }
        .recipe-card {
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .ingredient-tag {
            background-color: #FFD1D1;
            color: #594545;
            padding: 5px 10px;
            border-radius: 10px;
            margin: 3px;
            display: inline-block;
        }
        .header-container {
            text-align: center;
            padding: 20px;
            background-color: #FFC7C7;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #594545;
            margin-top: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

# 레시피 데이터베이스
def get_recipes():
    recipes = {
        "김치볶음밥": {
            "재료": ["김치", "밥", "계란", "파", "식용유"],
            "조리법": "1. 김치를 잘게 썬다.\n2. 프라이팬에 식용유를 두르고 김치를 볶는다.\n3. 밥을 넣고 함께 볶는다.\n4. 계란을 넣고 살짝 더 볶는다.\n5. 파를 뿌려 완성한다.",
            "난이도": "쉬움",
            "시간": "15분",
            "이미지": "🍚"
        },
        "계란말이": {
            "재료": ["계란", "파", "당근", "소금", "식용유"],
            "조리법": "1. 계란을 풀어 소금을 넣고 섞는다.\n2. 파와 당근을 잘게 썰어 넣는다.\n3. 프라이팬에 식용유를 두르고 계란물을 부어 익힌다.\n4. 익으면 말아서 완성한다.",
            "난이도": "쉬움",
            "시간": "10분",
            "이미지": "🍳"
        },
        "참치마요덮밥": {
            "재료": ["참치캔", "마요네즈", "밥", "김", "양파"],
            "조리법": "1. 참치캔의 기름을 뺀다.\n2. 양파를 잘게 썬다.\n3. 참치에 마요네즈와 양파를 넣고 섞는다.\n4. 밥 위에 참치마요 믹스를 올린다.\n5. 김 가루를 뿌려 완성한다.",
            "난이도": "쉬움",
            "시간": "5분",
            "이미지": "🐟"
        },
        "김치찌개": {
            "재료": ["김치", "돼지고기", "두부", "파", "고춧가루", "간장"],
            "조리법": "1. 김치와 돼지고기를 적당한 크기로 자른다.\n2. 냄비에 김치와 돼지고기를 넣고 볶는다.\n3. 물을 붓고 끓인다.\n4. 두부를 넣고 간장으로 간을 한다.\n5. 파를 넣고 마무리한다.",
            "난이도": "보통",
            "시간": "30분",
            "이미지": "🍲"
        },
        "된장찌개": {
            "재료": ["된장", "두부", "애호박", "양파", "파", "고추"],
            "조리법": "1. 애호박, 양파, 고추를 적당한 크기로 자른다.\n2. 냄비에 물을 붓고 끓인다.\n3. 된장을 풀어 넣는다.\n4. 야채와 두부를 넣고 끓인다.\n5. 파를 넣고 마무리한다.",
            "난이도": "보통",
            "시간": "20분",
            "이미지": "🥘"
        },
        "라면땅콩볶음": {
            "재료": ["라면", "땅콩", "양파", "간장", "설탕", "고추장"],
            "조리법": "1. 라면을 삶아서 물기를 뺀다.\n2. 프라이팬에 양파를 볶는다.\n3. 라면과 땅콩을 넣고 간장, 설탕, 고추장으로 간을 한다.\n4. 골고루 볶아서 완성한다.",
            "난이도": "쉬움",
            "시간": "15분",
            "이미지": "🍜"
        },
        "감자채볶음": {
            "재료": ["감자", "당근", "식용유", "소금", "후추"],
            "조리법": "1. 감자와 당근을 채 썬다.\n2. 프라이팬에 식용유를 두르고 감자를 먼저 볶는다.\n3. 당근을 넣고 함께 볶는다.\n4. 소금, 후추로 간을 하고 바삭하게 볶아 완성한다.",
            "난이도": "보통",
            "시간": "20분",
            "이미지": "🥔"
        }
    }
    return recipes

# 레시피 카드 표시 함수
def display_recipe(name, recipe):
    with st
