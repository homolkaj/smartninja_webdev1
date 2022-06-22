# Homework 12.4 - 12.4: Absolute difference between two numbers
#
# The inputs in this function are two real numbers.
# The result is an absolute difference between the numbers.
# (Hint: this means the result cannot be a negative number.)

def diff(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1

print(diff(6, 3))
print(diff(3, 6))