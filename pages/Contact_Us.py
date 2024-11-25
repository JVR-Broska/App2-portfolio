import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key='email_forms'):
    user_email  = st.text_input("Your Email Address..")
    user_message = st.text_area("Your message")
    options = ["1", "2", "3"]
    st.selectbox(label="escolha", options=options, key="topic")

    button = st.form_submit_button("Subimit")
    print(button)


    if button:
        if '@' and '.' in user_email:
            st.write("Sending message...", key='status')
            send_email.subimit_email(user_email, user_message)
            st.session_state['status'] = ""
        else:
            st.write("Your email is not valid")

if button:
    st.write(f"{user_email} said: {user_message}")