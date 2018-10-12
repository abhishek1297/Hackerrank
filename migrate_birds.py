n = int(raw_input())
array = ''.join(raw_input().split())
dic = {}
for ele in array :
    if not (ele in dic.keys()) :
        dic[ele] = array.count(ele)
mx = max(dic.values())
types = []
for key, value in dic.iteritems() :
    if value == mx :
        types.append(key)
types = sorted(map(int, types))
print types[0]
    