"""List utility functions."""

__author__ = "730228276"


def all(x: list[int], y: int) -> bool:
    """Return boolean values when comparing an integer to my list."""
    i: int = 0
    while i < len(x):
        if y == x[i]:
            return True
        i = i + 1
    return False


def is_equal(x: list[int], y: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    while len(x) == len(y):
        if x[i] == y[i]:
            i += 1
        return True
    return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    


    
    
    
    

        


        
   
            
    

    

      
