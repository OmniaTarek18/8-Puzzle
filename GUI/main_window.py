import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Algorithms.search_technique import SearchTechnique   
from GUI.Utilities.path import get_directions
from GUI.Utilities.styles import *
from GUI.Utilities.validation import is_valid_input
from GUI.puzzle import Puzzle
from GUI.results import Results

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.path = []    
        self.results = {}
        self.current_index = 0
        self.current_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        
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
        self.puzzle = Puzzle()
        self.puzzle.setContentsMargins(30,0,30,0)
        self.puzzle.setSpacing(0)  
        
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
        self.results_layout = Results()
        
        # create layout for left widget 
        right_layout = QVBoxLayout(right_widget)
        right_layout.addStretch()
        right_layout.addLayout(self.puzzle)
        right_layout.addLayout(path_layout)
        right_layout.addLayout(self.results_layout)
        right_layout.addStretch()
        
        # create main layout which include both left and right widgets
        main_layout = QHBoxLayout(main_widget)
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)
        
        set_main_stylesheet(self)
     
    def solve(self):
        input = self.init_state.text()
        
        if not is_valid_input(input) :
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
        self.path = algorithm.path
        
        self.results = {
            'Cost' : algorithm.cost,
            'Running Time' : algorithm.running_time,
            'Depth':  algorithm.depth,
            'Nodes Explored': algorithm.nodes_explored,
            'Directions': get_directions(self.path)
        }
         
        self.current_index = 0
        self.results_layout.update(self.results)
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
        self.puzzle.update(self.current_state)           
               
        
        
       
    
           
   

