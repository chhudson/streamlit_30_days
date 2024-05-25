import streamlit as st

st.write('Hello world!')

st.header('st.button')

# st.button("Say hello", type="primary")
if st.button('Say hello', type="primary"):
    st.write('Why hello there')
else:
    st.write('Goodbye')