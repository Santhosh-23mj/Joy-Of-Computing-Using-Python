#!/usr/bin/python3

"""
This demonstrates the dictionaries. It is denoted as follows
dict_name = {'key':value,'key':value...}
"""

print("Creating a Dictionary - dict = {}")
namelist = {}

print("\nAdding values to the dictionary - dict['key'] = value")
namelist['105'] = "n00bie"
namelist['106'] = "n00bgod"

print("\nPrinting whole dictionary - print(dict)")
print(namelist)

print("\nPrinting the keys alone - dict.keys()")
print(namelist.keys())
print("This datastructure is called 'tuple'")

print("\nConverting to list - list(dict.keys())")
print(list(namelist.keys()))

print("\nPrinting Values alone - dict.values()")
print(list(namelist.values()))

print("\nPrinting whole dictionary as tuples - dict.items()")
print(namelist.items())

print("\nAdding to dictionary - dict['key'] = value")
namelist['107'] = "no name"
print(namelist)

print("\nDeleting from dictionary - del dict['key']")
del namelist['107']
print(namelist)

"""
There are even more functions in dictionary like push(),pop(),etc..,
to reveal it use <tab> in console 
To get help about a function use function_name?
"""
