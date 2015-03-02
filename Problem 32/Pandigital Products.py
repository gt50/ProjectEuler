__author__ = 'Shawn'


def ispandigital(number):
    #return sorted(map(int, str(number))) == list(set(map(int, str(number))))
    return sorted(number) == list(set(number))

def getproducts(max):
    for i in range(max):
        for j in range(max):
            if ispandigital(map(int, str(i)) + map(int, str(j)) + map(int, str(i*j))): print i, j, i*j

def test():
    assert ispandigital(15234) == True
    assert ispandigital(7254) == True
    assert ispandigital(1111) == False
    print "Tests Passed!"


test()
getproducts(10000)