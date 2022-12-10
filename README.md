# 5801_G27_P1
5801 Project 1 Group 27 


How to Run:
You must have python3 installed on your computer for this to run.
With a command line open utilize the cd command until you are in the directory with the source code, 
make sure the file you would like to read is in the same folder, then run the command "python3 view.py".

From this point follow the onscreen instructions, it will ask you to input the file name, for which you will enter 
the name with the file extension (e.g. tester.txt). Then enter the desired lms type and question type, 
currently these have no impact but are in place for later functionality. From there enter the desired number of questions, 
as above, this does not currently do anything but is needed for future functionality in the question generation's later versions. You will then be 
asked if you want to remove comments, respond with either "y" for yes or "n" for no. If yes you will further be asked if 
you would like comments to be deleted entirely, enter "d", or to combine the comment line with the line of code immediatly following,
enter "c". You will then be asked if you would like to combine any non-order specific lines of code, enter "n" to skip, 
otherwise a loop will begin where you will be prompted to enter the start and end lines of any lines to combine, this will 
continue until a value of "-1" is entered in the start line to end the loop. Regardless of which options are chosen, at the
end of the function the list containing the lines as they are stored will be printed to the terminal (this is temporary 
to demonstrate functionality until question generation is implemented). 
