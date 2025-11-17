import streamlit as st
from rag import load_rules, retrieve

# ---- Page Config ----
st.set_page_config(
    page_title="Carrom Referee Chatbot",
    page_icon="🎯",
    layout="centered"
)

# ---- Custom CSS ----
st.markdown("""
<style>

body {
    background-color: #111111;
    color: #FFFFFF;
}

input[type="text"] {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border: 1px solid #444444 !important;
    padding: 10px !important;
}

textarea, .stTextInput>div>div>input {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

.stTextInput label {
    color: #BBBBBB !important;
}

.stMarkdown {
    color: #FFFFFF !important;
}

.answer-box {
    background-color: #000000;
    color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #333333;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #888888;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---- App Title ----
st.markdown("<h1 style='text-align:center;'>🎯 Carrom Referee Chatbot</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#BBBBBB;'>Ask any carrom rule doubt — answered by AI trained on full official rules.</p>", unsafe_allow_html=True)


# ---- Load Rules ----
rules, embeddings = load_rules("rules.txt")

# ---- Input Box ----
query = st.text_input("Ask your question here:")

# ---- Output ----
if query:
    answer, _ = retrieve(query, rules, embeddings)

    st.markdown(
        f"<div class='answer-box'><strong>Answer:</strong><br>{answer}</div>",
        unsafe_allow_html=True
    )


# ---- Footer ----
st.markdown(
    "<div class='footer'>Made by Raveen, a carrom player | Powered by LLM</div>",
    unsafe_allow_html=True
)
