import streamlit as st
from get_menu import get_menu_as_string

st.title('Welcome to the VTx lunch menu wizard!')

get_menu = st.button('click here to get the latest menu')
if get_menu:
    menu = get_menu_as_string()
    st.text(menu)