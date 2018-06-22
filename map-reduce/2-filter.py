

l = [ 1, 2, 3, 4, 4, 5 ]

def divisible_by_2(n):
  return (n % 2) == 0 

# with def
print filter(divisible_by_2, l)

# with lambda
print filter(lambda n: (n % 2) == 0, l)