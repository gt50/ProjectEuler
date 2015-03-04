__author__ = 'sjackson'
#>>> [number[i:] for i in range(len(number))]
#['3797', '797', '97', '7']
#>>> [number[:i:] for i in range(1,len(number)+1)]
#['3', '37', '379', '3797']
import math
def is_prime(number):
    s = int(math.sqrt(number) + 1)
    if number < 2:
        return False
    for i in range(2, s):
        if number % i == 0:
            return False
    return True

def is_prime_list(numbers):
    numbers = map(int,numbers)
    return True if set(map(is_prime,numbers)) == set([True]) else False

def find_primes(max):
    primes = []
    for i in range(8,max):
        if is_prime(i):
            k = str(i)
`           truncate_left = [i[j:] for j in range(len(k))]
            truncate_right = [i[:j:] for j in range(1,len(k)+1)]
            if is_prime(truncate_left) and is_prime(truncate_right):
                primes.append(i)
                if len(primes) >=11:
                    return primes
    return primes

def test():
    assert is_prime_list(['3', '37', '379', '3797']) == True
    assert is_prime_list(['10']) == False
    print "Tests Passed!"

test()
print find_primes(1000)