import itertools
st, n = raw_input().split()
arr = itertools.permutations(st, int(n))
arr = sorted(arr)
for ele in arr :
    print ''.join(ele)
