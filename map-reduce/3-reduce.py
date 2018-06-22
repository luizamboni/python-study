
l = [ 1, 2, 3, 4, 4, 5 ]


# with lambda
print reduce(lambda state, current: state + current, l)