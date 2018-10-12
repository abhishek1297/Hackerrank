n = int(raw_input())
array = map(int, raw_input().rstrip().split())
day, m = map(int, raw_input().rstrip().split())
cnt = 0
for i in range(n) :
    if(sum(array[i:i+m]) == day) :
        cnt += 1
print cnt