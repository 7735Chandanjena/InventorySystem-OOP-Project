# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Utility functions (helper code).

Step-by-step Instructions:
1. Implement data validation helpers:
   - validate_price(price) → raise error if < 0
   - validate_stock(stock) → raise error if < 0
2. Implement file helpers (optional):
   - save_to_json(data, filename)
   - load_from_json(filename)

TODO for Students:
- Add at least 2 validation functions.
- Optionally, implement file handling for persistence.
"""


# Utility/helper functions.
# TODO: Implement this file

# Utility functions for validation and file operations.
''' Utilitie functions  are helper function when price shows below zero and stock shows below zero
    then this helper functions helps to handle this type of errors'''
    
''' import module from  exception file ''' 

from exceptions import InvalidOperationError
def validate_price(price):#Ensure price > 0
    if price <0:
        raise InvalidOperationError('price can not negative')
     
    

def validate_stock(stock): #Ensure stock >= 0
    if stock<0:
        raise InvalidOperationError('stock can not be negative')
    
    
