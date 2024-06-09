def procedure(*num: tuple) -> str:
    
    ast = '*'
    
    if not isinstance(num, tuple):
        raise TypeError('A tuple is required.')
    
    for i in num:
        if not isinstance(i, int):
            raise TypeError('A int is required.')
        
        if i == num[-1]:
            return f'{ast * i}\n'
        else:
            print(f'{ast * i}\n')