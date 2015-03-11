__author__ = 'Shawn'


def fill_integers(maxdigits):
    i = 0
    a = ''
    while len(a) < maxdigits + 1:
        a = a + str(i)
        i += 1
    return a

a = fill_integers(1000000)
print int(a[1]) * int(a[10]) * int(a[100]) * int(a[1000]) * int(a[10000]) * int(a[100000]) * int(a[1000000])