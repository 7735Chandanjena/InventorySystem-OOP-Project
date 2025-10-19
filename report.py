# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Handles reports and data export.

Step-by-step Instructions:
1. Define Report class with methods:
   - generate_inventory_summary(store)
     → Show all products, stock, total value
   - generate_category_summary(store)
     → Group products by category
2. Export options (optional extended scope):
   - Export to JSON
   - Export to CSV

TODO for Students:
- Implement Report class.
- Write clean tabular output using print.
- Optionally, add export to a file.
"""

'''
->Generates reports for inventory.
-> TODO: Implement this file
->Reporting functions to analyze inventory.
->Also include file export for CSV/JSON.
'''
import json
import csv

class Report:
    def __init__(self, store):
        self.store = store

    def total_inventory_value(self): # get total value of Inventory.
        total_inventory_value=0
        for prod in self.store.products.values():
            total_price=prod.price*prod.stock
            total_inventory_value+=total_price
        return f"the total value is --->  {total_inventory_value}"
    

    def low_stock_items(self, threshold=5):
        """Return all products whose stock values are less than five.""" 
        low_stock=[prod.p_name for prod in self.store.products.values() if prod.stock < threshold]
        
        return low_stock
            

    def category_summary(self):
        """Return a summary showing the total number of products in each category using dictionary."""
        categories_summary={}
        for prod in self.store.products.values():
            category=prod.category   
            if category in categories_summary:
                categories_summary[category]+=1
            else:
                categories_summary[category]=1
        return f"total product in each categorty --> {categories_summary}"
    
    def export_to_json(self, storerecord):
        '''  Export product details into JSON file.'''
        data=[]
        for prod in self.store.products.values():
            data.append({'product_id':prod.product_id,
                         'p_name':prod.p_name,
                         'category':prod.category,
                         'price':prod.price,
                         'stock':prod.stock})
        with open(storerecord,'w') as f:
            json.dump(data,f,indent=4)
        print(f"all datab added to --> {storerecord}")
            
    
        

    def export_to_csv(self, store_record):
        with open(store_record,'w',newline='') as f:
            writer= csv.writer(f)
            writer.writerow(['product_id', 'p_name', 'price', 'stock', 'category'])
            for prod in self.store.products.values():
                writer.writerow([prod.product_id,prod.p_name,prod.price,prod.stock,prod.category])
        
                """Export all product details from the store into a CSV file."""
        
