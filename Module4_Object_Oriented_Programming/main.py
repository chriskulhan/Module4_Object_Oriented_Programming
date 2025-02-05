# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls
class DunnDelivery:
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        #Menu attribute = menu of items you can order to be delivered:
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        #Prices are encapsulated within the class:
        #initialize it right now, assign in values
        #using a dictionary, there is a single key and single value
        self.prices = {
            "Monster" : 3.99, 
            "Rockstar": 3.99, 
            "Latte": 4.99,
            "Cappuccino": 4.99,
            "Bagel": 2.99,
            "Muffin": 2.99,
            "Scone": 2.99,
            "Falafel Wrap": 8.99,
            "Hummus & Pita": 7.99,
            "Chicken Wrap": 8.99
        }

        #Add a dictionary of the delivery locations and number minutes to deliver to that location
        #use keyword self, because 
        #key-value pairs, key is location, value is number of minutes to that location
        self.delivery_locations = {
            "Library":10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
#Show the menu of items available for delivery
# Create a new method using def
#category is set to none by default
def show_menu(self, category = None)   
    #if there is a category value chosen, print items in category:
    if category: 
        print(f"\n=== {category} ===")     
        #Loop through items in category on the menu, display them to the user:
        #use for loop, predefined number of items
        for item in self.menu[category]:
            print(f"{item}: ${self.price[item]:.2f}")
    else:
        #show the entire menu if they haven't specified a category
        for category in self.menu:
            #show the category name:
            print(f"\n=== {category} ===")
            #nest a second for loop, to go through each item within the category
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]}:.2f")
#Method to calculate the total cost of the order:
#set false as default
def calculate_total(self, items, has_student_id = False):
    #Calculate the total 
    total = sum(self.prices[item]) for item in items)
        
    #calculate the student discount based on the student id  
    #if has_student_id = True and total is more than 10
    if has_student_id and total > 10:
        total *= 0.9

    #this method returns the total cost of the order to the code that called the method
    return total;    