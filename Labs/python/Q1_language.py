
'''
In this activity, you will create a word translator that will translate a word in Language A to Language B where A and B are given as input to the program. For simplicity, there are only three languages: english, hindi and punjabi [no testcase will have a language other than these three languages, you may hardcode this as well] and one word in any of these languages can be translated to only one word in any other language. Only the words present in the files are considered to be in the vocabulary of the language. Also note that all words will be in lower case. You are given a file translations.csv (comma separated values), which has 4 columns. Column-1 has the name of Language-1, Column-2 has word in Language-1, Column-3 has the name of Language-2, Column-4 has word in Language-2. 
For example: hindi,aasmaan,punjabi,ambar means that aasmaan in hindi translates to ambar in punjabi. 

LabDirectory contains the following files:
- language.py: This is the python script that you need to complete.
- testcases: This folder contains the testcases for the python script.
- translations.csv: This file contains the translation data.

Tasks:

1. Your python script will accept command line arguments and based on the query type provided as first argument to the script, interpret other command line arguments, perform operations and finally print the result on terminal.
2. There are 3 types of queries that you need to handle (language will always be one of english, hindi or punjabi):

Query 1: Given a language, print its vocabulary i.e all distinct words that appear in translations.csv belonging to the given language in the form of a list sorted lexicographically in reverse order.
For example: ```python3 language.py 1 english``` gets you all english words present in translations.csv.

Query 2: Given two languages A and B, print all translations available from Language A to Language B in the form of a list of tuples sorted lexicographically based on first element of tuple where the first element of each tuple is a word from Language A and the second element of the tuple is the corresponding translation in Language B.
For example: ```python3 language.py 2 hindi punjabi``` gets you all hindi to punjabi translations that can be interpreted from translations.csv.

Query 3: Given two languages A and B and a word w in Language A, print the translation of word w in Language B. If the translation is not available, print "UNK" without quotes.
For example: ```python3 language.py 3 punjabi hindi ambar``` gets you a hindi translation of punjabi word ambar that can be interpreted from translations.csv.

Important Points:
- It might be possible that there is an indirect translation available from Language A to Language B via Language C (check Example given below for clarity). There will be some testcases that will particularly check if your program handles such cases and they have a weightage of 2 marks in hidden testcases.
- So if you dont handle indirect translation, then you won't get all testcases
- Please run the autograder script to check if your program passes on public testcases.

Submission:
- You need to submit the python script (language.py) only.



EXAMPLE:
Suppose the file translations.csv is as follows:
punjabi,bhain,english,sister
hindi,bhagwan,punjabi,rab
english,mother,hindi,maa
english,god,punjabi,rab

Test Case 1
$ python3 language.py 1 punjabi

Output:
[rab, bhain]

Explanation:
Out of 8 words, 3 are punjabi words and out of them only 2 are distinct. Also in reverse lexicographical order rab comes before bhain.


Test Case 2
$ python3 language.py 2 hindi english

Output:
[('bhagwan', 'god'), ('maa', 'mother')]

Explanation:
There is an indirect translation of bhagwan from hindi to english, bhagwan (hindi) -> rab (punjabi) -> god (english). There is a direct translation of maa from hindi to english. Also bhagwan comes before maa in lexicographical order.

Test Case 3
$ python3 language.py 3 english hindi god

Output:
bhagwan

Explanation:
There is an indirect translation of god from english to hindi, god (english) -> rab (punjabi) -> bhagwan (hindi).
'''

import sys

f = open("translations.csv", 'r')
data = {}

for line in f:
    line = line.strip().split(",")
    if line[0] in data:
        pass
    elif len(data) == 0:
        data[line[0]] = []
    else:
        data[line[0]] = [None for _ in list(data.values())[0]]
    
    if line[2] in data:
        pass
    else:
        data[line[2]] = [None for _ in data[line[0]]]
    
    if line[1] in data[line[0]]:
        indx = data[line[0]].index(line[1])
        data[line[2]][indx] = line[3]
    elif line[3] in data[line[2]]:
        indx = data[line[2]].index(line[3])
        data[line[0]][indx] = line[1]
    else:
        for i in data.keys():
            if i not in {line[0], line[2]}:
                data[i].append(None)
        data[line[0]].append(line[1])
        data[line[2]].append(line[3])

command = int(sys.argv[1])

match command:
    case 1:
        print(sorted([i for i in data[sys.argv[2]] if i is not None], reverse=True))
    case 2:
        lang1 = sys.argv[2]
        lang2 = sys.argv[3]
        print(sorted([(data[lang1][indx], data[lang2][indx]) for indx in range(len(data[lang1])) if data[lang1][indx] and data[lang2][indx]]))
    case 3:
        lang1 = sys.argv[2]
        lang2 = sys.argv[3]
        word = sys.argv[4]
        if word in data[lang1]:
            trans = data[lang2][data[lang1].index(word)]
            print(trans if trans else "UNK")
        else:
            print("UNK")

---------------------------------------------------------

import sys

class word:
    def __init__(self, language, name, relations):
        self.language = language
        self.name = name
        self.relations = relations
    
    def add_relation(self, _word):
        self.relations.append(_word)

    def __bool__(self):
        return bool(self.name)

#interpreting the connections from translations.csv
words = []
with open("translations.csv", "r") as file:
    line = file.readline().strip("\n")
    fields = line.split(sep=",")

    while line:
        word1 , word2 = 0, 0
        for x in words:
            if x.name == fields[1]:
                word1 = x
            elif x.name == fields[3]:
                word2 = x

        if word1 == 0 : 
            word1 = word(fields[0], fields[1], [])
            words.append(word1)
        if word2 == 0 : 
            word2 = word(fields[2], fields[3], [])
            words.append(word2)


        # word_2 = word(fields[2], fields[3])

        word1.add_relation(word2)
        word2.add_relation(word1)

        line = file.readline().strip("\n")
        fields = line.split(sep=",")


if sys.argv[1] == "1":
    out = []
    for x in words:
        if x.language == sys.argv[2]:
            out.append(x.name)
    # print(out.sort()) out.sort RETURNS None
    out.sort(reverse=True)
    print(out)

if sys.argv[1] == "2":
    out = []
    for x in words:
        found = False
        if x.language == sys.argv[2]:

            for y in x.relations:
                if y.language == sys.argv[3]:
                    out.append((x.name, y.name))
                    found = True
                    break
            if not found:
                for y in x.relations:
                    for z in y.relations:
                        if z.language == sys.argv[3]:
                            out.append((x.name, z.name))
                            found = True
                            break
                    break  
    out.sort(key = lambda x: x[0])
    print(out)      

if sys.argv[1] == "3":

    for x in words:
        found = False
        if x.name == sys.argv[4]:

            for y in x.relations:
                if y.language == sys.argv[3]:
                    print(y.name)
                    found = True
                    quit()
            if not found:
                for y in x.relations:
                    for z in y.relations:
                        if z.language == sys.argv[3]:
                            print(z.name)
                            found = True
                            quit()
            if not found:
                print("UNK")
                quit()
    print("UNK")
