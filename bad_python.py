def myfunc(a, b):
    print(a, b)


# using myfunc:

a = 1
b = a**2            # Add a value for b, b is a squared even if a changes

myfunc(a, b)        #Remove myfunc(a) and replace with myfunc(a, b)
