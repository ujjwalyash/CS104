'''
Let's do some analysis of Olympics data. This problem is related to medal counting. We are providing you the files with the names like year.txt (for example 2008.txt, 2012.txt, etc.)

You are supposed to read these files one by one. The data in the files is in the format:
CountryName-#GoldMedals-#SilverMedals-#BronzeMedals
.
.
.
CountryName-#GoldMedals-#SilverMedals-#BronzeMedals

Read #GoldMedals as the number of Gold medals won by that country, and the same applies to the other notations as well. Check the testcase files (for example data/testcase1/2008.txt) for the data format.

Every information that you will read from these files, is going to be in string format. So, please do consider appropriate type conversions. Once you are done with this read part then for every country, you need to store the count of medals separately i.e. for Gold, Silver and Bronze for all the year.txt files at one place in a dictionary.

We have given an empty dictionary called totalData that you can use for storing this information. The format of this dictionary would be as follows:
{
  'CountryName': [#GoldMedals, #SilverMedals, #BronzeMedals],
  'CountryName': [#GoldMedals, #SilverMedals, #BronzeMedals]
  .
  .
  .
  'CountryName': [#GoldMedals, #SilverMedals, #BronzeMedals]
}

Now we want you to sort the country names based on their Gold medal count (in decreasing order) and in case of same number of Gold medals between two countries, tie breaking should be done based on the country names (just to avoid any sort of confusion between capital letters and small letters, we are providing you the data in small letters only).

Note: Medal count on which sorting needs to be done is the combined sum from all the year.txt files. You can store the result of this sorting in a similar format as the stored data.

A detailed example for the second testcase, the files are:
2020.txt:
india-1-2-4
japan-1-40-23
usa-20-30-40

2024.txt:
japan-1-20-50
indonesia-1-30-40
india-1-23-45
china-2-3-4

And the output dictionary:
{'usa': [20, 30, 40], 'china': [2, 3, 4], 'india': [2, 25, 49], 'japan': [2, 60, 73], 'indonesia': [1, 30, 40]}

Notice that usa is first because of having most (20) Gold medals. Among china, india and japan, since all have the same number of Gold medals (2), they will be sorted in lexicographic order.



So, at the end, you need to print the totalData dictionary as output.

Try looking for lambda functions (check reference 4) for solving this. Any implementation is fine but do not use any library other than os and argparse. You are allowed to use the "sorted" function, and you can use that on lists as well as dictionaries. Feel free to explore the ways to implement this.



For sorting a dictionary, it depends on the data contained in it, and for our case, the order will be decided as per two rules:
1. the countries should be arranged in decreasing order of Gold medals
2. in case the number of Gold medals are the same, the countries should appear in lexicographic order



You can check the expected outputs in the out folder (for example out/testcase1.txt).
If you want to view the output of your program, run it using this command:
python3 main.py --path data/testcase1/
You can replace the testcase path appropriately.

--------------------------------------------------------------------------
                References/Links
1. argument parsing (if you want to read)
https://realpython.com/command-line-interfaces-python-argparse/#adding-arguments-and-options

2. listing a directory (if you want to read)
https://www.geeksforgeeks.org/python-os-listdir-method/

3. file handling
https://realpython.com/working-with-files-in-python/

4. sorting using lambda (recommended)
https://www.w3schools.com/python/python_lambda.asp
'''

'''
    Olympics Medals
    Author: Saksham Rathi
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):
    # read the file
    with open(args.path + fileName, 'r') as file:
        # loop through data of file and set the values for the data
        for line in file:
            data = line.split("-")
            if data[0] in totalData:
                for i in range(3):
                    totalData[data[0]][i] += int(data[i+1])
            else:
                totalData[data[0]] = [0, 0, 0]
                for i in range(3):
                    totalData[data[0]][i] = int(data[i+1])

# sort as per gold medals and break ties lexicographically
totalData = dict(sorted(totalData.items(), key = lambda x : (-x[1][0], x[0])))
print(totalData)
