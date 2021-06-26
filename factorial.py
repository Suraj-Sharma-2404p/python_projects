def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

x = int(input('enter your number : '))
print(factorial(x))