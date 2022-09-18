import streamlit as st


# Initialize state
if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_count():
    st.session_state.count += 1


st.markdown(f"# Count = {st.session_state.count}")

st.button('Increment', on_click=increment_count)
