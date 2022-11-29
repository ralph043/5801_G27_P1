# from model import Model
# fixture_demo.py

import pytest
from controller import *
from model import Model


def test_model(lms_type, question_type, num_questions, lines):
    # instantiating a model object

    model = Model(lms_type, question_type, num_questions, lines)

    # testing values with getters
    print(model.get_lines())
    assert (model.get_lms_type() == lms_type)
    assert (model.get_question_type() == question_type)
    assert (model.get_num_questions() == num_questions)

    # changing to new values with setters

    lines = ["changed line one", "changed line two", "changed line three", "changed line four"]
    lms_type = "changed test"
    question_type = "changed Parson"
    num_questions = 8
    model.set_lines(lines)
    model.set_lms_type(lms_type)
    model.set_question_type(question_type)
    model.set_num_questions(num_questions)

    # printing new values with getters
    
    assert (model.get_lines() == lines)
    assert (model.get_lms_type() == lms_type)
    assert (model.get_question_type() == question_type)
    assert (model.get_num_questions() == num_questions)

# def test_controller():



if __name__ == "__main__":
    lines = ["line one", "line two", "line three", "line four"]
    lms_type = "test"
    question_type = "Parson"
    num_questions = 6
    
    # testing the model class and its functions here

    test_model( lms_type, question_type, num_questions, lines)

