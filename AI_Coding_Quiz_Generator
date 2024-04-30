import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_KEY")

if OPEN_AI_API_KEY is None:
    raise ValueError("API keys not set. Please check your environment.")

client = OpenAI(api_key=OPEN_AI_API_KEY)

# Define the Streamlit app structure
def main():
    # Set the title of the app
    st.title("Quiz Generator")

    # Add a header for quiz parameters
    st.header("Quiz Parameters")

    # Add input fields for quiz type and coding subject
    coding_subject = st.text_input("Enter Coding Subject")
    quiz_type = st.selectbox("Select Quiz Type", ["Multiple Choice", "Coding Exercise", "Bug Fixing", "Definitions"])
    
    # Add a button to generate the quiz
    if st.button("Generate Quiz"):
        # Call a function to generate and display the quiz questions
        generate_quiz(quiz_type, coding_subject)

# Define a function to generate and display the quiz questions
def generate_quiz(quiz_type, coding_subject):
    # Display quiz parameters
    st.subheader("Quiz Type: " + quiz_type)
    st.subheader("Coding Subject: " + coding_subject)

    # Add logic to generate quiz questions based on the selected parameters
    if quiz_type == "Multiple Choice":
        # Generate a multiple choice question
        question = generate_multiple_choice_question(coding_subject)
        # Display the question
        st.write("Question:", question)
        # Get the user's answer
        user_answer = st.text_input("Your Answer")
        # Compare the user's answer to the correct answer
        correct_answer = get_correct_answer(question)
        # Evaluate the answer and return a score
        score = evaluate_answer(user_answer, correct_answer)
        st.write("Score:", score)
    # elif quiz_type == "Coding Exercise":
    #     # Generate a coding exercise question
    #     question = generate_coding_exercise_question(coding_subject)
    #     # Display the question
    #     st.write("Question:", question)
    #     # Get the user's answer
    #     user_answer = st.text_area("Your Answer")
    #     # Compare the user's answer to the correct answer
    #     correct_answer = get_correct_answer(question)
    #     # Evaluate the answer and return a score
    #     score = evaluate_answer(user_answer, correct_answer)
    #     st.write("Score:", score)
    # elif quiz_type == "Bug Fixing":
    #     # Generate a bug fixing question
    #     question = generate_bug_fixing_question(coding_subject)
    #     # Display the question
    #     st.write("Question:", question)
    #     # Get the user's answer
    #     user_answer = st.text_area("Your Answer")
    #     # Compare the user's answer to the correct answer
    #     correct_answer = get_correct_answer(question)
    #     # Evaluate the answer and return a score
    #     score = evaluate_answer(user_answer, correct_answer)
    #     st.write("Score:", score)
    # elif quiz_type == "Definitions":
    #     # Generate a definitions question
    #     question = generate_definitions_question(coding_subject)
    #     # Display the question
    #     st.write("Question:", question)
    #     # Get the user's answer
    #     user_answer = st.text_input("Your Answer")
    #     # Compare the user's answer to the correct answer
    #     correct_answer = get_correct_answer(question)
    #     # Evaluate the answer and return a score
    #     score = evaluate_answer(user_answer, correct_answer)
    #     st.write("Score:", score)
    else:
        st.write("Invalid quiz type selected")

    # Define functions to generate questions, get correct answers, and evaluate answers

    def generate_multiple_choice_question(coding_subject):
        response = client.Completions.create(
            engine="davinci-codex",
            prompt=f"Generate a multiple choice question for the coding subject: {coding_subject}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        question = response.choices[0].text.strip()
        return question
        
    # def generate_bug_fixing_question(coding_subject):
    #     response = client.Completions.create(
    #         engine="davinci-codex",
    #         prompt=f"Generate a bug fixing question for the coding subject: {coding_subject}",
    #         max_tokens=100,
    #         n=1,
    #         stop=None,
    #         temperature=0.7,
    #     )
    #     question = response.choices[0].text.strip()
    #     return question
    
    # def generate_definitions_question(coding_subject):
    #     response = client.Completions.create(
    #         engine="davinci-codex",
    #         prompt=f"Generate a bug fixing question for the coding subject: {coding_subject}",
    #         max_tokens=100,
    #         n=1,
    #         stop=None,
    #         temperature=0.7,
    #     )
    #     question = response.choices[0].text.strip()
    #     return question

    # Answer comparrison

    def get_correct_answer(question):
        # Use OpenAI to generate the correct answer for the given question
        response = client.Completions.create(
            engine="davinci-codex",
            prompt=f"Generate the correct answer for the question: {question}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        correct_answer = response.choices[0].text.strip()
        return correct_answer
    
    def evaluate_answer(user_answer, correct_answer):
        # Compare the user's answer to the correct answer and return a score
        if user_answer.lower() == correct_answer.lower():
            score = 1
        else:
            score = 0
        return score