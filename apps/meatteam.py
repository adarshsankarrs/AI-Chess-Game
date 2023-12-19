import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():
    # im1 = Image.open('/Users/ashwinv/Documents/SEM5/Signal/project/code/apps/VCODE.png')

    # st.header('Meet the Team')
    # st.image(im1, width=750)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AmritaVarshini ER")
        st.markdown('*AM.EN.U4AIE19010*')
        st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/varshini.jpeg")

    with col2:
        st.subheader("Ann Maria John")
        st.markdown('*AM.EN.U4AIE19013*')
        st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/ann.jpeg")

    with col3:
        st.subheader("Ashwin V")
        st.markdown('*AM.EN.U4AIE19018*')
        st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/ash.jpg")

    with st.container():
        col4, col5, col6 = st.columns(3)

        with col4:
            st.subheader("Devi Parvathy Nair")
            st.markdown('*AM.EN.U4AIE19026*')
            st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/devi.jpg", width=222)

        with col5:
            st.subheader("Vishal Menon")
            st.markdown('*AM.EN.U4AIE19070*')
            st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/Vishal.png", width=222)

    st.markdown('<center>Department of Computer Science and Engineering </center>', unsafe_allow_html=True)
  

    st.markdown("<center> Amrita Viswa Vidyapeetham </center>", unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    with st.container():
        col4, col5, col6 = st.columns(3)
        with col5:
            st.image("/Users/ashwinv/Documents/SEM5/maths/project/appp/imgs/logoneg.svg", width=70)
