__author__ = 'Shawn'

def last_n_of_power(x,n,digits):
    result = 1
    for i in range(n):
        result = result * x
        strresult = str(result)
        if len(strresult) > digits:
            result = int(strresult[-digits:])
    return result

def addpowers(start, finish, digits):
    powers = []
    for i in range(start, finish +1):
        powers.append(last_n_of_power(i,i,digits))
    return str(sum(powers))[-digits:]

print addpowers(1,1000,10)

