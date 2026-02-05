import streamlit as st

st.set_page_config(
    page_title="今日何食べる？｜献立メーカー",
    page_icon="🍽️"
)

st.title("今日何食べる？｜かんたん献立決定アプリ")

import streamlit as st

st.title("何食べる？🍽️")

# セッションに保存する箱（最初だけ作る）
if "menu" not in st.session_state:
    st.session_state.menu = {
        "ごはん": [
            {"name": "炒飯", "recipe": "ご飯を炒める"},
        ]
    }

# --- 追加フォーム ---
st.subheader("メニューを追加")

new_genre = st.text_input("ジャンル")
new_name = st.text_input("料理名")
new_recipe = st.text_area("レシピ")

if st.button("追加する"):
    if new_genre and new_name:
        if new_genre not in st.session_state.menu:
            st.session_state.menu[new_genre] = []

        st.session_state.menu[new_genre].append({
            "name": new_name,
            "recipe": new_recipe
        })
        st.success("追加しました！")

# --- 選択画面 ---
st.subheader("メニューを選ぶ")

genre = st.selectbox("ジャンル", list(st.session_state.menu.keys()))

names = [item["name"] for item in st.session_state.menu[genre]]
name = st.selectbox("料理", names)

if st.button("レシピを見る"):
    for item in st.session_state.menu[genre]:
        if item["name"] == name:
            st.write("📖 レシピ")
            st.info(item["recipe"])

