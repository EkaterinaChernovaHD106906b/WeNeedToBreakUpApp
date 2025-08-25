import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
st.title("We Need to Break Up 💔")

# --- Settings sidebar ---
st.sidebar.header("⚙️ Message Settings")

tone = st.sidebar.selectbox("🎭 Choose the tone for your message:", ["Polite", "Honest", "Humorous", "Firm"])
reason = st.sidebar.text_input("✏️ Reason for breakup (optional):")

# Display selections
st.write(f"Tone: {tone}")
if reason:
    st.write(f"Reason: {reason}")

st.sidebar.header("Contact us:")
st.sidebar.write("gweiubp@gmail.com")

def create_text_message_with_gpt(tone, reason):
    model = "gpt-4o-mini"
    temperature = 1
    max_tokens = 300
    prompt = f"Write a breakup message in a {tone} tone."
    if reason:
        prompt += f"Reason: {reason}"
    response = client.chat.completions.create(model=model, messages=[
        {"role": "system", "content": "You are an assistant that helps people write breakup messages in a respectful and empathetic way. Always keep the message short, clear, and appropriate for texting. Use the tone and relationship type provided by the user. Do not include unnecessary explanations or advice unless asked." },
        {"role": "user", "content": prompt}
    ], temperature=temperature, max_tokens=max_tokens, n=2)
    suggestions = [choice.message.content for choice in response.choices]

    return suggestions

if st.button("🔍 Ask GPT"):
    with st.spinner("Generating breakup message..."):
        suggestions = create_text_message_with_gpt(tone, reason)
    st.subheader("Suggested message")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Option 1")
        st.write(suggestions[0])
    with col2:
        st.subheader("Option 2")
        st.write(suggestions[1])
   