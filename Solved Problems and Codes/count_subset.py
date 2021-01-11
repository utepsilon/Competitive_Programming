from itertools import combinations
for __ in range(int(input())):
    n,k,q = map(int,input().split())
    st = input()
    dic = {}
    for j in range(q):
        l,r = map(int,input().split())
        test_str = st[l-1:r]
        #arr = []
        flag = [0]
        res = []
        st1 = str(l)+','+str(r)
        if st1 in dic.keys():
            print(dic[st1])
            continue
        
        ans = (len(test_str)*(len(test_str)+1))//2
        for i in range(len(test_str)):
            if flag.count(0)>=1:
                res =[test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2) if len(test_str[x:y]) == len(test_str)-i]
            else:
                break
            flag = []
            for x in res:
                if x.count('1')<=k and x.count('0')<=k:
                    flag.append(1)
                else:
                    ans -= 1 
                    flag.append(0)
        
        dic[st1]=ans
        print(ans)
        
            