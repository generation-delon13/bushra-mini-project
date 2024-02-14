import test_myprojectdata

# Order status list    
order_status = ["Pending", "Cancelled", "Delivered", "Shipped"]

courier_list = ["DPD", "Amazon", "Royal mail", "Evri"]

# Order in a list of dictionaries
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

# Started my code with a input to allow user interface
name = input("Hello, what is your name?: ")
# Printing a welcome message with the users input of their name
print("Hello " +name + ", welcome to Bushra's cafe!")
print()

# Load Product List and make the list into in string
file = open("products.txt", "r")
contents = file.read()
print(contents)
    
file = open("couriers.txt", "r")
info = file.read()
print(info)

# Reading the contents from the csv file into the menu program, which includes the extended list 
import csv

with open("products.csv", "r") as file:
    file = csv.reader(file, delimiter = ",")
    for row in file:
        print(row)
        
# Open couriers file and add couriers, try and expect if file is not found
file = None
couriers_new =["Just eat", "Deliveroo"]
try:
    file = open('couriers.txt', 'a')
    for item in couriers_new:
        file.write(item + '\n')
except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))
finally:
    if file:
        file.close()     

print("Please see the options below:")

# function to define menu, it's job is to only print the data in the brackets. If my menu changes, I only have to change it once. It will loop until the user chooses to exit
def main_menu():
        print(""" ---- MAIN MENU ----
            
        [0]: Exit program
        [1]: Products Menu
        [2]: Couriers Menu
        [3]: Orders Menu""")
        
        user_input = input("Please select an option: ")
        print(user_input)
        while True:
            # Needed an option to save program, I was having problems with the nested loops 
            if user_input == "0":
                print("Exiting app")
                break
            elif user_input == "1": 
                product_menu()
            elif user_input == "2":
                couriers_menu()
            elif user_input == "3":
                orders_menu()
            else:
                input("Please select valid option: ")
                 
# function to define orders menu, it's job is to only print the data in the brackets and procced to a sub menu
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
            for i, order in enumerate(orders):
                print(i, order)
                print(f'Order number {i}')
                print(f'Customer name: {order['customer_name']}')
                print(f'Customer address: {order['customer_address']}')
                print(f'Customer phone: {order['customer_phone']}')
                print(f'Order status: {order['status']}')
                print("")
        elif user_input == "2":
            create_new_order()
            orders.append(create_new_order)
            # Enumerating takes the collection of the dictionaries and iterates with the corresponding index, adding as it goes throught the list 
        elif user_input == "3":
            print("Our orders are:\n")
            for i, order in enumerate(orders):
                print(f"{i}:{order}")
            update_index = int(input("\nEnter the number of order you want to update: "))
            for i, status in enumerate(order_status):
                print(f"{i}:{status}")
            new_order_status = int(input("Enter the new status of the order: "))
            dict_to_update = orders[update_index]
            dict_to_update["Status"] = order_status[new_order_status]
            print("Updated status order: ")
            for i, items in enumerate(orders):
                print(f'{i}:{items}')
        elif user_input == "4":
            print('Our orders are:\n')
            for i, order in enumerate(orders):
                    print(f"{i}:{order}")
            update_index=int(input("\nEnter the index of order you want to update: "))
            dic_to_update=orders[update_index]
            for key, value in dic_to_update.items():
             print(f'{key}:{value}')
            new_cus_name=input('Enter the new value for customer name (leave blank to keep current value):')
            new_cus_add=input('Enter the new value for customer address(leave blank to keep current value):')
            new_cus_phno=input('Enter the new value for customerphone (leave blank to keep current value):')
            if new_cus_name:
                dic_to_update['customer_name']=new_cus_name
            if new_cus_add:
                dic_to_update['customer_address']=new_cus_add
            if new_cus_phno:
                dic_to_update['customer_phone']=new_cus_phno
            print('Our orders are :\n')
            for i, order in enumerate(orders):
                    print(f"{i}:{order}")
        else:
            input("Please select valid option: ")
            
# What does this do?? 
def create_new_order():
    try:
        customers_name = input("Customers name:")
        customers_address = int(input("Customers address:"))
        customers_number = int(input("Customers number:"))
    except:
        print("Something went wrong")

# What does this do? 
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
                courier_list = ["DPD", "Amazon", "Royal mail", "Evri"]
                print(*courier_list, sep="\n")
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
   
# User input 
def create_new_courier():
    courier_name = input("Courier name:")
    courier_number = input("Courier number:")
 
# # Order status list    
# order_status = ["Pending", "Cancelled", "Delivered", "Shipped"]

# courier_list = ["DPD", "Amazon", "Royal mail", "Evri"]

# What does this do? 
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
            food = ["Fries", "Chicken", "Wings", "Water", "Orange Juice", "Pie", "Patty"]
            print(*food, sep="\n")
            break
        elif user_input == "2":
            food = ["Fries", "Chicken", "Wings", "Water", "Orange Juice", "Pie", "Patty"]
            for x in range(1):
                food_input = input ("Please enter the product you would like to add: \n")
                print(f"\n{food_input} added successfully !")
                print("")
                food.append(food_input)
                print(food)
        else:
                input("Please select valid option: ")
                   
def food():
    food = ["1- Fries", "2- Chicken", "3- Wings", "4- Water", "5- Orange Juice", "6- Pie", "7- Patty"]
    
def new_product():
    input("Please enter product you would like to add:")
    
main_menu()