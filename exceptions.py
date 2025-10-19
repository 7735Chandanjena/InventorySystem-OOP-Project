# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Custom exception classes for the system.

Step-by-step Instructions:
1. Define exceptions:
   - ProductNotFoundError
   - CategoryNotFoundError
   - InvalidStockError
2. Use these exceptions in Store, Product, and Category classes.

TODO for Students:
- Implement custom exception classes (inherit from Exception).
- Replace generic errors with meaningful custom exceptions.
"""


# Custom exception handling.
# TODO
# Custom exception classes: Implement this file
''' We implment custom exception classes inherit from Exception which is use to
    handling errors in further files.''' 

class ProductNotFoundError(Exception): # if the product is not available in store.
    def __init__(self,message='product is not avilable'):
        self.message=message
        super().__init__(message)
        
        
class InavalidstockError(Exception): # if invalid sock occure.
    def __init__(self,stock='stock is not available'):
        self.stock=stock
        super().__init__(stock)
    

class InvalidOperationError(Exception): #  if invalid oeration is occure.
    def __init__(self,operation="the operation is not correct"):
        self.operation=operation
        super().__init__(operation)

class CategoryNotFoundError(Exception): # if category is not found in store.
    def __init__(self,category="This category is not avilable"):
        self.category=category
        super().__init__(category)