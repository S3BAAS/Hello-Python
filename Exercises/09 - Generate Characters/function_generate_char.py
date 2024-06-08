def generate_char(num: int, value: str) -> str:
    
    if not isinstance(value, str):
        raise TypeError('A string is required.')
    
    if not isinstance(num, int):
        raise TypeError('A integer is required.')
    
    if num <= 1:
        return 'The integer must be greater than 1.'
    
    return value * num    
    