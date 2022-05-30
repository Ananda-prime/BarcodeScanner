import barcode
import json
from threading import *

'''Opening JSON file'''
f = open("Employee_details.json")
'''returns JSON object as a dictionary'''
data = json.load(f)
print(data)

class Employee_details:
    def __init__(self):
        pass

    def getEmpolyee_details(self):
        '''Scanning the barcode and printing the user details
        if not print error message'''
        while True:
            user_in = (input("Enter the serial vale:").upper())

            # print(user_in)
            for key, value in data.items():
                if user_in == key:
                    print(value)
                    break
            else:
                print("Error: User not found")
                print("Add New User Details")
                break
                # print(value)

    def new_employee_details(self):
        serial_id = (input("Enter the Serial ID:").upper())
        user_name = input("Enter the Name:")
        user_id = input("Enter the ID:")
        user_model = input("Enter the Model:")
        a_dict = {serial_id: {"Name": user_name, "ID": user_id, "Model": user_model}}
        print(a_dict)

        with open("Employee_details.json") as f:
            new = json.load(f)

        new.update(a_dict)

        with open("Employee_details.json", "w") as f:
            json.dump(new, f)

empolyee = Employee_details()

empolyee.getEmpolyee_details()
empolyee.new_employee_details()
f.close()
empolyee.getEmpolyee_details()