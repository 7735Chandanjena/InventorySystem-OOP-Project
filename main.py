# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Main entry point of the Inventory Management System.

Step-by-step Instructions:
1. Import classes: Product, Category, Store, Report.
2. Create a Store object (this will hold all products and categories).
3. Implement a simple menu system:
   a. Add product
   b. Remove product
   c. Update stock
   d. Generate report
   e. Exit
4. Use input() to interact with the user.
5. Call appropriate Store methods based on the menu choice.


"""



''' importing all module in main file '''
from store import Store    
from product import Product
from report import Report
#import json
""" 
Main entry point for the Inventory Management System.

This program allows the user to:
--> Add, remove, or update products.
--> Manage stock and pricing.
--> Apply discounts by category.
--> Generate reports such as total inventory value, low stock items, and category summaries.
--> Export data to JSON  files for record keeping.
"""

def main():
    my_store=Store("Alice'sstore")
  
    p1= Product(101, "Laptop", 50000, 10, "Electronics") 
    p2= Product(102, "Mouse", 500, 3, "Electronics")
    p3= Product(103, "Jeans", 1200, 8, "Clothing")
    
    my_store.add_product(p1)
    my_store.add_product(p2)
    my_store.add_product(p3)
    
    
    while True:
        print("Inventory ManageMent system")
        print('1 --> add product')
        print('2  -> Remove Product')
        print('3 --> Update Stock ')
        print('4 --> Update Price')
        print('5 --> Apply Discount ')
        print('6 --> Show Reports ')
        print('7 --> Export Data')
        print('8 --> Saving data in file')
        print('9--> Exit')
        
        choice=input("Enter your choice---->")
        try: 
            if choice == '1':  # add product in store.
                Id=int(input("Enter product id-->"))
                name=input("enter product name -->")
                price=float(input("enter price -->"))
                stock=int(input("enter stock -->"))
                category=input("enter category name -->")
                catg_id=input('enter category id -->')
                prod=Product(Id,name,price,stock,category)
                my_store.add_product(prod,catg_id)
                print(f"product {name} add successfully.")
            elif choice == '2': # remove product fron Inventory and category.
                Id= int(input("enter id -->"))
                my_store.remove_product(Id)
            elif choice == '3': # Update the stock value of product.
                Id =int(input("enter id -->"))
                qty=int(input("enter quantity of product -->"))
                my_store.update_stock(Id,qty)
            elif choice == '4': # Update the price of product.
                Id=int(input("enter id -->"))
                new_price=float(input("enter new price -->"))
                my_store.update_price(Id,new_price)
            elif choice == '5':  # Apply the discount on a specific category.
                category_name=input('enter category name -->')
                discount_percent=float(input("enter discount percentage -->"))
                my_store.apply_discount_to_category(category_name,discount_percent)
            elif choice == '6': # For getting total Inventory value.
                report=Report(my_store)
                print(report.total_inventory_value())
                low_stock=report.low_stock_items()
                if low_stock:
                    for prod in low_stock:
                        print(prod)
                else:
                    print("no loe stock item")
                print(report.category_summary())
            elif choice == '7': # Return all products details.
                my_store.list_all_products()
            elif choice=='8': # sotre all details in store record file.
                report=Report(my_store)
                report.export_to_json('store_record.json')
                print("all data saved")
                
                
            elif choice == '9':  # Comed out side from the loop or program.
                print("Exit")
                break
        except Exception as e:
            print(f" error found --> {e}")

if __name__=="__main__": # this block runs the main program....
    main()       
        

                

   
    


