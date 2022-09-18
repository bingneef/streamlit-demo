import streamlit as st
import numpy as np
import os
from streamlit_cookies_manager import EncryptedCookieManager

# This should be on top of your script
cookies = EncryptedCookieManager(
    prefix="bingneef/streamlit-cookies-manager/",
    password=os.environ.get("COOKIES_PASSWORD", "My secret password"),
)

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()


# Initialize state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = cookies.get('logged_in') == '1' or False


def logout():
    cookies['logged_in'] = '0'
    st.session_state.logged_in = False


def verify_password():
    if 'password' in st.session_state and st.session_state.password == os.environ.get("PASSWORD", "TOETER"):
        cookies['logged_in'] = '1'
        st.session_state.logged_in = True
    else:
        st.error('Invalid password', icon="🚨")


st.markdown("# Inputpage ❄️")
st.sidebar.markdown("# Inputpage ❄️")

if st.session_state.logged_in:
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.sidebar.write(options)

    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = np.random.randn(10, 1)

    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)

    tab2.subheader("A tab with the data")
    tab2.write(data)

    st.button('Logout', on_click=logout)

else:
    st.text_input('Password', key="password", on_change=verify_password)