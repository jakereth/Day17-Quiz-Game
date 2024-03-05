class Quiz:
    #initialize the quiz with base values
    def __init__(self, qList):
        self.questionNum = 0
        self.questionList = qList
        self.score = 0

        #function to display question number and current question
    def nextQuestion(self):
         currentQuestion = self.questionList[self.questionNum]
         self.questionNum += 1
         user_answer = input(f"Q.{self.questionNum}: {currentQuestion} (True/False): ")
         self.check_answer(user_answer, currentQuestion)

        #function to check if there is still questions 
    def still_has_questions(self):
        return self.questionNum < len(self.questionList)

        #function to compare user answer to correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That was wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.questionNum}")
        print('\n')
