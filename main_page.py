import streamlit as st


# Initialize state
if 'count' not in st.session_state:
    st.session_state.count = 0


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.write(f"State count = {st.session_state.count}")
