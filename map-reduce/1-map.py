

list = [ 1, 2, 3, 4, 4, 5 ]

def pow(n):
  return n**n

# with def
print map(pow, list)

# with lambda
print map(lambda n: n**n, list)