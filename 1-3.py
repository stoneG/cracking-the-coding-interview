# Time: O(n^2)
# Space: O(1)
def is_permutation(str1, str2):
    if len(str1) == len(str2):
        for char in str1:
            if char in str2:
                str2.replace(char, '', 1)
        if len(str1) == len(str2) == 0:
            return True
