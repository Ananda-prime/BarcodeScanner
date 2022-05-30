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
from time import gmtime, strftime
import time


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
        self.ui.enter.clicked.connect(self.getEmpolyee_details)

        t = Thread(target=self.getEmpolyee_details)
        t2 = Thread(target=self.current_time)
        t.start()
        t2.start()

    def current_time(self):
        while True:
            self.live_time = self.ui.display_time.setText(strftime("%H:%M:%S \n %d:%m:%Y", gmtime()))
            #print(strftime("%H:%M:%S", gmtime()))
            time.sleep(1)

    def getEmpolyee_details(self):
        '''Scanning the barcode and printing the user details
        if not print error message'''

        while True:
            self.user_in = (input("Enter the serial vale:").upper())

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
                break
       #self.user_in = (input("Enter the serial vale:").upper())
        self.user_in = self.ui.lineEdit.text()
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
            #break
                # print(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    #window.getEmpolyee_details()
    sys.exit(app.exec())