def pal(num):
    x1 = num[::-1]
    if x1 == num:
        print('number is palindrome')
    else:
        print('number is not a palindrome number')

a = input('enter your content: ')
print(pal(a))