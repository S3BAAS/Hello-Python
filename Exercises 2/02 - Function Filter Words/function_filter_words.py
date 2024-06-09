def filter_words(_list: list, num: int) -> list:
    
    if not isinstance(_list, list):
        raise TypeError('A list is required.')
    
    if not isinstance(num, int):
        raise TypeError('An integer is required.')
        
    f_words = []
    
    for value in _list:
        if len(value) > num:
            f_words.append(value)
    
    if len(f_words) == 0:
        return None
    
    return f_words