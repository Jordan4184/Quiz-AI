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

# Define the function to generate quiz questions and answers
def generate_quiz_question(quiz_type, coding_subject, difficulty):
    system_prompt = "You are a creative and diverse computer programming and coding quiz generator."
    user_prompt = (
        f"Create a unique and detailed {difficulty.lower()} {quiz_type.lower()} question specifically about {coding_subject}. "
        "The answer should be clearly separated by stating 'Answer:' immediately following the question. "
        "Indicate the correct answer clearly. Avoid repetitive questions."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=350
        )
        content = response.choices[0].message.content.strip()
        answer_keyword = "Answer:"
        split_content = content.split(answer_keyword)

        if len(split_content) == 2:
            question = split_content[0].replace("**", "").strip()
            answer = split_content[1].strip()
            return question, answer
        else:
            st.error("Received unexpected format from API.")
            return "Error in API response format, please try again.", None
    except Exception as e:
        st.error(f"Failed to generate question: {str(e)}")
        return "Error generating question", None


# Define a function to evaluate the user's answer using OpenAI
def evaluate_answer(user_answer, correct_answer, quiz_type):
    evaluation_prompt = (
        f"Evaluate how correct the answer '{user_answer}' is for a {quiz_type.lower()} question with the correct answer '{correct_answer}'. "
        "Consider partial correctness and provide feedback on which parts are correct and which parts are incorrect. "
        "Provide a clear 'Yes' or 'No' at the end to indicate if the answer is mostly correct."
        "Avoid repeating the question in the evaluation. Keep the evaluation concise. Provide a code example if relevant."
        "If the answer is multiple choice, the user does not need to include explanation with the answer and providing a single letter answer is acceptable (e.g., 'A')."
    )
    messages = [
        {"role": "user", "content": evaluation_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=250  # Allow for a more verbose response
        )
        evaluation_content = response.choices[0].message.content.strip().split("\n")
        feedback = "\n".join(evaluation_content[:-1]).strip()
        evaluation = evaluation_content[-1].strip().lower()
        return evaluation == "yes", feedback
    except Exception as e:
        st.error(f"Failed to evaluate the answer: {str(e)}")
        return False, str(e)


# Define the Streamlit app structure
def main():
    st.title("Coding Quiz Generator")
    st.header("Quiz Parameters")

    # Initialize score and attempts if not already done
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0  # Initialize attempts

    coding_subject = st.text_input("Enter Coding Subject")
    quiz_type = st.selectbox("Select Quiz Type", ["Multiple Choice", "Coding Exercise", "Bug Fixing", "Definitions"])
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Generate Quiz"):
        question, correct_answer = generate_quiz_question(quiz_type, coding_subject, difficulty)
        st.session_state.question = question
        st.session_state.correct_answer = correct_answer
        st.session_state.user_answer = ""  # Clear previous answers when a new question is generated

    if 'question' in st.session_state and st.session_state.question != "Error in API response format, please try again.":
        st.subheader("Question")
        st.write(st.session_state.question)
        
        if quiz_type == "Coding Exercise":
            user_answer = st.text_area("Your Answer", key="user_answer")
        else:
            user_answer = st.text_input("Your Answer", key="user_answer")

        if st.button("Submit Answer"):
            st.session_state.attempts += 1  # Increment attempts whenever an answer is submitted
            is_correct, feedback = evaluate_answer(user_answer, st.session_state.correct_answer, quiz_type)
            if is_correct:
                st.success("Correct!")
                st.session_state.score += 1  # Update score if correct
            else:
                st.error(f"Incorrect. {feedback}. The correct answer is {st.session_state.correct_answer}")

            st.subheader(f"Score: {st.session_state.score}/{st.session_state.attempts} correct")  # Display the updated score

if __name__ == "__main__":
    main()

#README.md

#AI Coding Quiz Generator

#The code above is a Streamlit app that generates coding quiz questions and evaluates user answers using the OpenAI API.
#The app allows users to input a coding subject, select a quiz type (e.g., multiple choice, coding exercise), and choose a difficulty level.
#When the user clicks the "Generate Quiz" button, the app generates a quiz question based on the user inputs.
#The user can then input their answer and click the "Submit Answer" button to evaluate their response.
#The app uses the OpenAI API to generate quiz questions and evaluate user answers based on the correct answer.
#The user's score and number of attempts are displayed after each question.
#The app provides feedback on whether the user's answer is correct or incorrect and displays the correct answer.
#The app also provides feedback on the user's answer, including partial correctness and areas of improvement.
#The user can continue answering questions and see their updated score and number of attempts after each question.


#Functionality changes: 

#Adjust prompt engineering to better guide the model in generating questions
#Need to adjust answer prompts to accept multiple choice questions and coding questions with more forgiving evaluation
#Add more error handling and user feedback for better user experience
#Add more quiz types and difficulty levels for a more diverse set of questions
#Add a timer for each question to make the quiz more challenging
#Add a feature to save and share quiz results
#Add a feature to review past quiz questions and answers
#Add a feature to create custom quizzes based on user preferences

