class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        '''Checking if the questions are not over'''
        return self.question_number < len(self.question_list)
           

    def NextQuestion(self):
        '''Ask the current question and making the next one'''
        cur_qustion = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f'Q.{self.question_number}: {cur_qustion.text} (True/False)?: ')
        self.check_answer(user_answer, cur_qustion.answer)

    def check_answer(self, user_answer, correct_answer):
      '''Checking if the user is correct'''
      if user_answer.lower() == correct_answer.lower():
        self.score += 1
        print('You got it right')
      else:
        print('You got it wrong')

      print(f'The correct answer was: {correct_answer}.')
      print(f'Your current score is: {self.score}/{self.question_number}\n\n')
