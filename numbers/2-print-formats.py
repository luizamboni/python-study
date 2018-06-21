

# simplest
print("{} and {}".format(1, 2))


# ordered
print("{1} and {0}".format(1, 2))


# padding left
print("{:>10}".format(1))

# padding right (not work)
print("{:10d}".format(1))


# decimal
print("{} {:d}".format("decimal:", 1))
print('{} {:03d}'.format("decimal:",1))

# float
print("{} {:f}".format("float:",1))

print('{} {:03.2f}'.format("float:",1))
