"""
* what's the exam, topics, etc.

1.
-----
* sorting ... like sorting strings (without sort method)
* repeated application of list methods
    * list methods
* a quick overview of functions again


* 19 x lists of lists
* 19 x make up questions on the spot
* 19 x recursion

* 16 x nested loops
* 13 x assertions
* 0 x review slides?


* most likely going to have a list of methods on the exam
"""
"""
bubble sort
7, 3, 2
3, 7, 2
3, 2, 7

do this until there are no more swaps:
    go over *position*
    check adjacent, 
        if current is greater, then swap
"""
"""
def sort_stuff(numbers):
    swaps = 1
    while swaps > 0:
        # reset the number of swaps

        swaps = 0
        # generate all of the possible indexes
        for i in range(len(numbers)):
            if i < len(numbers) - 1 and numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1
    
#      0, 1, 2
nums = [7, 3, 2]
sort_stuff(nums)
print(nums)
"""
"""
add a new element to a list
----
* append # <-- parameter: value that you want to add, return: None
* extend # <-- return: None
* insert # <-- return: None

get rid of an element
----
* remove # <-- return: None
* pop # <-- return: the last element (and removes it from the list)
* del (not a method)

misc
----
* sort # <-- return: None
* count # <-- return: number of occurences of element
* index # <-- return: gives back index of first occurence of value
numbers = [1, 2, 3]
result1 = numbers.append(4) # [1, 2, 3, 4] ... None
numbers.extend([5, 6]) # [1, 2, 3, 4, 5, 6]
result2 = numbers.pop() # [1, 2, 3, 4, 5] ... 6
result3 = numbers.append([7, 8]) # [1, 2, 3, 4, 5, [7, 8]]

print(numbers)
print(result1)
print(result2)
print(result3)
"""
"""
(100, 0) [100, 0] -> x, y
(100, 100)
(0, 100)
(0, 0)
give me all the points where the sum of the x and y component within each point is < 200 as a list

move all of the x values 50 pixels (add 50 to x for every point)

actually use turtle + goto to draw a picture
"""
"""
points = [[100, 0], [100, 100], [0, 100], [0, 0]]

def f(my_list):
    new_list = []
    for point in my_list:
        if point[0] + point[1] < 200:
            new_list.append(point)
    return new_list

def f(my_list):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i][0] + my_list[i][1] < 200:
            new_list.append(my_list[i])
    return new_list

for point in points:
    point[0] += 50

print(points)
"""
def generate_deck():
    # returns [['clubs', '2'], ['hearts', 'J']]
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # go through every suit
       # go through every possible value
          # combine both into a list
          # add to the deck
    deck = []
    for s in suits:
        for v in values:
            deck.append([s, v])
    return deck

deck = generate_deck()
print(deck)

import random
def shuffle(deck):
    for i in range(100):
        start_i= 0
        end_i= len(deck) - 1
        i1 = random.randint(start_i, end_i)
        i2 = random.randint(start_i, end_i)
        deck[i1], deck[i2] = deck[i2], deck[i1]

shuffle(deck)
print(deck)

















