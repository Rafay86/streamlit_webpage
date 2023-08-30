from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title = "My WebPage", page_icon = ":tada:",layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#----
lottie_coding =load_lottieurl("https://lottie.host/d1252667-da25-4b2f-bdcd-d4c6e3ff6200/ICOzDluAQq.json")
img_contact_form = Image.open("images/webpage.png")
img_lottie_animation= Image.open("images/slot machine.png")

#------Header-------
with st.container():
    st.title("Hi, I am rafay ahmed :wave:")
    st.subheader("persuing Engineering from gulbarga")
    st.write("Iam learning python and data structures")
    st.write("[learn more >](https://rafay86.github.io/CV/)")


#  --what i do--
with st.container():
    st.write("--")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write(
            """
            iam learning python and dsa:
            - iam struggling with DSA.
            - and iam sure one day i will  master it.
            - and iam thinking of learning data science.
            - and below are the channel i am using for machine learning.
            """
        )
        st.write("[youtube channel >](https://www.youtube.com/user/sentdex)")
    with right_column:
        st_lottie(lottie_coding,height = 300,key= "coding")


#---- projects--
with st.container():
    st.write("---")
    st.header("my projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        #insert images
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("slot machine using python and oops ")
        st.write(
            """
            it contains python and oops principle
            """
        )
    with st.container():
        image_column,text_column = st.columns((1,2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
           st.subheader("webpage using html and css ")
           st.write(
               """
               it contains my repository
               """
           )
           st.markdown("[Github link..](https://github.com/Rafay86/my-website)")

# contact--
with st.container():
    st.write("--")
    st.header("Get in touch with me")
    st.write('##')

    #contact contact_from
    contact_form = """
    <form action="https://formsubmit.co/mohdrafay86@gmail.com" method="POST">
     <input type = "hidden" name ="_captcha" value= "false">
     <input type="text" name="name" placeholder = "your name" required>
     <input type="email" name="email" placehollder = "mohdrafay86@gmail.com" required>
     <textarea name = "message" placeholder= "your messaage here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
with right_column:
    st.empty()
