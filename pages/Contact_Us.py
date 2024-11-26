import streamlit as st
import send_email

user_email = 'undefined'
user_text = 'undefined'



st.header("Contact Me")
with st.form(key='email_forms'):
    user_email  = st.text_input(label="Your Email Address")

    user_topic = st.selectbox(label="What topic do you want to discuss?",
                              options=["Job Inquires", "Project Proposals", "Other"],
                              key="topic")

    user_text = st.text_area(label="Your text")

    button = st.form_submit_button("Submit")

if button:
    if '@' and '.' in user_email:
        st.write("Sending message...")

        send_email.subimit_email(user_email=user_email, subject=st.session_state['topic'], message=user_text)

        processed_message = f"""
        Subject: {st.session_state['topic']}
        {user_text}\nMessage by {user_email}"""
        st.write(processed_message)

    else:
        st.write("Your email is not valid")


st.session_state