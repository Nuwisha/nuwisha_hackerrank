#!/bin/python3

import sys

N = int(input().strip())

if N%2 != 0:
    print('Weird')
elif N >= 2 and N <= 5:
    print('Not Weird')
elif N >= 6 and N <= 20:
    print('Weird')
elif N > 20:
    print('Not Weird')

    
task = """
Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
Explanation

Sample Case 0:  
 is odd and odd numbers are weird, so we print Weird.

Sample Case 1:  
 and  is even, so it isn't weird. Thus, we print Not Weird.
"""

link = "https://www.hackerrank.com/challenges/py-if-else"