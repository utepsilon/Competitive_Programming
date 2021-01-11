t = int(input())
for __ in range(t):
    n,A,B = map(int,input().split())
    li = []
    if A>B:
        if n%2==0:
            j = n//2
        else:
            j = n//2  +1
        temp = j
        j = 0
        for i in range(temp+1):
            li.append(A*(i)**2+B*(n-j)**2)
            j +=1
        print(min(li))
        #print(li)
    else:
        if n%2==0:
            j = n//2
        else:
            j = (n//2 )+1
        temp = j
        #print(temp)
    
        for i in range(temp,n+1):
            li.append(A*(i)**2+B*(n-j)**2)
            j +=1
        #print(li)
        print(min(li))

        


        
    
    

    
    
      


"""Creatnx now wants to decorate his house by flower pots. He plans to buy exactly  ones. He can only buy them from Triracle's shop. There are only two kind of flower pots available in that shop. The shop is very strange. If you buy  flower pots of kind 1 then you must pay  and  if you buy  flower pots of kind 2. Please help Creatnx buys exactly  flower pots that minimizes money he pays.

Input Format

The first line contains a integer  denoting the number of test cases.

Each of test case is described in a single line containing three space-separated integers .

Output Format

For each test case, print a single line containing the answer.

Constraints

 

SAMPLE INPUT 
2
5 1 2
10 2 4

SAMPLE OUTPUT 
17
134
Explanation
Query 1: we have to buy exactly  pots. There are six possible options:

Buy  pot of first kind,  pots of second kind. The cost is: .
Buy  pot of first kind,  pots of second kind. The cost is: .
Buy  pots of first kind,  pots of second kind. The cost is: .
Buy  pots of first kind,  pots of second kind. The cost is: .
Buy  pots of first kind,  pot of second kind. The cost is: .
Buy  pots of first kind,  pot of second kind. The cost is: .
"""