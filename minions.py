def minion_game(string):
    kevin, stuart = [0] * 2
    n = len(string)
    vowel = ["A", "E", "I", "O", "U"]
    for i in range(n) :
        if string[i] in vowel :
            kevin += len(string) - i
        else :
            stuart += len(string) - i
    if stuart == kevin :
        print "Draw"
    elif stuart < kevin :
        print "Kevin " + str(kevin)
    else :
        print "Stuart " + str(stuart)