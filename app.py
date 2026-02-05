import streamlit as st
import json
import os

st.set_page_config(
    page_title="今日何食べる？｜献立メーカー",
    page_icon="🍽️"
)

st.title("献立決定🍽️")

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "ごはん": [
                {"name": "炒飯", "recipe": "ご飯を炒める"},
            ]
        }

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# セッションに保存する箱（最初だけ作る）
if "menu" not in st.session_state:
    st.session_state.menu = load_data()

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

        save_data(st.session_state.menu)  # ← ここで保存！

        st.success("保存しました！")

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


