# Time: O(n)
# Space: O(n)
def reverse(string):
    return ''.join([string[i] for i in range(len(string)-1, -1, -1)])
