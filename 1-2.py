# Time: O(n)
# Space: O(1)
def reverse(string):
    return ''.join([string[i] for i in range(len(string)-1, -1, -1)])

# More Pythonic, and includes the null-termination
# Time: O(n)
# Space: O(1)
def reverse(string):
    return string[-2::-1] + '\0'
