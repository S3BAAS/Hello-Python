def length(value: str) -> int:
    
    if not isinstance(value, str):
        raise TypeError('A string is required.')
    
    n = 0
    
    for _i in value:
        n += 1
    return n