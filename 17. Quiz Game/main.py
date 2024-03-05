from data import question_data
from question_model import Question
from quiz_brain import Quiz
#import all files data is being used from

#create a list to store all questions
questions = []

#loop through data in question file seperating questions from answers
for entry in question_data:
    # Extract text and answer from the dictionary
    text = entry["text"]
    answer = entry["answer"]
    
    # Create an instance of Question and append it to the list
    question = Question(text, answer)
    questions.append(question)

quiz = Quiz(questions)

#loop while there is still questions and while user doesnt want to exit
while quiz.still_has_questions():
    cont = input("Would you like to continue? Y for yes\nN for no").lower()
    if cont == 'n':
        print(f"Your final score is: {quiz.score}/{quiz.questionNum}")
        break
    else:
        quiz.nextQuestion()
