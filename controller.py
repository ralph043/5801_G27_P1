from model import Model

#class Controller:

    


    


def chooseSettings():
    # Ask user for file name and read file line by line into an array
    file_name = input("Enter file name: ")
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    #ask for lms type, question type, number of questions, and if they want to remove comments.
    lms_type = input("Enter LMS type: ")
    question_type = input("Enter question type: ")
    num_questions = input("Enter number of questions: ")
    while True:
        remove_comments = input("Remove comments? (y/n): ")
        if remove_comments == "y" or remove_comments == "n":
            break
        else: 
            print("Please enter a valid input of either y or n")
            continue 

    #if they want to remove comments, ask the user if they want to delete comments or combine them with the next line of code
    if remove_comments == "y":
        while True:
            remove_comments = input("Delete comments or combine them with the next line of code? (d/c): ")
            #if they want to delete comments, remove any line that starts with a # or // from lines, otherwise combine each index of lines starting with a # or // with the next index of lines
            if remove_comments == "d":
                lines = [line for line in lines if not line.startswith("#") and not line.startswith("//")]
                break
            elif remove_comments == "c":
                for i in range(len(lines)):
                    if lines[i].startswith("#") or lines[i].startswith("//"):
                        lines[i] = lines[i] + lines[i+1]
                        lines.pop(i+1)
                lines = [line for line in lines if line != ""]
                break
            else:
                print("Invalid input, please enter either d or c")
                continue
    
    #ask the user if they want to declare sets of non-order specific lines of code
    
    while True:
        declare_sets = input("Declare sets of non-order specific lines of code? (y/n): ")
        if declare_sets == "y" or declare_sets == "n":
            break
        else: 
            print("Please enter a valid input of either y or n")
            continue 
    
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
                elif end > len(lines):
                    print("Invalid input, please enter a end line less than or equal to the number of lines")
                    continue
                combined = ""
                for i in range(start, end+1):
                    combined += lines[i]
                lines[start] = combined
                for i in range(start+1, end+1):
                    lines.pop(start+1)
            

    #print lines, this is for testing and version 0.1 only, this can be modified to send lines to the question generator when it is implemented
    for line in lines:
        print(line)

    #declare new model object needed for question generator and later formatting for exporting to lms system
    model = Model(lines, lms_type, question_type, num_questions)
    



    
   
    


if __name__ == "__main__":
    chooseSettings()
    


