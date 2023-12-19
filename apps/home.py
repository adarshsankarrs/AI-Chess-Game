import streamlit as st
from PIL import Image
def app():
    image = Image.open('/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/bner.jpeg')
    st.image(image, caption='Welcome to our webapp!', use_column_width=True)
    st.subheader('19MAT301	Mathematics for Intelligent Systems 5')
    st.subheader("Group 2", anchor=None)
    st.subheader("A Game of Chess using Reinforcement Learning based on Monte Carlo Tree Search", anchor=None)
    st.subheader("Team Members", anchor=None)
    st.markdown('AmritaVarshini ER&emsp;19010<br> Ann Maria John &emsp;&nbsp;&nbsp; 19013<br> Ashwin V   &emsp;&emsp; &emsp; &emsp;19018  <br> Devi Parvathy Nair &nbsp; 19026  <br> Vishal Menon &nbsp;&nbsp;&emsp; &emsp;19070', unsafe_allow_html=True)
    st.subheader("Submitted to", anchor=None)
    st.markdown("Dr. Don S <br> Dr. Gopakumar G", unsafe_allow_html=True)
