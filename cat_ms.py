n = int(raw_input())
for _ in range(n) :
    x, y, z = map(int, raw_input().strip().split())
    temp = abs(z - x) - abs(z - y)
    if temp > 0 :
        print "Cat B"
    elif temp < 0 :
        print "Cat A"
    else :
        print "Mouse C"