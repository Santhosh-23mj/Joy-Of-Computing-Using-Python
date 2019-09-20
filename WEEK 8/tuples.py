#!/usr/bin/python3

"""
This program tell about python datastructure - 'Tuple'
Tuples are immutable and they are iterable
most functions that work with lists also work with 
tuples
"""

# declaring a tuple
flavours = ("vanilla","chocolate","strawberry","butterscotch")

# printing a tuple
print(flavours)

# using a loop
print("Using a loop")
for taste in flavours:
    print(taste)

# using index
print("Using the index")
for i in range(4):
    print(flavours[i])

print("Printing length of tuple : ",len(flavours))
print("Counting occurence : ",flavours.count('chocolate'))
print("Printing the index of an element : ",flavours.index('chocolate'))
print("\nWe cant insert values to tuple after it is initialized")
print("tuple[i] = 'value wont work'")
print("\nWe cant delete a single element from a tuple")
print("del tuple[i] wont work")
print("\nWe can only delete tuple as a whole")
print("del tuple - deletes it as a whole")
del flavours

print("\nTuples can be mainly used in image processing where the pixel values")
print("of an image remains constant")
