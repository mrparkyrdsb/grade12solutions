# Create a fibonacci sequence using a dictionary
'''
dict = {
    key : value,
    key2 : other_value
}
'''
fibs = {
    0: 0,
    1: 1
}

def fib(upper_limit, fib_dict):
    for address in range(2, upper_limit):
        fib_dict[address] = fib_dict[address-1] + fib_dict[address-2]
    return list(fib_dict.values())

print(fib(20, fibs))
