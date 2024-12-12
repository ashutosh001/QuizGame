class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def get_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number != len(self.question_list):
            self.next_question()

    def check_answer(self,correct_ans,user_ans):
        if correct_ans == user_ans:
            self.score += 1
            print("Correct")
        else:
            print("Incorrect")
        print(f"The correct answer was: {correct_ans}")
        self.get_score()

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        user_input = input(f"Q.{self.question_number+1}: {current_question} (True/False)?: ")
        self.question_number +=1

        self.check_answer(correct_ans=current_answer,user_ans=user_input)
        self.still_has_questions()
