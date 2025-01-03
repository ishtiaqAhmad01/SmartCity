import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sidebar Navigation Example")
        self.setGeometry(300, 100, 1400, 900)
        self.setStyleSheet("background-color: #2C3E50;")

        # Create the main layout
        main_layout = QHBoxLayout(self)

        # Create the sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addLayout(self.sidebar, 1)

        # Create the content area (stacked widget for changing content)
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("background-color: #34495E; border-radius: 10px;")

        # Add placeholder pages to the content area
        for i in range(1, 8):
            placeholder = QLabel(f"Content for Page {i}")
            placeholder.setAlignment(Qt.AlignCenter)
            placeholder.setStyleSheet("color: white; font-size: 20px;")
            self.content_area.addWidget(placeholder)

        main_layout.addWidget(self.content_area, 4)
        self.setLayout(main_layout)

    def create_sidebar(self):
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)

        # Create 7 buttons for the sidebar
        for i in range(1, 8):
            button = QPushButton(f"Page {i}")
            button.setStyleSheet(self.sidebar_button_style())
            button.clicked.connect(lambda _, page=i: self.show_content(page))  # Connect to the content display function
            sidebar_layout.addWidget(button)

        return sidebar_layout

    def sidebar_button_style(self):
        return """
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """

    def show_content(self, page):
        """
        Switch to the specified page in the content area.
        :param page: The index of the page to show (1-7).
        """
        self.content_area.setCurrentIndex(page - 1)

# Main entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
