# with open("couriers.txt", "a") as file:
#                  file.write() 
#                  print("Saving couriers list to couriers.txt.")
                 
                 
file = None
couriers_new =["DPD","Royal mail"]
try:
    file = open('couriers.txt', 'a')
    for item in couriers_new:
        file.write(item + '\n')
except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))
finally:
    if file:
        file.close()