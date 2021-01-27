import streamlit as st
import sys
sys.path.append("src")

from get_menu import get_menu_as_string

st.title('Welcome to the VTx lunch menu wizard!')

get_menu = st.button('click here to get the latest menu')
if get_menu:
    menu = get_menu_as_string()
    st.text(menu)

st.markdown(f'Link to order takeaway: https://webshop.meyerskantiner.dk/shop/2240/take-away/g/23332')