__author__ = 'Shawn'

import csv

def letter_to_number(letter):
    return ord(letter) - 64

def word_to_number(word):
    if len(word) > 1:
        return letter_to_number(word[0:1]) + word_to_number(word[1:])
    else:
        return letter_to_number(word)

def generate_triangle_numbers(n):
    a = []
    for i in range(1,n + 1):
        a.append((i*(i+1))/2)
    return a

def get_words(filename):
    f = open(filename)
    words = csv.reader(f)
    for row in words:
        wordlist = row
    return wordlist

def test():
    assert letter_to_number('A') == 1
    assert letter_to_number('Z') == 26
    assert word_to_number('SKY') == 55
    assert generate_triangle_numbers(10) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

test()
wordlist = get_words('C:\Users\Shawn\PycharmProjects\ProjectEuler\Problem 42\words.txt')
triangle_numbers = generate_triangle_numbers(1000)
print len([word for word in wordlist if word_to_number(word) in triangle_numbers])


