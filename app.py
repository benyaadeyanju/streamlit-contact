from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()

# Use Local CSS
#def local_css('style.css'):
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True )

#local_css("style/style.css")



#----Load Assets-----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_g7ycvpvy.json")
img_contact_form = Image.open("images/2.jpg")
img_lottie_animation = Image.open("images/1.jpg")


#------HEADER SECTION----
with st.container():
    st.subheader("Hi, I am Benya Adeyanju Jamiu :wave:")
    st.title("A PhD in AI-Computer Vision specialist from Nigeria")
    st.write("I am passionate about ways of using Python to developed different applications")
    st.write("[Learn More > ](https://www.w3schools.com/python/)")

with st.container():
    st.write("---")
    left_column, right_column= st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I like teaching students ML:
            - CV.
            - DL.
            - Scikit Learning

            if this sound interesting to you, considering contacting me for further information.
            """
        )
        st.write("[Learn More > ](https://www.w3schools.com/python/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

    #----Projects---
with st.container():
     st.write("---")
     st.header("My Projects")
     st.write("##")
     image_column, text_column = st.columns((1,2))
     with image_column:
         st.image(img_lottie_animation)
            
     with text_column:
            st.subheader("Integrate Lottie Animation Inside Your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and lottie Files are the easier
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Watch Video..](https://youtu.be/Fevfe__Geng)")

with st.container():
     st.write("---")
     st.header("My Projects")
     st.write("##")
     image_column, text_column = st.columns((1,2))
     with image_column:
         st.image(img_contact_form)
            
     with text_column:
            st.subheader("How to Add Contact Form to  Your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and lottie Files are the easier
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Watch Video..](https://youtu.be/Fevfe__Geng)")


#------------CONTACT-----
with st.container():
    st.write("---")
    st.header("Get in Touch With Me")
    st.write("##")

    # Documentation: 
    contact_form = """
    <form action="https://formsubmit.co/adeyanju2022@gmail.com" method="POST">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Your name" required>
          <input type="email" name="email" placeholder="Your E-mail" required>
          <textarea name="message" placeholder="Your message" required></textarea>
          <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()    
            
