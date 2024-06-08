def max_three(num1: int, num2: int, num3: int) -> int:
    
    if not isinstance(num1, int):
        raise TypeError('An integer is required.')
    
    if not isinstance(num2, int):
        raise TypeError('An integer is required.')
    
    if not isinstance(num3, int):
        raise TypeError('An integer is required.')
    
    
    if num1 > num2 and num1 > num3:
        print(num1)
        
    elif num2 > num1 and num2 > num3:
        print(num2)
        
    elif num3 > num1 and num3 > num2:
        print(num3)
        
max_three(1, 1, 3)