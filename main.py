from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
import json

# Trivia API request
response = requests.get(
    'https://opentdb.com/api.php?amount=12&category=23&difficulty=medium&type=boolean')
# Formating the json response
question_dict = json.loads(response.text)
# List comprehensive
question_bank = [Question(question['question'], question['correct_answer'])
                 for question in question_dict['results']]
                 
# Code for the data file(without the api) ----
# question_bank = [Question(question['text'], question['answer']) for question in question_dict]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.NextQuestion()

print(
    f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
