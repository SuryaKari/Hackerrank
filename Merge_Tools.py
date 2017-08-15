from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    #print length
    #num_breaks = k
    breaks = []
    #print length/num_breaks
    j = 0
    for i in range(k,len(string)+1,k):
        #print i
        breaks.append([string[j:i]])
        j = i
        
    for i in breaks:
        for j in i:
            #print j
            a = ''.join(sorted(set(j), key=j.index))
        print a
            