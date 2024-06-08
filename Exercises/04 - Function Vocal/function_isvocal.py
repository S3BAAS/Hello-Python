def is_vocal(character: str) -> str:
    
    if not isinstance(character, str):
        raise TypeError('A string is required.')
    
    if len(character) > 1:
        raise TypeError('Enter only one character.')
    
    l_char = character.lower()
    
    if l_char == 'a' or l_char == 'e' or l_char == 'i' or l_char == 'o' or l_char == 'u':
        return print(True)
    else:
        return print(False)