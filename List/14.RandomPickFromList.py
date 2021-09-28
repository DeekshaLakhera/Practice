import random
##choose random float between 0 and 1
print(random.random())
##choose random number within range 100
print(random.randrange(100))
##choose random even number between 0 and 100
print(random.randrange(0,100,2))
##pick from List
L=[3,5,8,9]
print(random.choice(L))
##shuffle elements of list L
random.shuffle(L)
print(L)
##choose random float (or int not sure)number within range 1,100
print(random.uniform(1,100))

