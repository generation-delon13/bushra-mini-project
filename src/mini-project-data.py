orders = [{"customer_name": "John",
    "customer_address": "Flat 6, Ilterdon Road, LONDON, N1 2HZ",
   "customer_phone": "0765785634",
   "status": "preparing"}, 
    
    {"customer_name": "Sam",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
   "customer_phone": "0765789334",
    "status": "preparing"}, 
    
     {"customer_name": "Bill",
    "customer_address": "68, Summerland Rd, LONDON, SE14 6FW",
   "customer_phone": "0785789334",
    "status": "preparing"}] 

# started my code with a input to allow user interface
name = input("Hello, what is your name?: ")

# Printing a welcome message with the users input of their name
print("Hello " +name + ", welcome to Bushra's cafe!")
print()

# Load Product List and make the list into in string
file = open("products.txt", "r")
contents = file.read()
print(contents)

print("")
    
file = open("couriers.txt", "r")
contents = file.read()
print(contents)
    

# Reading the contents from the csv file into the menu program, which includes the extended list 
import csv

with open("products.csv", "r") as file:
        file = csv.reader(file, delimiter = ",")
        for row in file:
            print(row)
# new_food_list = load_data("products.csv") - append to the list?       

print("Please see the options below:")

# function to define menu, it's job is to only print the data in the brackets. If my menu changes, I only have to change it once. It will loop until the user chooses to exit
def main_menu():
        print(""" ---- MAIN MENU ----
            
        [0]: Save or exit program
        [1]: Products Menu
        [2]: Couriers Menu
        [3]: Orders Menu""")
        
        user_input = input("Please select an option: ")
        print(user_input)
        while True:
            # need an option to save program
            if user_input == "0":
                save_or_exit()
            elif user_input == "1": 
                product_menu()
            elif user_input == "2":
                couriers_menu()
            elif user_input == "3":
                orders_menu()
            else:
                input("Please select valid option: ")
            

def save_or_exit():
        print(""" Would you like to save or exit program?
        [0]: Save products list to products.txt
        [1]: Save couriers list to couriers.txt
        [2]: Exit program""")
        
        while True:
            user_input = input("Please select an option: ")
            if user_input == "2": 
                print("Exiting program.")
                break
            elif user_input == "1":
                with open("couriers.txt", "a") as file:
                 file.write() 
                 print("Saving couriers list to couriers.txt.")
                 break
            elif user_input == "0":
                print("Saving products list to products.txt. ")
                break

def orders_menu():
    while True:
        print("""---- ORDERS MENU ----
              
        0 - Return to main menu
        1 - Print orders list
        2 - Create new order
        3 - Update existing order status
        4 - Update exisitng order""")
        
        user_input = input("Please enter your option from orders menu: ")
        if user_input == "0":
            main_menu()
        elif user_input == "1":
            # iterating through my listed dictionary, allows a clear reading of the multiple keys and values
            print('Orders Summary:')
            print("")
            for i, order in enumerate(orders, 1):
                # print(i, order)
                print(f'Order number {i}')
                print(f'Customer name: {order['customer_name']}')
                print(f'Customer address: {order['customer_address']}')
                print(f'Customer phone: {order['customer_phone']}')
                print(f'Order status: {order['status']}')
                print("")
        elif user_input == "2":
            create_new_order()
            orders.append(create_new_order)
        elif user_input == "3":
            print("Our orders are:\n")
            for i, order in enumerate(orders):
                print(f"{i}:{order}")
            update_index = int(input("\nEnter the index of order you want to update: "))
            for i, status in enumerate(order_status):
                print(f"{i}:{status}")
            new_order_status = (input("Enter the new status of the order: "))
            dict_to_update = orders[update_index]
            dict_to_update["Status"] = order_status[new_order_status]
            print("Updated status order: ")
            for i, items in enumerate(orders):
                print(f'{i}:{items}')
        else:
            input("Please select valid option: ")
            
def create_new_order():
    customers_name = input("Customers name:")
    customers_address = input("Customers address:")
    customers_number = input("Customers number:")
    
def couriers_menu():
    while True:
        print("""---- COURIERS MENU ----
              
        0 - Return to main menu
        1 - Print couriers list
        2 - Create new courier""")
        user_input = input("Please enter your option from couriers menu: ")
        if user_input == "0":
                main_menu()
        elif user_input == "1": 
                print(courier_list)
        elif user_input == "2":
                courier_list = ["DPD", "Amazon", "Royal mail", "Evri"]
                for x in range(1):
                    courier_input = input ("Please enter the courier you would like to add: \n")
                    print(f"\n{courier_input} added successfully !")
                    print("")
                    courier_list.append(courier_input)
                    print(courier_list)
    else:
        input("Please select valid option: ")

def create_new_courier():
    courier_name = input("Courier name:")
    courier_number = input("Courier number:")

# try:
#     user_input = int(input("Enter a number: "))
#     print("You entered:", user_input)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
        
order_status = ["Pending", "Cancelled", "Delivered", "Shipped"]

courier_list = ["DPD", "Amazon", "Royal mail", "Evri"]

# update_order_status
# new_product 
# def update_list
       
 # Benefits of using lists is the data stays constant, if one is removed I can still use the data in the same way
  
# need to append order to orders list create_new_order.append
    
def product_menu():
     while True:   
        print("""---- PRODUCT MENU ---- 
              
        0 - Return to main menu
        1 - Show products list
        2 - Create new product""")
        
        user_input = input("Please enter your option from product menu:")
        if user_input == "0":
                main_menu()
        elif user_input == "1":
            food = ['\n' "1- Fries", "2- Chicken", "3- Wings", "4- Water", "5- Orange Juice", "6- Pie", "7- Patty"]
            print(*food, sep="\n")
            break
        elif user_input == "2":
            food = ['\n' "1- Fries", "2- Chicken", "3- Wings", "4- Water", "5- Orange Juice", "6- Pie", "7- Patty"]
            for x in range(1):
                food_input = input ("Please enter the product you would like to add: \n")
                # print(food)
                print(f"\n{food_input} added successfully !")
                print("")
                food.append(food_input)
                print(food)
                # new_product = input("\nPlease enter the product you would like to add: ")
                # food.append(new_product)
                # print(f"\n{new_product} added successfully !")
        else:
                input("Please select valid option: ")
                   
def food():
    food = ["1- Fries", "2- Chicken", "3- Wings", "4- Water", "5- Orange Juice", "6- Pie", "7- Patty"]
    
def new_product():
    input("Please enter product you would like to add:")
    
main_menu()

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


# PRINT products list with its index values
#         GET user inputs for comma-separated list of product index values
#         CONVERT above user input to a string e.g. "2,1,3"

#         PRINT couriers list with index value for each courier
#         GET user input for courier index
#         SET order status to be 'PREPARING'

#         CREATE new order dictionary with above properties
#         APPEND order dictionary to orders list

#     ELSE IF user input is 3:
#         # UPDATE existing order status

#         PRINT orders list with its index values
#         GET user input for order index value

#         PRINT order status list with index values
#         GET user input for order status index value
#         UPDATE status for order
