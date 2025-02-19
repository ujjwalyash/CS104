**Activity**

There is a directory named inputs, which contains sub-directories, sub-sub-directories, and files. The sub-directories also contain some files. In this problem, you have to do a series of tasks:

Copy all the text files (*.txt) to a folder named outputs (without quotes)

Concatenate all the text files into a single file with line numbers (cat.txt). Files must be concatenated in lexicographic order of their names. (see example in testcases)

Count the number of non-empty lines in the provided text files and output to lines.txt.

Note: all files other than *.txt must be ignored. The three tasks can be done in any order. Write all the commands in submission.sh. You have to submit only the submission.sh file and not the two text files, or the folder you have generated.

Example: Suppose the input directory structure is as follows:

    input
    |-- project1/
        |--file1.txt
        |-- file2.txt
        |-- project1-1/
        |--file3.txt

    |-- project2/
        |-- file4.jpg
        |-- file5.txt
        |-- file6.docx
    |-- project3/
        |-- file7.txt
        |-- file8.txt 

Then the output should be:

    output/
        |--file1.txt
        |--file2.txt
        |--file3.txt
        |--file5.txt
        |--file7.txt
        |--file8.txt

There will also be two text files that you create:
    cat.txt
    lines.txt 