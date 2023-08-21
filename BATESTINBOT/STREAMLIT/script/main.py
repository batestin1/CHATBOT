import streamlit as st
import requests

def main():
    st.title("Batestin Bot - Watson Assistant Chat")

    # Definir a URL do servidor Flask
    flask_server_url = "http://localhost:5000"  # Substitua pelo URL correto se for diferente

    # Exibir o conteúdo do servidor Flask usando o componente de HTML
    response = requests.get(flask_server_url)
    st.components.v1.html(response.content, height=700)

if __name__ == "__main__":
    main()
