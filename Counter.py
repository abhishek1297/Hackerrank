from collections import Counter
n = int(raw_input())
array = map(int, raw_input().strip().split())
k = int(raw_input())
dic = Counter(array)
total = []
for i in range(k) :
    size, amt = map(int, raw_input().split())
    if size in dic.keys() :
        total.append(amt)
        dic[size] -= 1
        if dic[size] == 0 :
            del dic[size]
print sum(total)
