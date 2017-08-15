# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
num_elements = int(raw_input())
first_line = list(map(float,raw_input().split(" ")))

# Step 1 : Find the mean 
def findmean(input):
    a = 0
    for i in input:
        a = a+i
    mean = a/num_elements
    return round(mean,1)

# Step 2 : Find the Squared diff from the mean
def findsqdiff(input):
    list_diff = []
    mean1 = findmean(input)
    for i in input:
        list_diff.append(abs(i-mean1)**2)
    return list_diff


# Step 3 : Find the Standard Deviation

def findstdev(input):
    list_diff = sum(findsqdiff(input))
    std_dev = math.sqrt(list_diff/num_elements)
    return round(std_dev,1)

print findstdev(first_line)