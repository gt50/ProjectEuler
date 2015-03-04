__author__ = 'sjackson'

def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def is_bpalindrome(number):
    number = number[2:]
    return number == number[::-1]

def test():
    assert is_palindrome(989) == True
    assert is_palindrome(123) == False
    assert is_bpalindrome('0b1001') == True
    assert is_bpalindrome('0b1010') == False
    print "Tests Passed!"

def find_palindromes(max):
    palindromes = []
    for i in range(max):
        if is_palindrome(i) and is_bpalindrome(bin(i)):
            palindromes.append(i)
    print palindromes
    print sum(palindromes)

test()
find_palindromes(1000000)