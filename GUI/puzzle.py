from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GUI.Utilities.styles import set_free_label_style, set_label_style

class Puzzle(QGridLayout):
    def __init__(self):
        super().__init__()

        self.init_state = [0,1,2,3,4,5,6,7,8]
        self.puzzle_labels = []
        for i, value in enumerate(self.init_state):
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            if value > 0:
                set_label_style(label, value)  
            else :
                set_free_label_style(label)          
            self.puzzle_labels.append(label)
            self.addWidget(label,(i // 3),(i % 3))
        
    def update(self, state):
        # adding leading 0 if state length = 8 instead of 9
        if len(state) == 8 :
            state = '0' + state
            
        # update the labels with the right number or empty in case of 0
        for i, label in enumerate(self.puzzle_labels):
            value = state[i]
            if int(value) > 0:
                set_label_style(label, value)
            else:
                set_free_label_style(label)
            str_value = value if int(value) > 0 else ""
            label.setText(str_value)