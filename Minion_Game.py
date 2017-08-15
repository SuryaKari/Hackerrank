def minion_game(string):
    # your code goes here
        s = string

        vowels = 'AEIOU'

        kevsc = 0
        stusc = 0
        for i in range(len(s)):
            #print i
            if s[i] in vowels:
                #print s[i]
                kevsc += (len(s)-i)
                #print 'kevin :', kevsc
            else:
                #print s[i]
                stusc += (len(s)-i)
                #print 'stuart :', stusc

        if kevsc > stusc:
            print "Kevin", kevsc
        elif kevsc < stusc:
            print "Stuart", stusc
        else:
            print "Draw"