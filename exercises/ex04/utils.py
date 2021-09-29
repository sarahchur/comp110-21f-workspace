"""List utility functions."""

__author__ = "730228276"


def all(x: list[int], y: int) -> bool:
    """Return boolean values when comparing an integer to my list."""
    i: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if y != x[i]:
            return False
        i = i + 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    if len(x) == 0 and len(y) == 0:
        return True
    while len(x) == len(y):
        if x[i] == y[i]:
            return True
        i += 1
        return False
    return False


def max(x: list[int]) -> int:
    """Return the max number in the list."""
    i: int = 0

    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    else: 
        while i < len(x):
            if x[i] > x[i + 1]:
                return x[i]
            else:
                if x[i] < x[i + 1]:
                    return x[i + 1]
        i += 1
    return x[i]
  
  

    


    
    


    
    
    


    
    
    
    

        


        
   
            
    

    

      
