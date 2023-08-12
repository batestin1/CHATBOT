import streamlit as st

def main():
    st.title("Integração com Watson Assistant")

    # Carregando o conteúdo HTML do arquivo watson_chat.html
    with open("C:/Users/Bates/Documents/Repositorios/chatbot/BATESTINBOT/STREAMLIT/script/watson.html", "r") as f:
        watson_chat_code = f.read()

    # Exibindo o widget de chat do Watson Assistant
    st.components.v1.html(watson_chat_code, height=300)
    st.markdown(
        f'''
        <style>
            body {{
                background-image: url('C:/Users/Bates/Documents/Repositorios/chatbot/BATESTINBOT/STREAMLIT/assets/wall.jpg');
                background-size: cover;
                background-position: center;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
        </style>
        ''',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
