#!/usr/bin/env python3

# 5. Create your application file
# Create a new file in your project directory called app.py. 
# Be sure to import the appropriate Python and Peewee modules at the top of this file.

import datetime
import csv
import os

from collections import OrderedDict
from peewee import *


# 6. Initialize your Sqlite database
# Initialize a Sqlite database called inventory.db.

db = SqliteDatabase("inventory.db")

# 7. Create your Product model
# Create a model called Product that the Peewee ORM will use to build the database. 
# The Product model should have five attributes: 
# product_id, product_name, product_quantity, product_price, and date_updated. 
# Use PeeWee's built in primary_key functionality for the product_id field, 
# so that each product will have an automatically generated unique identifier.

class Product(Model):
    # -- https://docs.red-dove.com/peewee/peewee/models.html -- #
    # " The AutoField is used to identify an auto-incrementing integer primary key. 
    # If you do not specify a primary key, Peewee will automatically create an 
    # auto-incrementing primary key named “id”. "

    product_id = AutoField()
    product_name = TextField()
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def load_csv():

    with open('inventory.csv', newline='') as csvfile:
        artreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(artreader)
        counter = 0
        # 27 total products

        # Convert product_price format from $0.00 to 000
        for row in rows:
            # https://www.w3schools.com/python/ref_string_strip.asp
            if row['product_price']:
                list_row = list(row['product_price'])
                for character in list_row:
                    if character == "$" or character == ".":
                        list_row.remove(character)
                row['product_price'] = "".join(list_row)

            Product.create(product_name=row['product_name'],
                            product_price=row['product_price'],
                            product_quantity=row['product_quantity'],
                            date_updated=row['date_updated'])
        print("product created")

def clear():
    """Clear the menu"""
    ## Referenced from diary.py project, Unit 4
    os.system('cls' if os.name == 'nt' else 'clear')

def remove_db():
    """Utilized to prevent multiple databases being initialized/created."""
    os.system('rm inventory.db')

def print_table():
    products = Product.select().order_by(Product.product_price.desc()).get()
    print(products)

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit the application.\n")
        for key, value in menu.items():
            print('{}) {}.'.format(key, value.__doc__))
        choice = input('\nInput a choice: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()
        

def view_single_product():
    """View a single product in the inventory"""
    # 12. Displaying a product by its ID - Menu Option V
        # Create a function to handle getting and displaying a product
        #  by its product_id.
    loop = True
    while loop:    
        try:
            search_query = int(input("\nEnter a Product ID: "))
        
            if search_query > 1000:
                raise OverflowError("Your integer is out of range. Enter an integer under 1000.")

        except ValueError as err:
            # Referenced from unit 1 error handling
            print("That input is not valid. Please enter an integer.")
            print("Error: {}".format(err))

        except OverflowError as err:
            print("That input is not valid.")
            print("Error: {}".format(err))
            
        else:
            selection = Product.select()
            search_results = selection.where(Product.product_id == search_query)
            if search_results:

                for search_result in search_results:

                    print("\nSearch Result: \n")
                    print('='*len(search_result.product_name),"\n")
                    print("{}\nQuantity: {}\nCost in Cents: {}\nDate Updated: {}".format
                                                        (search_result.product_name,
                                                        search_result.product_quantity,
                                                        search_result.product_price,
                                                        search_result.date_updated))
                    input("\nPress [Enter] to continue..")
                    loop = False
            else:
                print("There is no product with that ID, please enter another product ID.")

def add_product():
    """Add a product to the inventory"""
    pass

def make_backup():
    """Backup the contents of the database"""
    pass

# Referenced from diary.py project, Unit 4

# 11. Create a Menu to make selections
  # Create a function to handle interaction with the user of your app. 
  # This function should prompt the user to enter v in order to view the details of 
  # a single product in the database, a to add a new product to the database, 
  # or b to make a backup of the entire contents of the database.


menu = OrderedDict([
    ('a', add_product),
    ('b', make_backup),
    ('v', view_single_product),
    ])

# 8. Connect the database and create tables
    #  In your dunder main method:
    # 1 Ensure you are connected to the database you created/initialized
    # 2 Ensure you load the CSV products data into the created table
    # 3 Run the application so the user can make menu choices and interact with the application.

if __name__ == "__main__":
    remove_db()
    db.connect()
    db.create_tables([Product], safe=True)
    load_csv()
    menu_loop()

   # menu_loop()

