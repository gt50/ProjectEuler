__author__ = 'Shawn'
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
"""

def find_fractions():
    productn = 1
    productd = 1
    for numerator in range(10,100):
        for denominator in range (10,100):
            x = int(str(numerator)[0:1])
            y = int(str(denominator)[1:])
            if y == 0 or numerator == denominator:
                continue
            if str(numerator)[1:] == str(denominator)[0:1]:
                if (x/float(y)) == (numerator/float(denominator)):
                    print numerator, denominator
                    productn = productn * numerator
                    productd = productd * denominator
    print productn, productd


find_fractions()