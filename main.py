from question_data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question = Question(q_text=data["text"],q_answer=data["answer"])
    question_bank.append(question)

start_quiz = QuizBrain(question_list=question_bank)
start_quiz.next_question()