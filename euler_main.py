"""Problem from: https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""


def take_decimal_string(dec_string):
    dec_string_length = len(dec_string)
    i = 0
    result = 1
    power_of_ten = [1 + 10**x for x in range(7)]
    while i < dec_string_length:
        if i not in power_of_ten:
            i += 1
            continue

        value = int(dec_string[i]) 
        result = result * value
        i += 1

    return result
