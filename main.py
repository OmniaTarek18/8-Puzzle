import sys
from GUI.main_window import MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == "__main__":       
    # Application initialization
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())