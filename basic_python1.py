i = 5
j = 4.
print(i, type(i))
print(j, type(j))

k = 'ciao tutti'
print(k, type(k))

l = [1, 3., 'va bene']
print(l, type(l))

m = (45.67, 2, 'this cannot be changed')
print(m, type(m))

n = {'lunedi': 1, 'martedi': 2, 'mercoledi': 3, 'giovedi': 4, 'vernedi': 5}
print(n, type(n))

#Types of printing in Python
name = 'Ana Pascual Aranda'
age = 22

#The ugly way:
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')

#The old way:
print('My name is %s and I am %d years old.' % (name, age))

#The new way:
print('My name is {} and I am {} years old.'.format(name, age))

#The pythonic way:
print(f'My name is {name} and I am {age} years old.')
