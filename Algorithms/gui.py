import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from search_technique import SearchTechnique

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.path = []    
        self.current_index = 0
        self.current_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.puzzle_labels = []
        self.results = {}
        
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
        self.algorithm.addItem("A*")
        
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
        
        self.set_main_stylesheet()
     
    def solve(self):
        init_state = [int(x) for x in self.init_state.text().split(",")]
        
        type = self.algorithm.currentText()
        algorithm = SearchTechnique(type, init_state)
        results = algorithm.solve()
        self.path = results['Path']
        self.current_index = 0
        self.update_result_labels(results)
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
        self.current_state = self.path[self.current_index]
        self.step_label.setText(str(self.current_index))
        self.update_puzzle()
        
    def update_puzzle(self):
        for i, label in enumerate(self.puzzle_labels):
            value = self.current_state[i]
            if value > 0:
                self.set_label_style(label, value)
            else:
                self.set_free_label_style(label)
            str_value = str(value) if value > 0 else ""
            label.setText(str_value)
            
    def create_result_labels(self):
        items = ['Cost', 'Running Time', 'Depth', 'Nodes Explored']
        self.results_layout.addStretch()
        for i in items:
            label = QLabel()
            self.results[i] = label
            self.results_layout.addWidget(label) 
        self.results_layout.addStretch()
               
    def update_result_labels(self, results):
        for i in self.results:
            label = self.results[i]
            label.setText(f'{i} :    {results[i]}')
        
    def set_main_stylesheet(self):
        self.setStyleSheet("""
            * {
                color: #FFFFFF;
                font-size: 16px;   
            }
            QMainWindow {
                background-color: #2D2D30;  
            }
            
            QComboBox, QLineEdit {
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
            font-size: 20px;
            font-weight: bold;
            background-color: #3E3E42;
        """)  
        
    def set_label_style(self, label, value):
        label.setText(str(value))
        label.setStyleSheet("""
            padding: 40px;
            border: 1px solid black;
            font-size: 20px;
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
