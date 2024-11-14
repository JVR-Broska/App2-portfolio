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

df = pandas.read_csv('data.csv', sep=';')

col3, col4 = st.columns(2)
with col3:
    for index, row in df[0:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(row['url'])

with col4:
    for index, row in df[10:20].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(row['url'])
