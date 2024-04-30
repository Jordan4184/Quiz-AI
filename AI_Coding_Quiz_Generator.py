import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Fetch API keys
OPEN_AI_API_KEY = os.getenv("OPEN_AI_KEY")

# Check if API keys are set
if OPEN_AI_API_KEY is None:
    raise ValueError("API key not set. Please check your environment.")

# Initialize OpenAI client
client = OpenAI(api_key=OPEN_AI_API_KEY)

# Define the function to generate quiz questions based on the type
def generate_quiz_question(quiz_type, coding_subject):
    system_prompt = "You are a coding quiz generator."
    user_prompt = f"Generate a {quiz_type.lower()} question for the coding subject: {coding_subject}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )
        question = response.choices[0].message.content.strip()
        return question
    except Exception as e:
        st.error(f"Failed to generate question: {str(e)}")
        return "Error generating question."


# Define the Streamlit app structure
def main():
    st.title("Coding Quiz Generator")
    st.header("Quiz Parameters")

    coding_subject = st.text_input("Enter Coding Subject")
    quiz_type = st.selectbox("Select Quiz Type", ["Multiple Choice", "Coding Exercise", "Bug Fixing", "Definitions"])
    
    if st.button("Generate Quiz"):
        question = generate_quiz_question(quiz_type, coding_subject)
        st.subheader(f"Quiz Type: {quiz_type}")
        st.subheader(f"Coding Subject: {coding_subject}")
        st.write(question)

if __name__ == "__main__":
    main()