n = int(raw_input())
step = raw_input().strip()
level = 0
valley = 0
for i in range(n):
    if(step[i] == 'U') :
        level += 1
    elif step[i] == 'D' :
        if level == 0 :
            valley += 1
        level -= 1
print valley