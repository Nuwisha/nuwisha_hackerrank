link = "https://www.hackerrank.com/challenges/python-lists"

# ---=== SOLUTION ===---
number_of_operations = int(input().strip())
no_args_cmds = {'sort':list.sort, 'pop':list.pop, 'reverse':list.reverse}
single_args_cmds = {'remove':list.remove,'append':list.append}
double_args_cmds = {'insert':list.insert}
L = []
for i in range(number_of_operations):
    data = input().split()
    if data[0] == 'print':
        print(L)
    elif data[0] in no_args_cmds.keys():
        no_args_cmds[data[0]](L)
    elif data[0] in single_args_cmds.keys():
        single_args_cmds[data[0]](L,int(data[1]))
    elif data[0] in double_args_cmds.keys():
        double_args_cmds[data[0]](L,int(data[1]), int(data[2]))

# ---=== TASK ===---
task = """
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
