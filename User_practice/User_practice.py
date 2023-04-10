
# declare a class and give it name Shoe
class Shoe:		
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True
skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type) # Classic Sk8-Hi
print(dress_shoe.price)	# Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

#Methods
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    def on_sale_by_percent(self,percent):
        self.price = self.price * (1-percent)

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.price)
print(dress_shoe.price)
skater_shoe.on_sale_by_percent(0.2)
dress_shoe.on_sale_by_percent(0.3)
print(skater_shoe.price)
print(dress_shoe.price)

print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

#The skater shoe is going to go on sale by 20%. Reduce price:
skater_shoe.price = skater_shoe.price * (1-0.2)
#The dress she goes on sale by 10% reduction:
dress_shoe.price = dress_shoe.price * (1-0.1)
#The skater shoe is going to go on sale by another 10%. Reduce price:
skater_shoe.price = skater_shoe.price * (1-0.1)

#OR
# skater_shoe.on_sale_by_percent(0.2)



# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada
user_2 = User()
print(user_2.first_name) # also prints Ada

user_ada.first_name
