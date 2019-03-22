def sum_array(array):
    '''Return sum of all items in an array'''
    return sum(i for i in array)

def fibonacci(n):
    '''Return nth term in th fibonacci sequence'''
    #check if n is less than or equals to 1
    if n<=1:
        return n
    else:
        #apply the recursion by calling the function itself
        return (fibonacci(n-1)+fibonacci(n-2))

def factorial(n):
    '''Return n!'''
    #initialise all to 1 since factorial of 0 is 1 and 0 multiplied by any number is equal to zero
    fact = 1
    k = 1
    if n <=1:
        return 1
    elif n> 1:
        #while loop to loop through all the numbers needed
        while k != (n+1):
            fact = fact * k
            k = k+1
    return fact

def reverse(word):
    '''Return word in reverse'''
    message = ""
    for k in word:
        message = k + message
    return message
