

'''
GCD algorithm
'''
def gcd(a, b):
    #Using Euler's formula
    remainder = a%b
 #   x = a/b            may not need to divide at all
    while remainder!=0:
        a = b          #46, 31, 15
        b = remainder   #31, 15, 1
 #       x = a/b     
        remainder = a%b     #15, 1, 0 
        
    return b

'''
Rectangles on a rubik's cube
'''
def rubiks(n):
    #formula is: 6*sum(n)^2
    try:
        if(n<1):
            print("The input needs to be greater than 0!")
        else:
            return 6*sum(range(n+1))*sum(range(n+1))
    except TypeError:
        print("The input is not an integer!")

'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    while(n!=0):
        if is_this_it(n) == True:
            return n
        n=n-1
    return -1
        
'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
    guessing = 1
    while(is_this_smaller(guessing) == True):
        #print("checking number: " + str(guessing))
        guessing = guessing + 2
    #print("FIRST FAILURE: " + str(guessing))
    if (is_this_smaller(guessing - 1) == True):
        #print("checking number: " + str(guessing-1))
        return guessing
    else:
        #print("SECOND FAILURE: " + str(guessing-1))
        return guessing - 1


        

'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
    upper_bound = n
    lower_bound = 1
    while (lower_bound < upper_bound):    
        checking = (upper_bound + lower_bound)/2
        #print("upper bound: " + str(upper_bound) + "       lower bound: " + str(lower_bound))
        if(is_this_smaller(checking) == False): #number's smaller than middle number
            upper_bound = checking
        else:    #number's bigger than middle number
            lower_bound = checking + 1
    return upper_bound

