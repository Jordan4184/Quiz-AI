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
def generate_quiz_question(quiz_type, coding_subject):
    system_prompt = "You are a computer programing and coding quiz generator. Please generate a quiz question and provide a clear, separate answer in a plain text format without any formatting."
    user_prompt = f"Create a detailed {quiz_type.lower()} question specifically about {coding_subject} and clearly separate the answer by stating 'Answer:' immediately following the question. Indicate the correct answer by returning only its letter (e.g., 'A', 'B', 'C', or 'D') not the entire answer. For example, 'A) Prints numbers from 0 to 4' is the entire answer, I only want you to return the letter 'A'. Do not use any special formatting like bold or italics."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=250  # Increased tokens in case of longer questions
        )
        print("API Response:", response.choices[0].message.content)

        content = response.choices[0].message.content.strip()
        # Update to handle possible bold markers or other formatting issues
        answer_keyword = "**Answer:**"
        if answer_keyword in content:
            split_content = content.split(answer_keyword)
        else:
            answer_keyword = "Answer:"
            split_content = content.split(answer_keyword)

        if len(split_content) == 2:
            question = split_content[0].replace("**", "").strip()  # Clean up any residual bold markers
            answer = split_content[1].strip()
            return question, answer
        else:
            st.error("Received unexpected format from API.")
            return "Error in API response format, please try again.", None
    except Exception as e:
        st.error(f"Failed to generate question: {str(e)}")
        return "Error generating question", None



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
    
    if st.button("Generate Quiz"):
        question, correct_answer = generate_quiz_question(quiz_type, coding_subject)
        st.session_state.question = question
        st.session_state.correct_answer = correct_answer
        st.session_state.user_answer = ""  # Clear previous answers when a new question is generated

    if 'question' in st.session_state and st.session_state.question != "Error in API response format, please try again.":
        st.subheader("Question")
        st.write(st.session_state.question)
        user_answer = st.text_input("Your Answer", key="user_answer")

        if st.button("Submit Answer"):
            st.session_state.attempts += 1  # Increment attempts whenever an answer is submitted
            if user_answer.upper().strip() == st.session_state.correct_answer.upper().strip():
                st.success("Correct!")
                st.session_state.score += 1  # Update score if correct
            else:
                st.error(f"Incorrect. The correct answer is {st.session_state.correct_answer}")

            st.subheader(f"Score: {st.session_state.score}/{st.session_state.attempts} correct")  # Display the updated score

if __name__ == "__main__":
    main()

#Add text input fucntionality for answers so that the AI can take the answer input compare it to its answer and return a level of correctness with comments about correcting it. 

#Question Difficulty Levels: Adding difficulty levels to the quiz questions could make the app more appealing to users of different skill levels.