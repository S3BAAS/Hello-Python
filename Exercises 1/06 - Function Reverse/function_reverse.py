def reverse(value: str) -> str:
    
    if not isinstance(value, str):
        raise TypeError('A string is required.')
    
    if len(value) == 1:
        return 'More than one character is required.'
    
    return value[::-1]