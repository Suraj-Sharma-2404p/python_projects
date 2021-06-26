def fibonacci(num):
    a=0
    b=1
    if num<0:
        print('incorrect value')
    elif num==0:
        return 0
    elif num==1:
        return b
    else:
        for i in range(1,num):
            c=a+b
            a=b
            b=c
        return b
print(fibonacci(10))