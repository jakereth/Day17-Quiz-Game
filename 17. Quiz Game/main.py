from data import question_data
from question_model import Question
from quiz_brain import Quiz

questions = []

for entry in question_data:
    # Extract text and answer from the dictionary
    text = entry["text"]
    answer = entry["answer"]
    
    # Create an instance of Question and append it to the list
    question = Question(text, answer)
    questions.append(question)

quiz = Quiz(questions)

while quiz.still_has_questions():
    cont = input("Would you like to continue? Y for yes\nN for no").lower()
    if cont == 'n':
        print(f"Your final score is: {quiz.score}/{quiz.questionNum}")
        break
    else:
        quiz.nextQuestion()