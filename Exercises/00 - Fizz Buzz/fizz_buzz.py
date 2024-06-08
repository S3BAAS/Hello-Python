for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 != 0:
        print(f'{i}: Fizz')
        
    elif i % 5 == 0 and i % 3 != 0:
        print(f'{i}: Buzz')
        
    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i}: Fizz Buzz')
    