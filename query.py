"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

brand = Brand.query.get(8)
# Get the brand with the **id** of 8.

model = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

model = Model.query.filter(Model.year < 1960).all()
# Get all models that are older than 1960.

brand = Brand.query.filter(Brand.founded > 1920).all()
# Get all brands that were founded after 1920.

model = Model.query.filter(Model.name.like('Cor%')).all()
# Get all models with names that begin with "Cor".

brand = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()
# Get all brands that were founded in 1903 and that are not yet discontinued

brand = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

model = Model.query.filter(Model.brand_name != "Chevrolet").first()
# Get any model whose brand_name is not Chevrolet.

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    print db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year==year)



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand=db.session.query(Brand.name, Model.name).all()

    for cars in brand:
    	print cars

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# Ans- <flask_sqlalchemy.BaseQuery object at 0x7f8ab1b5e510>
# type -<class 'flask_sqlalchemy.BaseQuery'>
# nothing runs until we want to fetch records

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# Many to Many adds an association table between two classes
# Can contain additional columns beyond those which are foreign keys to the left and right tables
# Left table relationship reference the object via one to many , the association class references the right side via many to one

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
	brands = Brand.query.filter(Brand.name.like('% + mystr + %')).all()
	return brands


def get_models_between(start_year, end_year):
    
    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
    return models
