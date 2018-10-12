def solve(name) :
    lst = map(lambda x : x.capitalize(), name.split())
    n = len(name)
    print n
    k = 0
    i = 0
    while i < n :
        cnt = 0
        j = i
        while name[j].isspace() :
            cnt += 1
            j += 1
        if cnt > 0 :
            lst[k] += ' ' * cnt
            i = j
            k += 1
        else :
            i += 1
    return ''.join(lst)
        