import streamlit as st
from rag import load_rules, retrieve

st.title("Carrom Referee Chatbot")

rules, embeddings = load_rules("rules.txt")

query = st.text_input("Ask any carrom rule doubt:")

if query:
    answer, score = retrieve(query, rules, embeddings)
    st.write("### Answer:")
    st.write(answer)
