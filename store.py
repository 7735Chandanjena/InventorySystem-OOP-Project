# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Store class.

Step-by-step Instructions:
1. Create Store class with attributes:
   - name (str)
   - products (dict → product_id: Product)
   - categories (dict → category_id: Category)
2. Methods:
   - add_product(product)
   - remove_product(product_id)
   - update_stock(product_id, qty)
   - get_product(product_id) → return Product object
   - list_all_products()
3. Ensure error handling:
   - Invalid product IDs
   - Negative stock updates

TODO for Students:
- Implement Store class methods.
- Maintain consistent product and category mappings.
- Use custom exceptions for errors.
"""


# Handles the Store class and product operations.
# TODO: Implement this file
# Store class manages all products and categories.
# Acts like a central manager.
''' importing modules to operate stores'''
from product import Product 
from category import Category
from exceptions import ProductNotFoundError, InvalidOperationError,CategoryNotFoundError

class Store:
    def __init__(self,name):
        ''' In store class has attributes : name,
            all products in store arrange using dictionary
            all categories of store arrange using dictionary '''
        self.name=name
        self.products={}
        self.categories={}
        # TODO: Maintain dict of products (id → Product)
        # TODO: Maintain dict of categories (name → Category)
        

    def add_product(self, product,category_id=None):
        ''' This method add products into  Inventory as well as in their specific 
            category also. '''
        if product.product_id in self.products:
          raise InvalidOperationError(f"Product id--> {product.product_id} already exists.")
        self.products[product.product_id] = product
        
        category_name=product.category
        if category_name not in self.categories: 
            self.categories[category_name]=Category(category_name,category_id)
        self.categories[category_name].add_product(product)
        return f" Added '{product.p_name}' under category '{category_name}'."
        

    def remove_product(self, product_id):
        ''' it removes products from Inventory and categtory also.'''
        if product_id not in self.products:
           raise ProductNotFoundError(f"No product found with id {product_id}.")
         
        product = self.products.pop(product_id)
        category = self.categories.get(product.category)
        
        
        if category:
            category.remove_product(product_id)

        print(f" Remove {product.p_name} from store and category {product.category}")
                

    def update_stock(self, product_id, qty):
        ''' This method maintains stock value of products of Inventory as well as
            category also.'''
        if product_id not in self.products:
           raise ProductNotFoundError(f"No product found with ID {product_id}.")
        product = self.products[product_id]
        
        if product.stock + qty < 0:
            raise InvalidOperationError(f"Cannot reduce stock below zero for product {product.name}.")
        product.update_stock(qty)
        print(f" Updated stock of {product.p_name} -> {product.stock} units.")
        # Update stock by calling Product.update_stock()
        

    def update_price(self, product_id, new_price):
        ''' this method for updating the price of products in Inventory.'''
        if product_id not in self.products:
            raise ProductNotFoundError(f"{product_id} does not exits")
        product = self.products[product_id]
        if new_price < 0:
            raise InvalidOperationError("Price must be greater than zero.")
        product.update_price(new_price)
        print(f" new price of {product} is {product.price}")


    def apply_discount_to_category(self, category_name, percent):
        ''' this function helps to apply discount on a specific category.
             it raise a error when a cetagory not found in the store'''
        if category_name not in self.categories: 
            raise CategoryNotFoundError(f"Category {category_name} does not exist.")
            
        category=self.categories[category_name]
        if percent <= 0 or percent > 100: # Ensure the percent must be greater then 0 and lessthan 100.
            raise InvalidOperationError("Discount percent must be between 1 and 100.")
        for product in category.products: 
            old_price = product.price
            discount = old_price * (percent / 100)
            product.price -= discount

            print(f" Applied {percent} percent discount on all products in {category_name} category.")
        
        

    def list_all_products(self):   #Return all products in store.
        if not self.products:
            print(" No products available in the store.")
            return
        for product in self.products.values():
            print(f" --> {product}")
         
        

    def find_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError(f"this {product_id} doesn't exits!")
        print('the product is')
        return self.products.get(product_id) 
        
    # find products in store.    