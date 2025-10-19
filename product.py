# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Product class.

Step-by-step Instructions:
1. Define a Product class with attributes:
   - product_id (int)
   - name (str)
   - price (float)
   - stock (int)
2. Add __init__ method to initialize attributes.
3. Add __str__ method to return a nice string representation.
4. Add update_stock method to increase or decrease stock.
   - Ensure stock cannot go below 0.
5. Add apply_discount method (optional extended scope).

TODO for Students:
- Implement Product class fully.
- Ensure validations (e.g., price >= 0, stock >= 0).
- Raise exceptions for invalid inputs.
"""



 
'''
->Product class represents a single store item. 
->import exceptionaly file
->Each product has attributes: id, name, price, stock, and category.
->Initialize product attributes
'''
from exceptions import InvalidOperationError
class Product:
    def __init__(self, product_id, p_name, price, stock, category):
        self.product_id=product_id
        self.p_name=p_name
        self.price=price           
        self.stock=stock
        self.category=category
        
    def update_stock(self, quantity):
        
        ''' This instance method maintains incrising or decreasig of stocks value
        in store.
        Raise exception if stock goes negative '''
            
        if self.stock+quantity<0:
            raise InvalidOperationError('invalid operation')
        self.stock+=quantity
        return f"total quantity of that product is --> {self.stock}"
        
    def update_price(self, new_price):
        ''' This method maintain price of product when the price get canges
            it raise exceptions when price get negative'''
        if new_price < 0:
            raise InvalidOperationError('invalid operation')
        self.price=new_price
      
        

    def apply_discount(self, percent):
        ''' This method used to apply discount on a product'''
        if percent < 0 or percent > 100:
            raise InvalidOperationError ('invalid discount')
        discount_amount= self.price*(percent/100)
        self.price-=discount_amount
        return f"final price of this product is--> {self.price}"
        
    def __str__(self):
        ''' it's  Return formatted product details'''
        return f"Name of product is : {self.p_name} product id is : {self.product_id} price of product : {self.price} , total stock is :{self.stock} and category is : {self.category}"
        