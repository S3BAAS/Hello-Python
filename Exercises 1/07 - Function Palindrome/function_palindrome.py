def is_palindrome(value: str) -> bool:
    
    if not isinstance(value, str):
        raise TypeError('A string is required.')
    
    if len(value) == 1:
        return 'More than one character is required.'
    
    lower_value = value.lower()
    
    string = lower_value[::-1]
    
    if string == lower_value:
        return True
    else:
        return False