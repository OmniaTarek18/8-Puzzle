import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Algorithms.search_technique import SearchTechnique   
  
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.path = []    
        self.results = {}
        self.current_index = 0
        self.current_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.puzzle_labels = []
        self.results_labels = {}
        
        main_widget = QWidget()  
        self.setCentralWidget(main_widget)
        
        # set up the window
        self.setWindowTitle("8 Puzzle")
        self.resize(900,600)

        # create left_widget (contains input fields and labels)
        left_widget = QWidget()
        left_widget.setFixedWidth(300)  
        
        # create layout for left widget 
        left_layout = QVBoxLayout(left_widget)
        left_widget.setStyleSheet("border-right: 1px solid #4D4D4D;")

        # create input fields
        self.init_state = QLineEdit()
        self.init_state.setPlaceholderText('e.g. 1,2,3,4,5,6,7,8,0')
        self.algorithm = QComboBox()
        self.algorithm.addItem("BFS")
        self.algorithm.addItem("DFS")
        self.algorithm.addItem("Iterative DFS")
        self.algorithm.addItem("A* Manhattan")
        self.algorithm.addItem("A* Euclidean")
        
        # create labels 
        init_state_label = QLabel("Initial State")
        algorithm_label = QLabel("Choose an Algorihm")
        
        # create solve button
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve)
        
        left_layout.addStretch()
        left_layout.addWidget(init_state_label)
        left_layout.addWidget(self.init_state)
        left_layout.addWidget(algorithm_label)
        left_layout.addWidget(self.algorithm)
        left_layout.addWidget(solve_button)
        left_layout.setSpacing(20)
        left_layout.addStretch()
        
        
        # create right_widget (contains puzzle, path, cost, running time, depth, node_explored)
        right_widget = QWidget()
        right_widget.setFixedWidth(600)
        
        # puzzle
        self.puzzle_layout = QGridLayout()
        self.puzzle_layout.setContentsMargins(30,0,30,0)
        self.puzzle_layout.setSpacing(0)  
        for i, value in enumerate(self.current_state):
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            if value > 0:
               self.set_label_style(label, value)  
            else :
                self.set_free_label_style(label)          
            self.puzzle_labels.append(label)
            self.puzzle_layout.addWidget(label,(i // 3),(i % 3))
        
        # buttons (next - step - prev)
        path_layout = QHBoxLayout()
        path_layout.setContentsMargins(0,20,0,20)
        
        self.step_label = QLabel()
        self.step_label.setAlignment(Qt.AlignCenter)
        self.step_label.setFixedWidth(100)
        
        prev = QPushButton("prev step")
        next = QPushButton("next step")
        
        next.clicked.connect(self.next_step)
        prev.clicked.connect(self.prev_step)
        
        prev.setFixedWidth(100)
        next.setFixedWidth(100)
        
        path_layout.addStretch()
        path_layout.addWidget(prev)
        path_layout.addWidget(self.step_label)
        path_layout.addWidget(next)
        path_layout.addStretch()
        
        # info layout
        self.results_layout = QVBoxLayout()
        self.create_result_labels()
        
        # create layout for left widget 
        right_layout = QVBoxLayout(right_widget)
        right_layout.addStretch()
        right_layout.addLayout(self.puzzle_layout)
        right_layout.addLayout(path_layout)
        right_layout.addLayout(self.results_layout)
        right_layout.addStretch()
        
        # create main layout which include both left and right widgets
        main_layout = QHBoxLayout(main_widget)
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)
        
        self.set_main_stylesheet(self)
     
    def solve(self):
        input = self.init_state.text()
        
        if not self.is_valid_input(input) :
            return
        
        init_state = int(input.replace(",",""))        
        type = self.algorithm.currentText()
        
        algorithm = None
        if type.split(" ")[0] == "A*":
            algorithm = SearchTechnique(type.split(" ")[0], init_state, type.split(" ")[1])
            
        else :  
            algorithm = SearchTechnique(type, init_state)
        
        if not algorithm.is_solvable(): 
            self.show_error_message("The Puzzle Can't Be Solved")
            return   
        
        algorithm.solve()   
        algorithm.get_path()
        
        self.results = {
            'Cost' : algorithm.cost,
            'Running Time' : algorithm.running_time,
            'Depth':  algorithm.depth,
            'Nodes Explored': len(algorithm.explored),
            'Path' : algorithm.path
        }
         
        self.path = self.results['Path']
        
        self.current_index = 0
        self.update_result_labels(self.results)
        self.update_current_state()
    
    def next_step(self):
        if self.current_index >= len(self.path)-1 or len(self.path) == 0:
            return
        self.current_index+= 1
        self.update_current_state()
        
    def prev_step(self):
        if self.current_index <= 0:
            return
        self.current_index-= 1
        self.update_current_state()
        
    def update_current_state(self):
        state = self.path[self.current_index]
        self.current_state = str(state)
        self.step_label.setText(str(self.current_index))
        self.update_puzzle()
        
    def update_puzzle(self):
        # adding leading 0 if state length = 8 instead of 9
        if len(self.current_state) == 8 :
            self.current_state = '0' + self.current_state
            
        # update the labels with the right number or empty in case of 0
        for i, label in enumerate(self.puzzle_labels):
            value = self.current_state[i]
            if int(value) > 0:
                self.set_label_style(label, value)
            else:
                self.set_free_label_style(label)
            str_value = value if int(value) > 0 else ""
            label.setText(str_value)
            
    def create_result_labels(self):
        items = ['Cost', 'Running Time', 'Depth', 'Nodes Explored']
        self.results_layout.addStretch()
        for i in items:
            label = QLabel()
            self.results_labels[i] = label
            self.results_layout.addWidget(label) 
        self.results_layout.addStretch()
               
    def update_result_labels(self, results):
        for i in self.results_labels:
            label = self.results_labels[i]
            label.setText(f'{i} :    {self.results[i]}')
        
    def validate_input_form(self, input):
        # use regex to validate the input (8 numbers from 0 to 8 + , and one number from 0 to 8)
        regex = r"^([0-8],){8}[0-8]$"
        match = re.search(regex, input)
        if match:
            return True
        else :
            return False
        
    def is_valid_input(self, input):
        # validate the input form (1,2,3,0,...)
        if not self.validate_input_form(input):
            self.show_error_message("Please, Enter valid state e.g. 0,1,2,3,4,5,6,7,8")
            return False
       
        init_state = [int(x) for x in input.split(",")]
        
        # check uniqueness
        if len(init_state) > len(set(init_state)):
            self.show_error_message("Please, Don't repeat any number")
            return False
        
        return True
        
        
    def show_error_message(self, message):
        msg = QMessageBox() 
        self.set_main_stylesheet(msg)        
        msg.setIcon(QMessageBox.Warning) 
        msg.setText(message) 
        msg.setWindowTitle("Invalid Input") 
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.exec_() 
        
    def set_main_stylesheet(self, component):
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
    def set_free_label_style(self, label):
        label.setText("") 
        label.setStyleSheet("""
            padding: 40px;
            border: 1px solid black;
            border-radius:10px;
            font-weight: bold;
            background-color: #3E3E42;
        """)  
        
    def set_label_style(self, label, value):
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
           
   
if __name__ == "__main__":       
    # Application initialization
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
