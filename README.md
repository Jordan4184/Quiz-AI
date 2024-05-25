# AI Coding Quiz Generator

This project is a Streamlit app that generates coding quiz questions and evaluates user answers using the OpenAI API. The app allows users to input a coding subject, select a quiz type, and choose a difficulty level. It then generates a quiz question based on the user inputs and evaluates the user's response.

## Features

- **Quiz Generation**: Generate unique and detailed quiz questions based on the selected coding subject, quiz type, and difficulty level.
- **Answer Evaluation**: Evaluate user answers for correctness, providing feedback on partial correctness and areas of improvement.
- **Scoring**: Track user score and number of attempts, displaying updated results after each question.
- **User Feedback**: Provide feedback on whether the user's answer is correct or incorrect and display the correct answer if the user is incorrect.

## Quiz Types

- Multiple Choice
- Coding Exercise
- Bug Fixing
- Definitions

## Difficulty Levels

- Easy
- Medium
- Hard

## Prerequisites

- **Python**: Make sure you have Python installed (>= 3.7).
- **Streamlit**: Install Streamlit using pip.
- **Dotenv**: Install python-dotenv using pip.
- **OpenAI**: Install openai using pip.
- **Metapub**: Install metapub using pip.

## How to Run the App

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Jordan4184/PubMed_AI.git
    cd PubMed_AI/In\ Progress
    ```

2. **Install the Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the project directory.
    - Add your OpenAI API key to the `.env` file:
        ```env
        OPEN_AI_KEY=your_openai_api_key
        ```

4. **Run the Streamlit App**:
    ```sh
    streamlit run Working_PubMedAI_Project.py
    ```

## Usage

1. **Enter Coding Subject**: Type the subject you want the quiz to focus on.
2. **Select Quiz Type**: Choose the type of quiz (Multiple Choice, Coding Exercise, Bug Fixing, Definitions).
3. **Select Difficulty**: Choose the difficulty level (Easy, Medium, Hard).
4. **Generate Quiz**: Click the "Generate Quiz" button to generate a quiz question.
5. **Submit Answer**: Input your answer and click the "Submit Answer" button to evaluate your response.
6. **View Feedback and Score**: See feedback on your answer and view your score and number of attempts.

## Future Enhancements

- Adjust prompt engineering to better guide the model in generating questions.
- Enhance answer evaluation to accept multiple choice questions and coding questions with more forgiving evaluation.
- Add more error handling and user feedback for better user experience.
- Expand quiz types and difficulty levels for a more diverse set of questions.
- Implement a timer for each question to make the quiz more challenging.
- Add a feature to save and share quiz results.
- Add a feature to review past quiz questions and answers.
- Add a feature to create custom quizzes based on user preferences.

- ## Acknowledgments
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/) For providing primary code body and architecture, as well as integration to streamlit
- [dotenv](https://github.com/theskumar/python-dotenv)
- [Metapub](https://github.com/metapub/metapub)
