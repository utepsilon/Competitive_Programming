t = int(input())
while(t>0):
    t= t-1;
    s = input()
    arr = [int(x) for x in input().split()]

    set1 = set(list(s))
    
    tl =len(s)
    tw = sum([arr[ord(x)-97] for x in set1])
    sp = 0


    for i in set1:
        c = s.count(i)
        sp = sp+ c*(arr[ord(i)-97])
    spa = (10*sp)/(tl*tw)
    print('{:.2f}'.format(round(spa,2)))
"""
        
PROBLEM STATEMENTPoints: 30
Milly is a very cool algorithmist. She likes to make new algorithms to solve real world scenarios. This time she is playing with strings and she is trying to produce some new concept out of it. She has developed a new concept of SPA which stands for STRING POINT AVERAGE. This concept is described below :

Suppose we have a string S, Then :

enter image description here

Here ,
             C[ch]: Count of a character ch in S,
             W[ch]: Weight of the character ch,
              TL:   Total length of S and
              TW:   Total Weight of unique characters of S
Input
First line of the input will contain a integer T (number of test cases).
Then for every test case there will be two lines, First one will have the string S and the other one will have 26 space separated integers denoting W[ch].
Output
For every test case, print the required SPA and Your answer will be considered as correct if it has an absolute error less than 10-2.
Constraints
1 ≤ T ≤ 10
1 ≤ W[ch] ≤ 100
1 ≤ TL ≤ 105
ch ∈ {a, b, c ... ,z}
SAMPLE INPUT 
1
aab
20 50 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
SAMPLE OUTPUT 
4.29
Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Score is assigned if any testcase passes.
Allowed Languages: Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
Activity
"""