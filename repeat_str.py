#!/bin/python

'''
Given an integer, n, find and print the number of letter a's in the first n letters
input :
s = aba
n = 10
output :
7
repeat the string till the length reaches n therefore abaabaabaa
'''

from collections import Counter

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    dic = Counter(s)
    if l == n :
        return dic['a']
    if l == 1 :
        if s != 'a' :
            return 0
        return n
    cnt = dic['a'] * (n / l)
    rem = n % l
    for i in range(n - rem, n) :
        if s[i % l] == 'a' :
            cnt += 1
    return cnt
    
s = raw_input()
n = int(raw_input())
result = repeatedString(s, n)
print result