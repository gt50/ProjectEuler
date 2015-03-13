__author__ = 'Shawn'

def long_division_repeat_length(n,d):
    remainders = []
    answer = ''
    numerator = str(n)
    found_decimal = False
    endofnumerator = False
    tempnumerator = 0
    for i in range(len(numerator) + d + 1): #repeating digits are at most of length equal to the denominator
        nextdigit = numerator[0 + i: 1 + i]
        if nextdigit == '' or nextdigit == '.':
            if nextdigit == '':
                endofnumerator = True
            if not found_decimal:
                answer += '.'
                found_decimal = True
                continue
            nextdigit = 0
        tempnumerator = int(str(tempnumerator) + str(nextdigit))
        answer += str(tempnumerator / d)
        tempnumerator = tempnumerator % d
        if endofnumerator:
            if tempnumerator in remainders:
                print n, d, len(remainders), remainders
                return len(remainders)
            else:
                remainders.append(tempnumerator)
        if tempnumerator == 0:
            return 0

def test():
    assert long_division_repeat_length(1,2) == 0
    assert long_division_repeat_length(1,3) == 1
    assert long_division_repeat_length(1,7) == 6

def find_longest():
    longest = (0,0)
    for i in range(1,100):
        length = long_division_repeat_length(1,i)
        if length > longest[1]:
            longest = (i,length)
    return longest

test()
print find_longest()

# The code answers 982 instead of 983 as longest. Every reasonable test seems accurate.