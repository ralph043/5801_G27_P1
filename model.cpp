#include<iostream>
#include<array> 
#include<tuple> 
#include<string>
#include<cstring>
#include<vector>
#include "stdio.h"
#include<fstream>
using namespace std;

class model {
    public:


        //constructor with default values
        model(std::string questionType = "reordering", 
                int numQuestions = 500, 
                std::string lmsType = "canvas", 
                std::string lineTuples = {}, 
                std::string filePath = "./") {
            
            cout << "l" << endl;
            setQuestionType(questionType);
            cout<< "g" << endl;
            setNumQuestions(numQuestions);
            cout << "h" << endl;
            setLmsType(lmsType);
            cout << "i" << endl;
            setLineTuples(&lineTuples);
            cout << "j" << endl;
            setFilePath(filePath);
            cout << "k" << endl;
         }


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

        string* getLineTuples(){
            return *(this->lineTuples);
        }

        void setLineTuples(string* newLineTuples){
            *(this->lineTuples) = newLineTuples;
        }

        std::string getFilePath(){
            return this->filePath;
        }

        void setFilePath(std::string newFilePath){
            this->filePath = newFilePath;
        }


    private:
        std::string questionType = "reorder";
        int numQuestions = 500;
        std::string lmsType = "canvas";
        string* lineTuples[500];
        std::string filePath = NULL;
        
};



//  int main(int argc, char const *argv[])
//     {

//         return 0;
//     }
