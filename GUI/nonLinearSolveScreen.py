from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontMetrics
from GUI.steps import StepsDisplay
from GUI.matrix_screen import clear_layout

class NonlinearSolveScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.steps = ""
        
        main_layout = QVBoxLayout()
        
        container_layout = QVBoxLayout()

        self.method_label = QLabel("Method:")
        self.method_label.setStyleSheet("color:black;")
        self.method_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(self.method_label)
        container_layout.addWidget(QLabel(" "))

        root_layout = QHBoxLayout()
        self.root_label = QLabel("Root:")
        self.root_label.setStyleSheet("color:black;")
        self.root_field = QLineEdit()
        self.root_field.setReadOnly(True)
        self.root_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.root_field.setStyleSheet("color:black;")
        
        root_layout.addWidget(self.root_label)
        root_layout.addWidget(self.root_field)
        
        font_metrics = QFontMetrics(self.root_field.font())
        text_width = font_metrics.horizontalAdvance(self.root_field.text()) + 30  
        self.root_field.setFixedWidth(text_width)
        
        container_layout.addLayout(root_layout)
        container_layout.addWidget(QLabel(" "))

        execution_time_layout = QHBoxLayout()
        self.execution_time_unit = QLabel("ms")
        self.execution_time_unit.setStyleSheet("color:black;")
        self.execution_time_label = QLabel("Execution Time:")
        self.execution_time_label.setStyleSheet("color:black;")
        self.execution_time_field = QLineEdit()
        self.execution_time_field.setReadOnly(True)
        self.execution_time_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.execution_time_field.setStyleSheet("color:black;")
        
        execution_time_layout.addWidget(self.execution_time_label)
        execution_time_layout.addWidget(self.execution_time_field)
        execution_time_layout.addWidget(self.execution_time_unit)
        
        font_metrics = QFontMetrics(self.execution_time_field.font())
        text_width = font_metrics.horizontalAdvance(self.execution_time_field.text()) + 30  
        self.execution_time_field.setFixedWidth(text_width)
        
        container_layout.addLayout(execution_time_layout)
        container_layout.addWidget(QLabel(" "))

        # Number of Iterations Layout
        iterations_layout = QHBoxLayout()
        self.iterations_label = QLabel("Number of Iterations:")
        self.iterations_label.setStyleSheet("color:black;")
        self.iterations_field = QLineEdit()
        self.iterations_field.setReadOnly(True)
        self.iterations_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.iterations_field.setStyleSheet("color:black;")
        
        iterations_layout.addWidget(self.iterations_label)
        iterations_layout.addWidget(self.iterations_field)
        
        font_metrics = QFontMetrics(self.iterations_field.font())
        text_width = font_metrics.horizontalAdvance(self.iterations_field.text()) + 30  
        self.iterations_field.setFixedWidth(text_width)
        
        container_layout.addLayout(iterations_layout)

        # Significant Figures Layout
        sig_fig_layout = QHBoxLayout()
        self.sig_fig_label = QLabel("Correct Significant Figures:")
        self.sig_fig_label.setStyleSheet("color:black;")
        self.sig_fig_field = QLineEdit()
        self.sig_fig_field.setReadOnly(True)
        self.sig_fig_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sig_fig_field.setStyleSheet("color:black;")
        
        sig_fig_layout.addWidget(self.sig_fig_label)
        sig_fig_layout.addWidget(self.sig_fig_field)
        
        font_metrics = QFontMetrics(self.sig_fig_field.font())
        text_width = font_metrics.horizontalAdvance(self.sig_fig_field.text()) + 30  
        self.sig_fig_field.setFixedWidth(text_width)
        
        container_layout.addLayout(sig_fig_layout)

        # Relative Error Layout
        relative_error_layout = QHBoxLayout()
        self.relative_error_label = QLabel("Relative Error:")
        self.relative_error_label.setStyleSheet("color:black;")
        self.relative_error_field = QLineEdit()
        self.relative_error_field.setReadOnly(True)
        self.relative_error_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.relative_error_field.setStyleSheet("color:black;")
        
        relative_error_layout.addWidget(self.relative_error_label)
        relative_error_layout.addWidget(self.relative_error_field)
        
        font_metrics = QFontMetrics(self.relative_error_field.font())
        text_width = font_metrics.horizontalAdvance(self.relative_error_field.text()) + 30  
        self.relative_error_field.setFixedWidth(text_width)
        
        container_layout.addLayout(relative_error_layout)
        
        container_widget = QWidget()
        container_widget.setLayout(container_layout)
        main_layout.addWidget(container_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.steps_button = QPushButton("Show Steps")
        self.steps_button.clicked.connect(self.show_steps)
        main_layout.addWidget(self.steps_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.error_message = QLabel("")
        self.error_message.setStyleSheet(""" 
            max-width: 650px;
            height: 50px;
            background-color: #439A97;
            color: #F3F7EC;
            border-radius: 5px;
            padding: 10px;
            margin: 15px 0;
            font-size: 30px;
        """)
        self.error_message.setVisible(False)
        main_layout.addWidget(self.error_message, alignment=Qt.AlignmentFlag.AlignCenter)
        
        main_layout.addStretch()

        self.home_button = QPushButton('Home Screen')
        self.home_button.clicked.connect(self.home)
        main_layout.addWidget(self.home_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)

        self.setStyleSheet(""" 
            QWidget{
                font-size: 20px;
                font-family: Arial, sans-serif;
            }
            QLabel{
                font-weight: bold;
                color: #333;
            }
            QLineEdit{
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                min-width: fit-content;
            }
            QPushButton{
                background-color: #439A97;
                color: #F3F7EC;
                border-radius: 5px;
                padding: 10px;
                margin: 15px 0;
                font-size: 20px;
            }
            QPushButton:hover{
                background-color: #62B6B7;
            }
        """)

    def set_solution(self, method, root, execution_time, steps, iterations, significant_figures, relative_error):
        self.steps = steps
        
        if isinstance(root, str) and "No Solution" in root:
            self.error_message.setText(root)
            self.error_message.setVisible(True)
            self.method_label.setVisible(False)
            self.root_field.setVisible(False)
            self.root_label.setVisible(False)
            self.execution_time_field.setVisible(False)
            self.execution_time_label.setVisible(False)
            self.execution_time_unit.setVisible(False)
            self.steps_button.setVisible(False)
            self.iterations_label.setVisible(False)
            self.iterations_field.setVisible(False)
            self.sig_fig_label.setVisible(False)
            self.sig_fig_field.setVisible(False)
            self.relative_error_label.setVisible(False)
            self.relative_error_field.setVisible(False)
            return
        else:
            self.error_message.setVisible(False)
            self.method_label.setVisible(True)
            self.root_field.setVisible(True)
            self.root_label.setVisible(True)
            self.execution_time_field.setVisible(True)
            self.execution_time_label.setVisible(True)
            self.execution_time_unit.setVisible(True)
            self.steps_button.setVisible(True)
            self.iterations_label.setVisible(True)
            self.iterations_field.setVisible(True)
            self.sig_fig_label.setVisible(True)
            self.sig_fig_field.setVisible(True)
            self.relative_error_label.setVisible(True)
            self.relative_error_field.setVisible(True)

        self.method_label.setText(f"Selected method: {method}")
        self.root_field.setText(f"{root}")
        
        font_metrics = QFontMetrics(self.root_field.font())
        text_width = font_metrics.horizontalAdvance(f"{root}") + 30
        self.root_field.setFixedWidth(text_width)
        
        self.execution_time_field.setText(f"{execution_time / 1000:.6f}")
        font_metrics = QFontMetrics(self.execution_time_field.font())
        text_width = font_metrics.horizontalAdvance(f"{execution_time / 1000:.6f}") + 30
        self.execution_time_field.setFixedWidth(text_width)

        self.iterations_field.setText(f"{iterations}")
        font_metrics = QFontMetrics(self.iterations_field.font())
        text_width = font_metrics.horizontalAdvance(f"{iterations}") + 30
        self.iterations_field.setFixedWidth(text_width)

        self.sig_fig_field.setText(f"{significant_figures}")
        font_metrics = QFontMetrics(self.sig_fig_field.font())
        text_width = font_metrics.horizontalAdvance(f"{significant_figures}") + 30
        self.sig_fig_field.setFixedWidth(text_width)

        self.relative_error_field.setText(f"{relative_error:.6e}")
        font_metrics = QFontMetrics(self.relative_error_field.font())
        text_width = font_metrics.horizontalAdvance(f"{relative_error:.6e}") + 30
        self.relative_error_field.setFixedWidth(text_width)

    def home(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_steps(self):
        step_dialog = StepsDisplay(self.steps)
        step_dialog.exec()

