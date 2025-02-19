# Activity 1 - Validate using regex

You have a file named collect.txt with the following contents:



sakshamrathi21 1 22b1003@iitb.ac.in submission.sh

malaikaarora01 3 22b0069@iitb.ac.in submsubission.sh

guramritsingh07 8 22b0001@iitb.ac.in submission.sh

harishankark33 2 23b0907@iitb.ac.in submission.sh

kritingupta34 3 23b0948@iitb.ac.in submission.sh

nithinkamath10 2 zerodha@iitb.ac.in trade.sh

narendramodi24 4 22b0024@iitb.ac.in submission.sh 

kavyagupta11 1 22b1053@iitb.ac.in submission.sh

## Todo

(i) Every line has the following format: username<space>number<space>email-id<space>file submitted.

(ii) You need to select the valid lines and print them back into valid.txt. The following points will be used to judge whether a line is valid or not.

(iii) Every username consists of some (>0) lowercase letters followed by a two digit number

(iv) The next number should be between 1 and 4 (both inclusive).

(v) The email address should be of the form <22b><four digit number><@iitb.ac.in> or <23b><four digit number><@iitb.ac.in>

(vi) The name of the file submitted should be submission.sh. And the line should end after submission.sh.

(vii) You need to write your unix command (maybe, sequence of commands) in commands.sh.

(viii) Print the valid lines in 'valid.txt'

(ix) Print the usernames and roll numbers(first seven characters of email-id) sorted numerically by (last four digits of) roll numbers in 'sorted.txt'

(x) If you mess up the directory, you can restore it by running bash reset.sh . Remember to save the progress before doing this.

## Output expected

So, after executing your unix command, valid.txt will be:

sakshamrathi21 1 22b1003@iitb.ac.in submission.sh

harishankark33 2 23b0707@iitb.ac.in submission.sh

kritingupta34 3 23b0948@iitb.ac.in submission.sh

narendramodi24 4 22b0024@iitb.ac.in submission.sh 

kavyagupta11 1 22b1053@iitb.ac.in submission.sh

(2nd line - submitted file name not valid; 3rd line - integer not valid; 6th line - email id not valid)



and sorted.txt will be

narendramodi24 22b0024

harishankark33 23b0707

kritingupta34 23b0948

sakshamrathi21 22b1003

kavyagupta11 22b1053

# Activity 2 - Grep the Passed!

A list of students is given with their first names, roll numbers, and a comment saying PASSED or FAILED for each student.

Goal

Write a Unix command line to print the names and roll numbers of ONLY those students who have passed, from the result.csv present in the same directory as submission.sh.

The list of students will be given in result.csv. There will only be three columns:- the first being the students first name, the second as their roll number, and the last telling PASSED or FAILED, all separated by commas ,.

Example:- If the result.csv looks like =>

Kritin,23B0948,PASSED

Hari,23B0029,PASSED

Sambhav,23B1020,FAILED

Abhi,23B1230,PASSED

After executing your command line, your output should be =>

Kritin,23B0948

Hari,23B0029

Abhi,23B1230

Apart from the result.csv in /home/labDirectory/, there are 3 more such result.csv present in testcases/ folder. When you click the Evaluate button, the autograder will check the correctness of your command line (in submission.sh) against the 3 result.csv in testcases/ folder.

Note:-

1. You can print the entries in any order. But no entry should be missing, and extra entries should not be there.
2. All the roll numbers given in result.csv will be distinct.
3. All the test cases will have only 3 columns:- first name, roll number, and PASSED or FAILED, separated by commas.
4. In case you tamper with the testcases/ folder, still the autograder will check the correctness from the original version of the testcases/ provided to you.
5. Write your command line in submission.sh.
6. If you mess up the directory, you can restore it by running 'bash reset.sh' in /home/labDirectory. Remember to save the progress before doing this.


**Hint Use the grep (as the name of title suggests :-) and cut commands.**

# Activity 3 - Find is Your Friend
You are provided with a tar file files.tar.gz you are required to untar them. Doing this you will get a directory named bigdirectory. Do the following on this directory:

1. Find all the files in the directory recursively with the name 'file_<4 digits>.txt'
2. Find all the files that end with .log.
3. Find all the files in the directory with 777 permissions.
4. Find all the files that have been modified in the last 24 hrs
5. Find all the files such that they are both larger than 100 bytes and were modified more than 7 days ago.


Write all your commands in a file submission.sh. You must output the answers to each part in their corresponding text file. 

For example, if your command for part (1) is find ________ , then write find ______ > 1.txt.


# Activity 4 - Playing with Access Controls

You are given a zip file named input.zip. You must write Unix command lines in your Docker terminal to achieve the following goals.



Goals:-

1) Unzip input.zip to get input/ folder using the unzip command.

2) All the files given in the unzipped input/ folder have read, write and execute permission to ALL users. You must change the permissions to read, write and execute permission to the user who created the files ("user (u)") and "read and execute" only to any other user ("group (g)" and "others (o)"). This will be done for ALL the contents (files or subfolders) in the input/ directory using the chmod command.

3) Zip the modified unzipped directory and name it output.zip, using the zip command.



Note:-

1. Unlike other questions, you don't have to write your commands in any file named submission.sh. You will run your commands in your terminal and prepare output.zip. The autograder will check this zip file for the correctness of your commands.
2. This directory will contain a LOT of files, so manually changing the permission to every file separately will not help. Use appropriate flags to complete the job for every file together.
3. If you mess up the directory, you can restore it by clicking on More > Hard Reset Activity. Remember to save the progress before doing this.
4. Before starting, you must install zip command by running 'apt install zip -y'.