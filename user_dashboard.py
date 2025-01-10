import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from page1 import Page1
from page2 import DigitalDocumentStorage
from page3 import PublicTransportBooking
from page4 import AppointmentBooking
from page5 import UtilityBillManagement

class UserMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unified Citizen Services Portal")
        self.setGeometry(200, 100, 1400, 900)
        self.setStyleSheet("background-color: #2C3E50;")

        # Main layout
        main_layout = QHBoxLayout(self)

        # Sidebar for navigation
        self.sidebar = self.create_sidebar()
        main_layout.addLayout(self.sidebar, 1)

        # Content area for pages
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("background-color: #34495E; border-radius: 10px;")
        self.add_pages()

        main_layout.addWidget(self.content_area, 4)
        self.setLayout(main_layout)


    def create_sidebar(self):
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)

        # Navigation buttons with labels and icons
        buttons_info = [
            ("Complaint Management", "complaint_icon.png"),
            ("Transport Booking", "transport_icon.png"),
            ("Utility Bills", "utility_icon.png"),
            ("Appointment Booking", "appointment_icon.png"),
            ("Document Storage", "document_icon.png")
        ]

        for i, (label, icon) in enumerate(buttons_info):
            button = QPushButton(label)
            button.setIcon(QIcon(icon))  # Assuming appropriate icons are available
            button.setStyleSheet(self.sidebar_button_style())
            button.clicked.connect(lambda _, page=i: self.show_content(page))
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
                text-align: left;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """

    def add_pages(self):
        page1 = Page1()
        page5 = DigitalDocumentStorage()
        page2 = PublicTransportBooking()
        page4 = AppointmentBooking()
        page3 = UtilityBillManagement()

        for page in [page1, page2, page3, page4, page5]:
            page.setStyleSheet("font-size: 18px;")
            self.content_area.addWidget(page)

    def show_content(self, page):
        """
        Switch to the specified page in the content area.
        :param page: The index of the page to show (0-4).
        """
        if page < self.content_area.count():
            self.content_area.setCurrentIndex(page)
        else:
            QMessageBox.warning(self, "Navigation Error", "Selected page is not yet implemented.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserMainWindow()
    window.show()
    sys.exit(app.exec_())
