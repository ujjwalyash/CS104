'''
    Tower of Hanoi
    Author: Abhi Jain
'''

'''
Write your code to solve tower of hanoi problem here
Take input from user for number of disks

Output format:
line 1: number of moves(N)
line 2: move1
line 3: move2
...
line N+1: moveN
'''

'''
To solve this problem, you can use the recursive approach.
'''

import argparse
n = argparse.ArgumentParser()
n.add_argument("n", type=int)
args = n.parse_args()
n = args.n

def steps(n: int):
    return 2**n - 1

def solveHanoi(n: int, start: int, end: int, buffer: int):
    if n > 1:
        solveHanoi(n-1, start, buffer, end)
        print(f'{start} {end}')
        solveHanoi(n-1, buffer, end, start)
    else:
        print(f'{start} {end}')

    return None

print(steps(n))
solveHanoi(n, 1, 3, 2)
