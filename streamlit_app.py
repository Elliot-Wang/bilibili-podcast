import streamlit as st

st.title("🎈 Bilibili-Postcast")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
mobile = st.text_input("Mobile")
sms_code = st.text_input("Verify Code")
st.button("send code")
st.button("login", type="primary")