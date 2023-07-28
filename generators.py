import itertools

#we define the generator, this is computed only when called (yield)
squares = (x**2 for x in itertools.count(1))

print(f'Generator type: {type(squares)}')

#we execute the generator
for x in squares:
    print(x)
    if x>500:
        #we close the generator
        squares.close()
        

'''
#Another method without generator comprension:

def squares2():
    for x in itertools.count(1):
        yield x**2

for x in squares2():
    print(x)
    if x>500:
        break
'''
