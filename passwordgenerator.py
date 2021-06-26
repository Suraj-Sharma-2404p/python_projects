import random
print('Password Generator:: A tool to generate your passwords!!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,?'

number = input('amount of passwords to generate : ')
number = int(number)

length = input('Input Your password length: ')
length = int(length)

print('\n here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)


print(passwords)
