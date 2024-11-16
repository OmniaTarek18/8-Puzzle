from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Results(QVBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.results_labels = {}
        items = ['Cost', 'Running Time', 'Depth', 'Nodes Explored', 'Directions']
        self.addStretch()
        for i in items:
            label = QLabel()
            label.setWordWrap(True)
            self.results_labels[i] = label
            self.addWidget(label) 
        self.addStretch()

    def update(self, results):
        for i in self.results_labels:
            label = self.results_labels[i]
            label.setText(f'{i} :    {results[i]}')