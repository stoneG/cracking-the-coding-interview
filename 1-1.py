# Time: O(n)
# Space: O(n)
def all_unique(string):
    character = {}
    for char in string:
        if character.get(char):
            return False
    return True

# Time: O(n^2)
# Space: O(1)
def all_unique2(string):
    for i, char in enumerate(string):
        for other_char in string[i+1:]:
            if char == other_char:
                return False
    return True
