'''
Once upon a time, you were in a cool casino called "Dicey Haven". It was loud with dice rolling and people having a good time. You took a break from your usual coding stuff and decided to try a game (or your luck?).
You found a table with a sign that said, "Dice Sum Challenge: Count the Ways!" A friendly person explained the task: count how many ways you can get a sum 'n' by rolling a dice multiple times, where each roll gives you a number from 1 to 6.
Thinking about it for a bit, you figured you needed a Python script to solve this. Please write this python script in main.py.
Usage: python3 main.py {n}
(The number n will be provided as a command line argument.)

For example, if you run: "python3 main.py 3". Your output should be a single integer 4.
As, there are 4 ways to form the number 3: (1+1+1, 1+2, 2+1, 3).

Also, you need to print your result modulo 1000000007. (1e9+7)

(Note: To pass all the testcases, your code should not only produce correct results, but also run efficiently. Those who are curious can use dynamic programming. Check: https://www.geeksforgeeks.org/dynamic-programming/)
(If you do not understand the Dynamic Programming Solution, then don't worry. You can submit your bruteforce solution too. But, it should pass 4 out of 10 testcases.)
Note: Your code should not only produce correct results, but should run efficiently.
'''

'''
    Let's go to casino
    Author: Saksham Rathi
'''
import sys
# Please write your code in this file.
data = [1, 1, 2, 4, 8, 16, 32]
n = int(sys.argv[1])

def count(n: int):
    if n < 7:
        return data[n]

    while(len(data) < n+1):
        data.append(sum(data[-6:])%1000000007)
    return data[n]

print(count(n))

