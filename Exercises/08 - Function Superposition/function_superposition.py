def superposition(value1: list, value2: list) -> bool:
    
    if not isinstance(value1, list):
        raise TypeError('A list is required.')
    
    if not isinstance(value2, list):
        raise TypeError('A list is required.')
    
    for i in value1:
        for c in value2:
            if c == i:
                return True
            else:
                continue
    return False

print(superposition(['Hola', 'Que', 'Tal'], 'Hola'))