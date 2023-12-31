import streamlit as st
from writer import write_article
from misc import fetch_image
from sidebar import sidebar_conf

# basic configuration
st.set_page_config(
    page_title="ArtiFact",
    page_icon="./assets/favicon.png",
    layout="centered",
    initial_sidebar_state="expanded",
)

# sidebar configuration
sidebar_conf()
st.image("./assets/logoX.png")

# take input from user
topic = st.text_input("Write the topic of the Article", max_chars=60)
generate_article = st.button("Generate Article")

# check if topic is given and button is pressed
if topic and generate_article:
    # extract fields from topic
    extract_topic = topic.split("--")
    inputs = {
        "topic": extract_topic[0],
        "user": extract_topic[1],
        "words": extract_topic[2],
    }

    # Display loading GIF while generating the article
    loading_placeholder = st.empty()
    loading_html = f'<div style="display: flex; justify-content: center; align-items: center;"><img src="{st.secrets["loading_gif_url"]}" alt="Loading" width="300px" height="300px"></div>'
    loading_placeholder.markdown(loading_html, unsafe_allow_html=True)

    # fetch image and write article
    image = fetch_image(inputs['topic'], st.secrets["pexels_api_key"])
    article = write_article(inputs, st.secrets["email"], st.secrets["password"])

    # Create HTML string for loading image within a card-like layout
    loading_image_html = f"""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 33  0px;  /* Set a fixed height for the card, adjust as needed */
        margin: 20px;   /* Add margin from all sides */
    ">
        <div style="
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        ">
            <img src="{image}" alt="Loading" style="max-width: 100%; max-height: 100%;">
        </div>
    </div>
    """

    if image and article: 
        loading_placeholder.empty()
        st.markdown(loading_image_html, unsafe_allow_html=True)
        st.markdown("# ----------- Generated Article -----------")
        st.markdown(article, unsafe_allow_html=True)
