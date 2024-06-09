def longest_word(_list: list) -> str:
    
    if not isinstance(_list, list):
        raise TypeError('A list is required.')
    
    long_word = _list[0]
    
    for word in _list:
        if len(word) >= len(long_word):
            long_word = word
            
    return long_word