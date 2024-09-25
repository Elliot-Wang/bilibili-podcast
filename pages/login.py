import streamlit as st

if "login_data" not in st.session_state:
    st.session_state.login_data = {
        "sms_sended": False,
        "logined": False,
    }
login_data = st.session_state.login_data

st.title("🎈 Login Bilibili")

mobile = st.text_input("Mobile")
sms_code = st.text_input("Verify Code")

def click_one_button():
    if not login_data["sms_sended"]:
        login_data["sms_sended"] = True
    else:
        login_data["logined"] = True
    st.rerun()


one_button = st.button("login" if login_data["sms_sended"] else "send code",
             type="primary" if login_data["sms_sended"] else "secondary")

if one_button:
    if not login_data["sms_sended"]:
        login_data["sms_sended"] = True
    else:
        login_data["logined"] = True

    st.rerun()

if login_data["logined"]:
    login_data["logined"] = True
    st.success("you are logined")
elif login_data["sms_sended"]:
    st.toast("verify code has sended!")

if st.button("clear session"):
    del st.session_state["login_data"]
    st.rerun()
else:
    st.session_state.login_data = login_data