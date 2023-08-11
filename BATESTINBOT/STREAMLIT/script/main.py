import streamlit as st
from key import key

def main():
    keys = str(key()['key'])
    bot_url = f"https://webchat.botframework.com/embed/botBatestin?s={keys}"
    page_bg = f'''
    <style>
    .stApp {{
        background-image: url("C:/Users/Bates/Documents/Repositorios/chatbot/BATESTINBOT/STREAMLIT/assets/wall.jpg");
        background-size: cover;
        background-repeat: repeat;
    }}
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)
    st.markdown('<div class="stApp"><h1 style="text-align: center;">BOT BATESTIN</h1></div>', unsafe_allow_html=True)
    iframe_code = f'<iframe src="{bot_url}" style="min-width: 300px; width: 100%; min-height: 400px;"></iframe>'
    st.markdown('<div class="stApp">' + iframe_code + '</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

