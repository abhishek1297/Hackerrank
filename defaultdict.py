from collections import defaultdict

d = defaultdict(list)
n,m=map(int,raw_input().strip().split(' '))
for i in xrange(1,n+1):
    s=raw_input().strip()
    d[s].append(i)
for i in xrange(m):
    s=raw_input().strip()
    print " ".join(map(str,d[s])) if d[s]!=[]  else "-1"