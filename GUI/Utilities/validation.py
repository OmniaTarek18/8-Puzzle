import re
from GUI.Utilities.styles import set_main_stylesheet
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
    
def is_valid_input(input):
    # validate the input form (1,2,3,0,...)
    if not validate_input_form(input):
        show_error_message("Please, Enter valid state e.g. 0,1,2,3,4,5,6,7,8")
        return False
    
    init_state = [int(x) for x in input.split(",")]
    
    # check uniqueness
    if len(init_state) > len(set(init_state)):
        show_error_message("Please, Don't repeat any number")
        return False
    
    return True
    
def validate_input_form(input):
    # use regex to validate the input (8 numbers from 0 to 8 + , and one number from 0 to 8)
    regex = r"^([0-8],){8}[0-8]$"
    match = re.search(regex, input)
    if match:
        return True
    else :
        return False
    
def show_error_message(message):
    msg = QMessageBox() 
    set_main_stylesheet(msg)        
    msg.setIcon(QMessageBox.Warning) 
    msg.setText(message) 
    msg.setWindowTitle("Invalid Input") 
    msg.setStandardButtons(QMessageBox.Ok) 
    msg.exec_() 