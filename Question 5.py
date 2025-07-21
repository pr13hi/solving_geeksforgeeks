# Question : The FizzBuzz Program
#            You are given a number  and you have to print your answer according to the following:
#            If the number is divisible by 3, you print "Fizz" (without quotes)
#            If the number is divisible by 5, you print "Buzz" (without quotes)
#            If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
#            In any other case, you print the number itself

#            Note: You should add a newline character after print() statement.

# Solution :

def fizzBuzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
        
