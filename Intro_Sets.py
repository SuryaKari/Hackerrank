def average(array):
    # your code goes here
    #print array
    sum = 0
    set_array = list(set(array))
    count = 0
    for i in set_array:
        sum = sum+i
        count = count+1
    return sum/count
    