# Enter your code here. Read input from STDIN. Print output to STDOUT
input_number = float(raw_input())
input_list = list(map(float,raw_input().split(" ")))
#mean
def findmean(input):
    a = 0
    for i in input:
        a = a+i
    mean = a/input_number
    return round(mean,1)

def findmedian(input):
    count = 0
    list = []
    count1 = 0
    a = 0
    input2 = sorted(input)
    if input_number%2 == 0:
        # print input_number%2 == 0
        for i in input2:
            #we get input_number/2 index and inputnumber/2-1 index
            count = count+1
            #print count
            #print i
            if count == int(input_number/2) or count == int((input_number/2)+1):
                #print(count == int(input_number/2) or count == int((input_number/2)+1))
                list.append(i)
        for i in list:
            count1 = count1+1
            a = a+i
        return round(a/count1,1)
                
    elif input_number%2 != 0:
         for i in input:
            #we get input_number/2 index and inputnumber/2-1 index
            count = count+1
            if count == int(((input_number+1)/2)-1):
                list.append(i)
            return list

def findmode(input):
    dict1 = {}
    for i in input:
        dict1[i] = input.count(i)
    #print dict
    sumval = sum(dict1.values())
    mean = int(sumval/input_number)
    if  max(dict1.values()) == mean:
        #print max(dict.values())
        #print mean
        return int(min(input))
    else:
        d = dict((k, v) for k, v in dict1.items() if v == max(dict1.values()))
        min1 = sorted(d)
        return int(min1[0])
        
        

print findmean(input_list)
print findmedian(input_list)    
print findmode(input_list)       