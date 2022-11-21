#include <iostream>
#include <string>
#include "stdio.h"

class model {
    public:
        std::string getQuestionType(){
            return this->questionType;
        }

        void setQuestionType(std::string newQuestionType){
            this->questionType = newQuestionType;
        }

        int getNumQuestions(){
            return this->numQuestions;
        }

        void setNumQuestions(int newNumQuestions){
            this->numQuestions =  newNumQuestions;
        }

        std::string getLmsType(){
            return this->lmsType;
        }

        void setLmsType(std::string newLmsType){
            this->lmsType = newLmsType;
        }

        std::vector<std::string> getLineTuples(){
            return this->lineTuples;
        }

        void setLineTuples(std::vector<std::string> newLineTuples){
            this->lineTuples = newLineTuples;
        }


    private:
        std::string questionType;
        int numQuestions;
        std::string lmsType;
        std::vector<std::string> lineTuples;
        std::string filePath;
        
};