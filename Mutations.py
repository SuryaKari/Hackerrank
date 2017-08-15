def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    b = "".join(a)
    return b