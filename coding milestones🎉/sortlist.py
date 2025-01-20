#Define the function myfunc that takes a number n as input
def myfunc(n):
    # Return the absolute difference between n and 50
    return abs(n - 50)

#Define the list of numbers
thislist = [100, 50, 65, 82, 23]

#Sort the list using the myfunc function to determine the order based on the absolute difference from 50 e.g 100-50=50, 50-50=0, 65-50= 15, 82-50=32, 23-50=27. sorting it based on which has an absolute difference closest to 50, itll be 0, 15, 27, 32, 50 and rearranging based on this, we'll have: 50, 65, 23, 82, 100
thislist.sort(key = myfunc)

#Print the sorted list
print(thislist)

