def all_unique(string):
    for i, char in enumerate(string):
        for j in range(len(string)):
            if i != j and char == string[j]:
                return False
    return True
