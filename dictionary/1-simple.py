

user = {
  'name': "luiz",
  'email': "luiz@example.com"
}

print user

# alter
user['name'] = "luiz zamboni"
print user


# delete field
del user['name']
print user

# add field
user['name'] = 'again'
print user