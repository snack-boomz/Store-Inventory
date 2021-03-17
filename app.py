#!/usr/bin/env python3

# 5. Create your application file
# Create a new file in your project directory called app.py. 
# Be sure to import the appropriate Python and Peewee modules at the top of this file.

import datetime
import csv

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
    product_quantity = TextField()
    product_price = TextField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def load_csv():

    with open('inventory.csv', newline='') as csvfile:
        artreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(artreader)
        counter = 0
        # 27 total products
        for row in rows:
            print(row)
            try:
                Product.create(
                               product_name=row['product_name'],
                               product_price=row['product_price'],
                               product_quantity=row['product_quantity'],
                               date_updated=row['date_updated'])
            # referenced from students.py exercise
            except IntegrityError:
                pass

def print_table():
    pass
    products = Product.select()
    for product in products:
        print(product.date_updated)


# 8. Connect the database and create tables
    #  In your dunder main method:
    # 1 Ensure you are connected to the database you created/initialized
    # 2 Ensure you load the CSV products data into the created table
    # 3 Run the application so the user can make menu choices and interact with the application.

if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    load_csv()
    #print_table()

   # menu_loop()

