# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
no_of_elem = int(raw_input())
first_line = list(map(float,raw_input().split(" ")))
sec_line = list(map(float,raw_input().split(" ")))

def weightedmean(input1,input2):
    product = [a*b for a,b in zip(input1,input2)]
    sum1 = sum(product)
    sum2 = sum(input2)
    wm = sum1/sum2
    return round(wm,1)


print weightedmean(first_line,sec_line)