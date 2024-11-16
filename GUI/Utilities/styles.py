        
def set_main_stylesheet(component):
    component.setStyleSheet("""
        * {
            color: #FFFFFF;
            font-size: 16px;   
        }
        QMainWindow, QMessageBox {
            background-color: #2D2D30;  
        }
        QComboBox,QComboBox QAbstractItemView, QLineEdit {
            padding: 5px; 
            border: 1px solid #4D4D4D; 
            border-radius: 5px; 
            background-color: #3E3E42; 
        }
        QPushButton {
            background-color: #AF4F4C; 
            padding: 10px; 
            border: none; 
            border-radius: 5px; 
        }
        QPushButton:hover {
            background-color: #964341; 
        }
    """)
def set_free_label_style(label):
    label.setText("") 
    label.setStyleSheet("""
        padding: 40px;
        border: 1px solid black;
        border-radius:10px;
        font-weight: bold;
        background-color: #3E3E42;
    """)  
    
def set_label_style(label, value):
    label.setText(str(value))
    label.setStyleSheet("""
        padding: 40px;
        border: 1px solid black;
        border-radius: 10px;
        margin: 0.5px;
        font-size: 25px;
        font-weight: bold;
        background-color: #504caf;
    """) 