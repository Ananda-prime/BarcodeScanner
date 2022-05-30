import sys
import os
from PySide6 import *
import qt_material
from datetime import datetime
import time
from Ui_app_rc1 import *

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

    def getEmpolyee_details(self):
        '''Scanning the barcode and printing the user details
        if not print error message'''
        while True:
            self.user_in = (input("Enter the serial vale:").upper())

            # print(user_in)
            for key, value in data.items():
                if self.user_in == key:
                    print(value)
                    break
                    self.display_user_in = str(value)
                    self.ui.display_user_details.setText(self.display_user_in)

            else:
                print("Error: User not found")
                print("Add New User Details")
                break
                self.ui.display_user_details.setText("Error: User not found \n Add New User Details ")

                # print(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    #t = Thread(target=window.getEmpolyee_details())
    #t.start()
    window.getEmpolyee_details()
    sys.exit(app.exec())