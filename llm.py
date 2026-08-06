from groq import Groq 

client = Groq(api_key="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")

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
