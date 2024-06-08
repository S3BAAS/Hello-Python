def max_(num1: int, num2: int) -> int:
    
    if not isinstance(num1, int):
        raise TypeError('An integer is required.')
    
    if not isinstance(num2, int):
        raise TypeError('An integer is required.')
    
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)