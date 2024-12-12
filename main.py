from question_data import question_data
from question_model import Question


question_bank = []
for data in question_data:
    question = Question(q_text=data["text"],q_answer=data["answer"])
    question_bank.append(question)