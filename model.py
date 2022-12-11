class Model:
    def __init__(self, lms_type, question_type, num_questions, lines):
        self.lms_type = lms_type
        self.question_type = question_type
        self.num_questions = num_questions
        self.lines = lines
    
    def get_lms_type(self):
        return self.lms_type

    def get_question_type(self):
        return self.question_type

    def get_num_questions(self):
        return self.num_questions

    def get_lines(self):
        return self.lines

    def set_lms_type(self, lms_type):
        self.lms_type = lms_type

    def set_question_type(self, question_type):
        self.question_type = question_type

    def set_num_questions(self, num_questions):
        self.num_questions = num_questions

    def set_lines(self, lines):
        self.lines = lines

class Question:
    def __init__(self, options, correct_answer):
        self.correct_answer = correct_answer
        self.options = options 

    def get_correct_answer(self):
        return self.correct_answer
    def get_options(self):
        return self.options

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

    def set_options(self, options):
        self.options = options