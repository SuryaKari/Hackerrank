def swap_case(s):
    a = s.split(" ")
    #print a
    letters = []
    letters2 = "-".join(a)
    letters3 = letters2.split()
    for idx,i in enumerate(letters3):
        
        for j in i:
            if j.isupper():
                j = j.lower()
            elif j.islower():
                j = j.upper() 
            letters.append(j)
        almost = "".join(letters)
        return almost.replace("-"," ")