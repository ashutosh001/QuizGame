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

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        user_input = input(f"Q.{self.question_number+1}: {current_question} (True/False)?: ")
        self.question_number +=1
        if user_input == current_answer:
            print("Correct")
            print(f"The correct answer was: {current_answer}")
            self.score +=1
            self.get_score()
        else:
            print("Incorrect")
            print(f"The correct answer was: {current_answer}")
            self.get_score()

        self.still_has_questions()
