# 001010
# 001001

def bit_max(x, y):
    msb = get_msb(x^y)
    if x & (2 ** (msb - 1)):
        return x
    return y

def get_msb(num):
    counter = 0
    while num:
        num >>= 1
        counter += 1
    return counter

if __name__ == '__main__':
    print 'bit_max(10,20):', bit_max(10,20)
    print 'bit_max(20,5):', bit_max(20,5)
    print 'bit_max(29472,224719):', bit_max(29472,224719)
