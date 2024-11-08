import streamlit as st
import pandas



codes = {'code1':"", 'code2':"", 'code3':"", 'code4':""}

index = 1
for code in codes:
    with open(f'codes/code{index}.txt', 'r') as file:
        codes[code] = file.read()
    index += 1

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Joao Broska")
    content = """Hi, I am here to create some genius ideas for your business, providing a way to shortly cut the problems and make you higher than our concurrence. 
    Let's plan together and make sure to keep ambition on it.
    """
    st.info(content)

st.write("Below you have all of the good information about my work history.")

df = pandas.read_csv('data.csv')



col3, col4 = st.columns(2)
with col3:
    st.subheader("Todo App")
    content = """A distraction-free web app to help you focus on creating and completing tasks.
    """
    image = "images/1.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code1'])

    st.subheader("Portfolio website")
    content = """A website built entirely in pytho to showcase coding projects and apps.
    """
    image = "images/2.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code2'])

    st.subheader("Typing Analyzer")
    content = """A program that monitors the computer keyboard and returns the most typed words of the session.
    """
    image = "images/5.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code4'])

with col4:
    st.subheader("Portfolio website")
    content = """A program that monitors the computer webcam and sends an email when a new object enters the view.
    """
    image = "images/3.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code3'])


    st.subheader("Typing Analyzer")
    content = """A program that monitors the computer keyboard and returns the most typed words of the session.
    """
    image = "images/6.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code4'])


    st.subheader("Typing Analyzer")
    content = """A program that monitors the computer keyboard and returns the most typed words of the session.
    """
    image = "images/4.png"
    st.write(content)
    st.image(image)
    expand = st.expander("Source Code")
    expand.code(codes['code4'])
