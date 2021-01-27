import random 
import requests
import streamlit as st
import sys
sys.path.append("src")
from get_menu import get_menu_as_string

# get list of all emojis
r = requests.get('https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json') 
emoji_list = list(r.json().keys())

# APP
st.title('Welcome to the VTx lunch menu wizard!')

menu = get_menu_as_string()
st.text(menu)

emoji = random.choice(emoji_list)
st.markdown(f'Link to order takeaway: https://webshop.meyerskantiner.dk/shop/2240/take-away/g/23332')
st.markdown(f'Have a nice day. Here is a random emoji :{emoji}:')