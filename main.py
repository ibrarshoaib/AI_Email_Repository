import streamlit as st

from llm import generated_email
from prompts import cold_intro, follow_up, proposal


st.set_page_config(
    page_title="AI Email Drafting Assistant",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Drafting Assistant")
st.write("Generate professional emails in seconds using AI.")

st.divider()

name = st.text_input("Your Name")

email_type = st.selectbox(
    "Email Type",
    (
        "Cold Introduction",
        "Follow-up",
        "Proposal"
    )
)

purpose = st.text_area(
    "Email Purpose",
    placeholder="Example: Introduce my AI project to a recruiter..."
)

tone = st.selectbox(
    "Tone",
    (
        "Friendly",
        "Formal",
        "Short"
    )
)

if st.button("Generate Email", use_container_width=True):

    if not name or not purpose:
        st.warning("Please fill in all required fields.")

    else:

        if email_type == "Cold Introduction":
            prompt = cold_intro(name, purpose, tone)

        elif email_type == "Follow-up":
            prompt = follow_up(name, purpose, tone)

        else:
            prompt = proposal(name, purpose, tone)

        with st.spinner("Generating email..."):
            email = generated_email(prompt)

        st.success("Email Generated Successfully!")

        st.subheader("Generated Email")

        st.text_area(
            "",
            value=email,
            height=300
        )

        st.download_button(
            label="Download Email",
            data=email,
            file_name="generated_email.txt",
            mime="text/plain",
            use_container_width=True
        )