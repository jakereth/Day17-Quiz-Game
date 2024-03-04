from data import question_data

questions = []

for entry in question_data:
    # Extract text and answer from the dictionary
    text = entry["text"]
    answer = entry["answer"]
    
    # Create an instance of Question and append it to the list
    question = Question(text, answer)
    questions.append(question)

Quiz(questions)