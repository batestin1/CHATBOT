import streamlit as st

chatbot_url = "https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?backgroundImageURL=https%3A%2F%2Fus-south.assistant.watson.cloud.ibm.com%2Fpublic%2Fimages%2Fupx-9148eace-be33-47ff-b027-d1c9e6c0e6cd%3A%3Ade7e2ef8-3c45-4dca-bf0d-62c0fccec1de&integrationID=60a965ec-37ee-4aa3-b735-0558faf6fb76&region=us-south&serviceInstanceID=9148eace-be33-47ff-b027-d1c9e6c0e6cd"

st.set_page_config(page_title="BATESTIN BOT")

st.markdown('<h1 style="text-align: center;">BOT BATESTIN</h1>', unsafe_allow_html=True)

iframe_code = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
    <iframe src="{chatbot_url}" width="600" height="400"></iframe>
</div>
"""
st.markdown(f'{iframe_code}', unsafe_allow_html=True)
