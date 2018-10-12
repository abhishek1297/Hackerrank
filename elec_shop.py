import itertools
b, n, m = map(int, raw_input().strip().split())
key = map(int, raw_input().strip().split())
usb = map(int, raw_input().strip().split())
arr = itertools.product(key, usb)
sm = sorted(map(lambda x : sum(x), arr))
flag = True
for i in sm[::-1] :
    if i <= b :
        print i
        flag = False
        break
if flag :
    print "-1"

