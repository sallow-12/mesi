import streamlit as st
import random
from datetime import datetime

st.title("何食べる？")

step1 = st.radio(
    "ジャンルを選んで",
    ["ごはん", "ワンプレート　丼", "おかず", "サラダ", "スープ"],
    key="step1"
)

if step1 == "ごはん":
    step2 = st.radio(
        "米が好き！",
        ["炊き込みご飯", "煮込みご飯", "炒飯"],
        key="step2"
    )

elif step1 == "ワンプレート　丼":
    step2 = st.radio(
        "お手軽！",
        ["鍋", "煮込み料理", "丼"],
        key="step2"
    )
