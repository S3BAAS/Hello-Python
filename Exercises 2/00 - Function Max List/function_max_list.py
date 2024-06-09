def max_list(_list: list) -> int:
    
    if not isinstance(_list, list):
        raise TypeError('A list is required.')
    
    max_value = _list[0]
    
    for value in _list:
        if value > max_value:
            max_value = value
        
    return max_value