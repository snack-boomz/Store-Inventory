# 5. Create your application file
# Create a new file in your project directory called app.py. 
# Be sure to import the appropriate Python and Peewee modules at the top of this file.

from peewee import *

# 6. Initialize your Sqlite database
# Initialize a Sqlite database called inventory.db.

db = Sqlitedatabase("inventory.db")

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

# 8. Connect the database and create tables
    #  In your dunder main method:
    # 1 Ensure you are connected to the database you created/initialized
    # 2 Ensure you load the CSV products data into the created table
    # 3 Run the application so the user can make menu choices and interact with the application.

if __name__ == "__main__":
    db.connect()
    db

    menu_loop()

