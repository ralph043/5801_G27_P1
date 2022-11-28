#include<iostream>
#include<array> 
#include<tuple> 
#include<string>
#include<cstring>
#include<vector>
#include "stdio.h"
#include "model.cpp"
#include<fstream>
using namespace std;

class controller {
    public:

   
    

      string* mergeLines(int start, int end, string* myarr){
         int tempSize = myarr->size(); 
         string* temparr[tempSize];
         string tempstr;
         for(int i = 0; i < myarr->size(); i++){
            if(i < start){
               (*temparr)[i] = (*myarr)[i];
            }
            else if (i >= start && i <= end) {
               tempstr += ((*myarr)[i] + "\n");
            }
            else {
               break;
            }
         }

         (*temparr)[start] = tempstr;
         int temparrindex = start+1;

         for(int j = end; j < myarr->size(); j++){
            (*temparr)[temparrindex] = (*myarr)[j];
            temparrindex++;
         }
         return *temparr;
      } 


      void chooseSettings(){
            cout << "C" << endl;
            model model1;
            cout << "D" << endl;
            std::cout << "Enter file path" << std::endl;
            char* tempFP;
            std::cin >> tempFP;

            model1.setFilePath(tempFP);


            //ask for lms type, question type and if they want to annotate.
            std::cout << "Enter LMS type" << std::endl;
            std::string tempLMS;
            std::cin >> tempLMS;

            model1.setLmsType(tempLMS);

            std::cout << "Enter question type" << std::endl;
            std::string tempQT;
            std::cin >> tempQT;

            model1.setQuestionType(tempQT);

            std::cout << "Do you want to annotate? (y/n)" << std::endl;
            std::string tempA;
            std::cin >> tempA;
                //if (no annotations), read through entire file, add each line to vector iff line doesnt start with "//"

            std::ifstream input(tempFP);
            std::ifstream tempInput(tempFP);

            //set array of size equal to the total number of lines in the file
            std::string line;
            int lineCount = 0;
            int commentCount = 0;
            std::string comments = "//";
            for (std::string line; getline(tempInput, line);)
            {
               lineCount++;
               int check = line.compare(0,2, comments);
               // if( ((strcmp(line[0], comments[0])) == 0) && ((strcmp(line[1], comments[1])) == 0) ) {
               //    lineCount--;
               //  }
               if(check == 0) {
                  commentCount++;
               }
            }

            int commentless = lineCount - commentCount;

            int ind = 0;
            if(tempA == "n"){
               string* fileArray[lineCount];
               for( std::string line; getline( input, line ); ){
                  (*fileArray)[ind] = line;
               }
               
               for(int i = 0; i < lineCount; i++){
               std::cout << (*fileArray)[i] << std::endl;
               }
            }
            else if(tempA == "y"){
               string* fileArray[commentless];
               std::cout<< "Would you like to choose a start and end line or group lines together? (s/g)" << std::endl;
               std::string tempAG;
               std::cin >> tempAG;

               int currentLine = 0;
               
               if(tempAG == "s"){
                  
                  std::cout << "Enter start line" << std::endl;
                  int tempSL;
                  std::cin >> tempSL;


                  std::cout << "Enter end line" << std::endl;
                  int tempEL;
                  std::cin >> tempEL;


                  //read through file, add each line to vector iff line doesnt start with "//" and is between start and end line
                  for( std::string line; getline( input, line ); ){
                     if( currentLine >= tempSL && currentLine <= tempEL){
                        int check = line.compare(0,2, comments);
                        if(check == 0) {
                           (*fileArray)[ind] = line;
                           ind++;
                        }
                     }
                  }
               }

               else if(tempAG == "g"){
               //ask user for first line in grouping of non-order dependent line as well as end line to be inputted into string of vectors, read each line up to but not including start line and add to vector iff line doesnt start with "//", then combine each line between start line and end line into one string and push to vector, then repeat until entered start line is -1
                 int startLine = 0;
                 int endLine = 0;


                 while(startLine != -1){
                  cout << "Enter start line. (or -1 to exit)" << endl;
                  cin >> startLine;
                  if(startLine == -1){
                     break;
                  }
                  if (endLine <= startLine){
                     cout << "End Line must be greater than start line. Please try again." << endl;
                     continue;
                  }
                 (*fileArray) = mergeLines(startLine, endLine, (*fileArray));
                  
                 }
               }
               for(int i = 0; i < (commentless); i++){
               std::cout << (*fileArray)[i] << std::endl;
               }
            }
            // model1.setFile(tempV);   
            //print tempV
            


                //elif (yes annotations), ask for start line, then read to said line, and ask for end line. Then starting from the start line ask how many lines until next unique code line, loop until end line
            
       }
       
       

        void generateQuestions(){
            
       }

         

    private:
          
};

 int main(int argc, char const *argv[])
    {
      cout << "Welcome to the Question Generator!" << endl;
      controller* test = new controller();
      cout << "A" << endl;
      test->chooseSettings();
      cout << "B" << endl;
      
    }

