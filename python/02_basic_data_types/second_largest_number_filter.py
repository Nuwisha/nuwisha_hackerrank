link = "https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list"

# ---=== SOLUTION ===---
total = int(input().strip())
L = list(map(int, input().split()))
L = list(filter(lambda x : x != max(L),L))
print(max(L))

# ---=== TASK ===---
task = """
You are given  numbers. Store them in a list and find the second largest number.

Input Format 
The first line contains . The second line contains an array [] of  integers each separated by a space.

Constraints 
 

Output Format 
Output the value of the second largest number.

Sample Input

5
2 3 6 6 5
Sample Output

5
"""
