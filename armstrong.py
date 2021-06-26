#  armstrong number : sum f the cube of all its digits is equal to the same number
num = int(input('enter a number : '))
sum = 0
temp = num

while temp >0:
    c = temp % 10
    sum += c**3
    temp //= 10

if num == sum:
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')

