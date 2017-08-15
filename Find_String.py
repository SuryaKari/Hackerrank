import re
def count_substring(string, sub_string):
    length = len(string)
    sub_length = len(sub_string)
    count = 0
    for i in range(0,length):
        if string[0:sub_length] == sub_string:
            count = count+1
            string = string[1:]
            #print string
        elif string[0:sub_length] != sub_string:
            count = count
            string = string[1:]
            #print string  
    return count