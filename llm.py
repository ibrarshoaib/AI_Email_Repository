from groq import Groq 
import streamlit as st

client = Groq(api_key=st.secrets[GROQ_API_KEY])

def generated_email(prompt):
    response = client.chat.completions.create(
    model ="llama-3.3-70b-versatile",
    messages=[
        {
            "role" : "user",
            "content" : prompt
        }
    ]
    )
    email = response.choices[0].message.content 
    return email 
