#!/usr/bin/python3
# my_calculating-program.py

a = 10
b = 5

from calculator_1 import add, sub, mul, div

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result_add))
print("{:d} - {:d} = {:d}".format(a, b, result_sub))
print("{:d} * {:d} = {:d}".format(a, b, result_mul))
print("{:d} / {:d} = {:d}".format(a, b, result_div))
