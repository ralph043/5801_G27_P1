import json
import random
from model import Model
from model import Question

#class Controller:

def chooseSettings():
    # Ask user for file name and read file line by line into an array
    file_name = input("Enter input file name: ")

    while True:
        try:
            file = open(file_name, "r")
            break
        except:
            print("File not found. Please try again.")
            file_name = input("Enter file name: ")

    lines = file.readlines()
    file.close()

    num_of_lines = len(lines)
    #  a valid input of either 'mc' for multiple choice or 'fib' for fill in the blank")

    #ask for lms type, question type, number of questions, and if they want to remove comments.
    lms_type = input("Enter LMS type: ")

    while True:
        question_type = input("Enter question type:('mc' for multiple choice / 'fib' for fill in the blank) ")

        if question_type == "mc" or question_type == "fib":
            break
        else:
            print("Please enter a valid question type of either 'mc' for multiple choice or 'fib' for fill in the blank")

    while True:
        try:
            num_questions = int(input("Enter number of questions: "))
            if (num_questions <= 0 or num_questions > num_of_lines):
                print("Number of questions must be greater than 0, and less than the number of lines in the file inputted. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid Input, Please enter a number.")

    while True:
        remove_comments = input("Remove comments? (y/n): ")
        if remove_comments == "y" or remove_comments == "n":
            break
        else: 
            print("Please enter a valid input of either y or n")

    #if they want to remove comments, ask the user if they want to delete comments or combine them with the next line of code
    if remove_comments == "y":
        while True:
            remove_comments = input("Delete comments or combine them with the next line of code? (d/c): ")
            #if they want to delete comments, remove any line that starts with a # or // from lines, otherwise combine each index of lines starting with a # or // with the next index of lines
            if remove_comments == "d":
                lines = [line for line in lines if not line.startswith("#") and not line.startswith("//")]
                break
            elif remove_comments == "c":
                checker = len(lines)
                for i in range(len(lines)):
                    
                    if lines[i].startswith("#") or lines[i].startswith("//"):
                        lines[i] = lines[i] + lines[i+1]
                        lines.pop(i+1)
                        checker = checker - 1   
                    if(i == checker-1): 
                        break
                         
                #lines = [line for line in lines if line != ""]
                break
            else:
                print("Invalid input, please enter either d or c")
    
    #ask the user if they want to declare sets of non-order specific lines of code
    
    while True:
        declare_sets = input("Declare sets of non-order specific lines of code? (y/n): ")
        if declare_sets == "y" or declare_sets == "n":
            break
        else: 
            print("Please enter a valid input of either y or n")
    
    #if they want to declare sets, loop until start is -1, ask the user for start line and end line and combine all lines in between, inclusive, into one line and replace the lines in between with that line
    if declare_sets == "y":
        print("Disclaimer: Lines are 0-indexed and if comments were removed, lines may have changed")
        start = 0
        while start > -1:
            start = int(input("Enter start line between 0 and " + str(len(lines)) + " or enter -1 to exit: "))
            
            
            if start > len(lines):
                print("Invalid input, please enter a start line less than or equal to the number of lines")
                continue
            elif start > -1:
                end = int(input("Enter end line: "))
                if start >= end:
                    print("Start line must be less than end line")
                    continue
                elif end >= len(lines):
                    print("Invalid input, please enter a end line less than or equal to the number of lines")
                    continue
                combined = ""
                for i in range(start, end+1):
                    combined += lines[i]
                lines[start] = combined
                for i in range(start+1, end+1):
                    lines.pop(start+1)
            

    #print lines, this is for testing and version 0.1 only, this can be modified to send lines to the question generator when it is implemented
    #for line in lines:
    #    print(line)

    #declare new model object needed for question generator and later formatting for exporting to lms system
    global model 

    model= Model(lms_type, question_type, num_questions, lines)
    generateQuestions(model)

def MCQuestionGeneratorHelper(correct_line):

    #create a list to hold the correct line and 3 mutants

    options = []

    #loop for 3 iterations, in each iteration create a variation of the correct line by reordering the elements of the line and adding it to the list
    
    for i in range(3):
            
            #create a list of the elements of the line

            line_list = correct_line.split()

            #shuffle the list

            random.shuffle(line_list)

            #convert the list back into a string

            line = " ".join(line_list)

            #check if the line is already in the list, if it is, re run the loop, otherwise add it to the list

            if line in options:
                i = i - 1
            else:
                options.append(line)
            
    #add the correct line to the list and shuffle the list

    options.append(correct_line)
    random.shuffle(options)

    #create a variable to hold the index of the correct line in the list

    correct_index = options.index(correct_line)

    #create a question object with the list of options and the index of the correct line and return it

    q1 = Question(options, correct_index)
    return q1



def FIBQuestionGeneratorHelper(correct_line):
    #randomly generate a number between 0 and the length of the line, this will be the index of the first blank
    first_blank = random.randint(0, len(correct_line) - 1)
    
    #randomly generate a number between 1 and the length of the line remaining after the first index, this will be the number of indexes deleted

    num_deleted = random.randint(1, len(correct_line) - first_blank)

    #create a list of the elements of the line

    line_list = correct_line.split()

    #loop through each index from first blank to first blank + num deleted and set the value of that index to "____"

    for i in range(first_blank, first_blank + num_deleted):
        line_list[i] = "____"


    #convert the list back into a string

    fib_line = " ".join(line_list)

    #create a list with the correct line and the fib line

    options = [correct_line, fib_line]

    #create a question object with the list of options and the index of the correct line and return it

    q1 = Question(options, 0)
    return q1






def generateQuestions(model):
    
    #create a list of objects named "questionsToReturn"

    questionsToReturn = []

    question_type = model.get_question_type()
    questions = model.get_lines()
    numOfQuestions = model.get_num_questions()

    #variable to count number of questions generated

    count = 0

    #if question type is "mc" multiple choice code for multiple choice goes here

    if (question_type == "mc"):

        #break down list into sublist
        
        for line in questions:
            if (count > numOfQuestions):
                break
            questionsToReturn.append(MCQuestionGeneratorHelper(line))
            count = count + 1


    #if question type is fill in the blank code for fill in the blank goes here

    elif (question_type == "fib"):
        
        #loop through each line in the list

        for line in questions:
            if (count > numOfQuestions):
                break
            #call helper function to generate a fill in the blank variation of the line

            questionsToReturn.append(FIBQuestionGeneratorHelper(line))
            count = count + 1


    data=[]
    for feature in questionsToReturn:
        data.append({"Question Options: ":feature.get_options()})
        data.append({"Correct Option index(0 indexed): ":feature.get_correct_answer()})
    jsonData=json.dumps(data)

    json_object = json.loads(jsonData)

    json_formatted_str = json.dumps(json_object, indent=2)

    # print formatted JSON Object, this is for testing and version 0.2 only, this will be changed when implementing file output

    print(json_formatted_str)

