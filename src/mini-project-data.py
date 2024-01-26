# started my code with a input to allow user interface
name = input("Hello, what is your name?: ")

print("Hello " +name + ", welcome to Bushra's cafe!")
print()

print("Please see the options below:")

# function to define menu, it's job is to only print the data in the brackets. If my menu changes, i only have to change it once.
def main_menu():
    while True:
        print(""" ---- MAIN MENU ----
            
        [0]: Exiting the program.
        [1]: Products Menu
        [2]: Orders Menu""")
        user_input = input("Please select an option: ")
        if user_input == "0":
            print("Exiting program")
            break
        elif user_input == "1": 
            product_menu()
        elif user_input == "2":
            orders_menu()
            
#     print()
# user_input = input("Please select an option: ")
    
def exiting_program():
    while True:
        user_input = input("Please select an option: ")
        if user_input == "0": 
            print("Exiting program.")
            break
    
def orders_menu():
    while True:
        print("""---- ORDERS MENU ----
              
        0 - Return to main menu
        1 - Print orders list
        2 - Create new order 
        3 - Update exisitng order status""")
        user_input = input("Please enter your option from orders menu: ")
        if user_input == "0":
            main_menu()
        elif user_input == "1":
            orders_list()
        elif user_input == "2":
            create_new_order()
        elif user_input == "3":
            update_order_status = print("Updating existing order status")
            
def create_new_order():
    customers_name = input("Customers name:")
    customers_address = input("Customers address:")
    customers_number = input("Customers number:")
        
# update_order_status
# new_product 
# def update_list
            
def orders_list():  
    customer_list = [{
    "customer_name": "Sam",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0765789334",
   "status": "preparing"}, 
                     
    {"customer_name": "John",
   "customer_address": "Flat 6, Ilterdon Road, LONDON, N1 2HZ",
  "customer_phone": "0765785634",
   "status": "preparing"}, 
    
    {"customer_name": "Sam",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0765789334",
   "status": "preparing"}, 
    
    {"customer_name": "Sam",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0765789334",
   "status": "preparing"}] 
    
def product_menu():
    while True:
        print("""---- PRODUCT MENU ---- 
              
        0 - Return to main menu
        1 - Show products list
        2 - Create new product
        3 - Update existing product""")
        user_input = input("Please enter your option from product menu: ")
        if user_input == "0":
            main_menu()
        elif user_input == "1":
            food = ["1- Fries", "2- Chicken", "3- Wings", "4- Water", "5- Orange Juice", "6- Pie", "7- Patty"]
            for x in food:
                print(x)
        elif user_input == "2":
            new_product = input("\nPlease enter the product you would like to add: ")
            food.append(new_product)
            print(f"\n{new_product} added successfully!")
        elif user_input == "3":
            print(food)
            update_list = int(input)
        else:
            input("Please select valid option: ")
                   

def new_product():
    input("Please enter product you would like to add:")
    
main_menu()

# if option == 0:
#     print("Exiting program.")
# elif option == 1:
#     print("You have selcted Products Menu.")
# elif option == 2:
#     print("You have selected O=
#     print("Ycted Products Menu.")
# elif option == 2:
#     print("You have selected Orders Menu.")
# else:
#     print("Please select a valid option.")

# while True:
#    food =

# product_menu= input()
# if a == "a":
#     print(product_menu)
# elif b == "b":
#     print("Exiting menu")

# amount = 12.40
# merchant = 'Amazon'
# transaction_str = f'You spent £{amount} at {merchant}'
# print(transaction_str)

# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# third_person = people[1:2]
# print(third_person)

# drinks = ['Coffee', 'Tea', 'Water']

# try:
#   drink_option = int(input('Enter a drink index: '))
#   chosen_drink = drinks[drink_option]
#   print(f'You chose {chosen_drink}')
# except:
#   print('That drink index does not exist!')

# print("                       ")
# menu = {"Pizza": 3.00,
#         "Cheese Burger": 2.00,
#         "Chips": 1.50,
#         "Coke": 1.00,
#         "Water": 1.00,}
# for key, value in menu.items():
#     print(f"{key:15}: £{value:.2f}")