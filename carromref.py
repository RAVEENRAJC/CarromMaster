import streamlit as st
from rag import load_rules, retrieve

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="Carrom Referee Chatbot",
    page_icon="🎯",
    layout="centered",
)

# ---------------------- Custom CSS ----------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #F02A2A;
        margin-bottom: -10px;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }
    .answer-box {
        background-color: #fff5e6;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #ff8c00;
        font-size: 17px;
        margin-top: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #777;
    }
    .stTextInput>div>div>input {
        background-color: #fff;
        padding: 12px;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------- Header ----------------------
st.markdown("<div class='main-title'>🎯 Carrom Referee Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Ask any rule — fouls, queen, covering, scoring, special cases!</div>", unsafe_allow_html=True)

# ---------------------- Load Rules ----------------------
rules, embeddings = load_rules("rules.txt")

# ---------------------- User Input ----------------------
query = st.text_input("💬 Enter your carrom rule question:")

if query:
    with st.spinner("Analyzing rules… 🤔"):
        answer, score = retrieve(query, rules, embeddings)

    st.markdown("### ✅ Answer:")
    st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)

    st.markdown(f"**Confidence Score:** `{round(score, 3)}`")

# ---------------------- Suggestions ----------------------
st.write("---")
st.markdown("#### 📝 Example Questions")
col1, col2 = st.columns(2)

with col1:
    st.write("- What happens if the queen is not covered?")
    st.write("- Is pocketing striker a foul?")
    st.write("- What if the striker jumps?")

with col2:
    st.write("- Can I cover the queen later?")
    st.write("- What is the penalty after a foul?")
    st.write("- When does the match end?")

# ---------------------- Footer ----------------------
st.markdown(
    "<div class='footer'>Made by Raveen, a carrom player | Powered by LLM</div>",
    unsafe_allow_html=True
)
