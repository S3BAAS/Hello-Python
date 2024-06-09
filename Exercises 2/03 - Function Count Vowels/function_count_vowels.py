def count_vowels(word: str) -> dict:
    
    if not isinstance(word, str):
        raise TypeError('A string is required.')
    
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    l_word = word.lower()
    
    for value in l_word:
        match value:
            case 'a':
                a += 1
            case 'e':
                e += 1
            case 'i':
                i += 1
            case 'o':
                o += 1
            case 'u':
                u += 1
            case _:
                continue
            
    d_word = {
        'A': a,
        'E': e,
        'I': i,
        'O': o,
        'U': u
    }
    
    return d_word