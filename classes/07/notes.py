"""
for loop - a count controlled loop
repeat a block of code for every element in a sequence of elements
* characters in a string
* items in a list
* numbers in a arithmetic range

1. start w/ key word for
2. followed by some variable name (your choice!)
3. in (key word)
4. your sequence (iterable object)

you can use range to create a "range object"
a range object represents an arithmetic sequence
you can call range function (which creates a range object) 3 ways:
* 1 arg = range(n)... starts at 0, goes up to, but not including n, steps by 1
* 2 arg = range(n, m)... starts at n, goes up to, but not including m, steps by 1
* 3 arg = range(n, m, step)... starts at n, goes up to, but not including m, steps by step

"""

""" 1, 2, 3, 4, 5"""
""" \/---- represents the current element being examined in the while loop"""
for number in range(1, 6):
    print(number)








