from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ganai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Error: GOOGLE_API_KEY is not set in the environment.")
else:
    ganai.configure(api_key=API_KEY)
    model = ganai.GenerativeModel("gemini-pro")

    def my_output(query) -> str:
        try:
            response = model.generate_content(query)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    # Streamlit UI
    st.set_page_config(page_title="SMART BOT🤖")
    st.header("SMART BOT🤖")

    user_input = st.text_input("Input:", key="input")
    submit = st.button("Ask your Query")

    if submit and user_input.strip():
        response = my_output(user_input)
        st.subheader("Response:")
        st.write(response)
    elif submit:
        st.warning("Please provide some input.")