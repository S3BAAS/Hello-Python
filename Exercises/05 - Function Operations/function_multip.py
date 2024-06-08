def multip(*nums: tuple) -> int:
    
    if not isinstance(nums, tuple):
        raise TypeError('A tuple is required.')
    
    s = 1
    
    for i in nums:
        s *= i
    return s