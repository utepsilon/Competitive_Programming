n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
c = [int(x) for x in input().split()]
b = []
for i in range(len(a)):
    b.append([])
    for j in range(len(c)):
        b[i].append(c[j]-a[i])
k = set()
if len(b)>1:
    p = set(b[0])
    q = set(b[1])
    k = p.intersection(q)

for i in range(2,len(b)):
    l = set(b[i])
    k = k.intersection(l)
if len(b)==1:
    k = set(b[0])
for i in sorted(k) :
    print(i,end=" ")
    

"""
In this problem, we define "set" is a collection of distinct numbers. For two sets  and , we define their sum set is a set . In other word,  set  contains all elements which can be represented as sum of an element in  and an element in . Given two sets , your task is to find set  of positive integers less than or equals  with maximum size such that . It is guaranteed that there is unique such set.

Input Format

The first line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .

The third line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .

Output Format

Print all elements of  in increasing order in a single line, separated by space.

Constraints

 

SAMPLE INPUT 
2
1 2
3
3 4 5

SAMPLE OUTPUT 
2 3
Explanation
If  is an element of set , then  is an element of set , so we must have . Clearly,  cannot be  because  is not an element of set . Therefore, .
"""