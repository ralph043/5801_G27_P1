#include <iostream>
#include <string>
#include "stdio.h"
#include "model.cpp"

class controller {
    public:
       void chooseSettings(FILE file, bool annotations){
            model model1 = new model();

            std::cout << "Enter file path" << std::endl;
            std::string tempFP;
            std::cin >> tempFP;

            model1.setFilePath(tempFP);

            //open file -> set to arbitrary variable
            //ask for lms type, question type and if they want to annotate.
                //if (no annotations), read through entire file, add each line to vector iff line doesnt start with "//"

                //elif (yes annotations), ask for start line, then read to said line, and ask for end line. Then starting from the start line ask how many lines until next unique code line, loop until end line
            
       }

        void generateQuestions(){
            
       }

    private:
       FILE file;
};