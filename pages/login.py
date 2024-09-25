import streamlit as st
from bilibili_api.login import login_with_sms, send_sms, PhoneNumber, Check

if "login_data" not in st.session_state:
    st.session_state.login_data = {
        "sms_sended": False,
        "logined": False,
        "login_message": None,
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
    phone = str(mobile).strip(" ")
    code = str(sms_code).strip(" ")
    if not login_data["sms_sended"]:
        send_sms(PhoneNumber(phone, country="+86")) # 默认设置地区为中国大陆
        login_data["sms_sended"] = True
    else:
        c = login_with_sms(PhoneNumber(phone, country="+86"), code)
        if isinstance(c, Check):
            # 还需验证
            login_data["login_message"] = "需要进行验证。请考虑使用二维码登录"
        else:
            st.session_state.credential = c
            login_data["logined"] = True

    st.rerun()

if login_data["logined"]:
    login_data["logined"] = True
    st.success("you are logined")
elif login_data["login_message"] is not None:
    st.fail(login_data["login_message"])
elif login_data["sms_sended"]:
    st.toast("verify code has sended!")

if st.button("clear session"):
    del st.session_state["login_data"]
    st.rerun()
else:
    st.session_state.login_data = login_data
