

# a simple value
print [ x**2 for x in range(10) ]


#  a tuple

print [ (x, y) for x in range(1,11) for y in range(1,6) ]


# filtering (2 divisible)
print [ x for x in range(10) if x % 2 == 0 ]
