import math

def factors(num, factor):
    """Returns number of times 'factor' is a factor of num."""
    i = 0
    while num % (factor ** (i+1)) == 0:
        i += 1
    return i

def factorial_trailing_zeroes(n):
    num_fives = 0
    num_twos = 0
    for i in xrange(1, n+1):
        num_fives += factors(i, 5)
        num_twos += factors(i, 2)
    return min(num_fives, num_twos)

if __name__ == '__main__':
    print '10! =', math.factorial(10)
    print 'factorial_trailing_zeroes(10) =', factorial_trailing_zeroes(10)
    print '15! =', math.factorial(15)
    print 'factorial_trailing_zeroes(15) =', factorial_trailing_zeroes(15)
    print '8! =', math.factorial(8)
    print 'factorial_trailing_zeroes(8) =', factorial_trailing_zeroes(8)
