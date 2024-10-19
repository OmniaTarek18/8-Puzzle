# 8-Puzzle

the hierarchy of the GUI
 main_widget 
         |_ main_layout (QHBoxLayout)
                 |_ left_widget 
                 |        |_ left_layout (QVBoxLayout)
                 |                |_ init_state_label (QLabel)
                 |                |_ init_state       (QLineEdit)
                 |                |_ algorithm_label  (QLabel)
                 |                |_ algorithm        (QComboBox)
                 |                |_ solve_button     (QPushButton)
                 |_ right_widget 
                          |_ right_layout (QVBoxLayout)
                                  |_ puzzle_layout  (QGridLayout)
                                  |       |_ 9 labels (QLabel)
                                  |_ path_layout    (QHBoxLayout)
                                  |       |_ prev       (QPushButton)
                                  |       |_ step_label (QLabel)                 
                                  |       |_ next       (QPushButton)
                                  |_ results_layout (QHBoxLayout)
                                          |_ 4 labels (QLabel)     