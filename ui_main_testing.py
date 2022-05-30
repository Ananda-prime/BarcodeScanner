import sys
import os

from PySide6 import *
import qt_material
from datetime import datetime
import time
from Ui_app_rc2 import *
import barcode
import json
from threading import *


'''Opening JSON file'''
f = open("Employee_details.json")
'''returns JSON object as a dictionary'''
data = json.load(f)
print(data)

class Mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        t1 = Thread(target=self.current_time)
        t1.start()
        #t1.join()
        self.ui.enter.clicked.connect(self.getEmpolyee_details)
        self.ui.update_key.clicked.connect(self.new_employee_details)

    def current_time(self):
        while True:
            self.now_1 = datetime.now()
            self.start_time = self.ui.display_time.setText(self.now_1.strftime("%H:%M:%S \n %d:%m:%Y"))
            time.sleep(1)

    def getEmpolyee_details(self):

        '''Scanning the barcode and printing the user details
        if not print error message'''
        self.user_in = self.ui.scanbarcode.text()
        # print(user_in)
        for key, value in data.items():
            if self.user_in == key:
                print(value)
                self.display_user_in = str(value)
                print(self.display_user_in)
                self.ui.display_user_details.setText(self.display_user_in)
                break

        else:
            print("Error: User not found")
            print("Add New User Details")
            self.ui.display_user_details.setText("Error: User not found \n Add New User Details ")
            # break
            # print(value)

    def new_employee_details(self):
        self.serial_id = self.ui.serialid_text.text()
        print(self.serial_id)
        self.user_id = self.ui.uid_text.text()
        print(self.user_id)
        self.user_name = self.ui.name_text.text()
        print(self.user_name)
        self.user_wwid = self.ui.wwid_text.text()
        print(self.user_wwid)
        self.user_lap_model = self.ui.model_text.text()
        print(self.user_lap_model)

        a_dict = {self.serial_id: {"UID": self.user_id ,"Name": self.user_name,
                 "WWID": self.user_wwid, "Laptop Model": self.user_lap_model}}
        print(a_dict)

        with open("Employee_details.json") as f:
            new = json.load(f)

        update = new.update(a_dict)
        self.ui.update_key.clicked.connect(update)

        with open("Employee_details.json", "w") as f:
            json.dump(new, f)
        print("successfully added")
        f.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec())