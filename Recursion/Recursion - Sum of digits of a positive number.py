def sumOfDigits(n):
    assert n >=0 and int(n) == n, 'n should be a positive integer'
    if n < 10:
        return n
    else:
        return n%10 + sumOfDigits(int(n/10))

#Example
print(sumOfDigits(2599999))
