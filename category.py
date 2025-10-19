# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Category class.

Step-by-step Instructions:
1. Create Category class with attributes:
   - category_id (int)
   - name (str)
   - products (list of Product objects)
2. Add methods:
   - add_product(product)
   - remove_product(product_id)
   - list_products() → return all products in this category
3. Ensure duplicate products are not added.

TODO for Students:
- Implement Category class.
- Link products properly.
- Use exceptions for invalid operations.
"""


# Handles product categories.
# TODO: Implement this file

# Category class groups products (e.g., Electronics, Clothing).
# It can track all products under that category.
from product import Product   
from exceptions import ProductNotFoundError
class Category:
    ''' In categoy class contains attributes : category name, category id 
        a list of products in this category '''
    def __init__(self, cg_name,category_id):
        self.cg_name=cg_name
        self.category_id=category_id
        self.products=[]
                

    def add_product(self, product):
        ''' This method add products in their specific category'''
        if not isinstance(product,Product):
            raise ProductNotFoundError ('product is not type of this product')
        self.products.append(product)
        return f"products in this category -> {self.products}"
        
    def remove_product(self, product_id):
        ''' This instance method remove prducts from list of products from 
            category'''
        for prod in self.products:
            if prod.product_id==product_id:
                self.products.remove(prod)
                print(f" the product {prod.p_name} removed")
                
                return
        raise ProductNotFoundError('invalid product')

    def list_products(self):  # Return all products in this category
        return [str(x) for x in self.products]
        
    def __str__(self):
        ''' String representation → Category name + product count'''
        return f"name {self.cg_name},and category id is : {self.category_id} and list of product is : {[p.p_name for p in self.products]}"
         
        