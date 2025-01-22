from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class BaseDashboard(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 1400, 900)
        self.setStyleSheet("background-color: #2C3E50;")

        # Main Layout
        self.page_widgets = {}  
        self.sidebar_buttons = []  
        main_layout = QHBoxLayout()

        # Sidebar and content area
        self.sidebar_layout = QVBoxLayout()
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("background-color: #34495E; border-radius: 10px;")

        # Create sidebar widget
        self.create_sidebar()

        # Set layout
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(self.sidebar_layout)
        main_layout.addWidget(sidebar_widget, 1)
        main_layout.addWidget(self.content_area, 4)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_sidebar(self):
        """Create sidebar layout with dynamic buttons."""
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.sidebar_layout.setContentsMargins(10, 10, 10, 10)

        # Logout button
        logout_button = QPushButton("Logout")
        logout_button.setFixedWidth(150)
        logout_button.clicked.connect(self.logout)
        logout_button.setStyleSheet('''
            QPushButton {
                background-color: #E74C3C;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
                margin-left: 65px;
            }
        ''')
        self.sidebar_layout.addStretch()
        self.sidebar_layout.addWidget(logout_button)

    def add_page(self, label, widget):
        """Add a new page to the dashboard."""
        button = QPushButton(label)
        button.setStyleSheet(self.sidebar_button_style())
        button.clicked.connect(lambda: self.show_content(label))

        # Add button to sidebar and widget to content area
        self.sidebar_layout.insertWidget(len(self.sidebar_buttons), button)
        self.sidebar_buttons.append(button)
        self.content_area.addWidget(widget)

        # Track the page widget by its label
        self.page_widgets[label] = widget

    def show_content(self, label):
        """Show the page corresponding to the label."""
        widget = self.page_widgets[label]
        self.content_area.setCurrentWidget(widget)

    def sidebar_button_style(self):
        """Styles for sidebar buttons."""
        return """
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """

    def logout(self):
        """Handle logout."""
        QMessageBox.information(self, "Logout", "You have been logged out successfully!")
        


