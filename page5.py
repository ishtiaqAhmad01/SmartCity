import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class UtilityBillManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Utility Bill Management")
        self.setGeometry(300, 100, 1000, 600)
        self.setStyleSheet("background-color: #2C3E50; color: white;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel("Utility Bill Management")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #FFFFFF;")
        header.setFont(QFont("Arial", 20))
        main_layout.addWidget(header)

        # Tabs for Current and Previous Bills
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #C0C0C0;
                background: #F0F0F0;
                border-radius: 10px;
            }
            QTabBar::tab {
                background: #3498DB;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                margin: 2px;
                width: 200px;
            }
            QTabBar::tab:selected {
                background: #2980B9;
                font-weight: bold;
            }
        """)

        # Current Bills Tab
        self.current_bills_tab = QWidget()
        self.init_current_bills_tab()

        # Previous Bills Tab
        self.previous_bills_tab = QWidget()
        self.init_previous_bills_tab()

        self.tabs.addTab(self.current_bills_tab, "Current Bills")
        self.tabs.addTab(self.previous_bills_tab, "Previous Bills")

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def init_current_bills_tab(self):
        layout = QVBoxLayout()

        # Filter Section
        filter_layout = QHBoxLayout()
        category_label = QLabel("Filter by Category:")
        category_label.setFont(QFont("Arial", 14))
        filter_layout.addWidget(category_label)

        self.filter_dropdown = QComboBox()
        self.filter_dropdown.addItems(["All", "Electricity", "Water", "Gas", "Internet"])
        self.filter_dropdown.setStyleSheet("padding: 5px; border-radius: 5px; background-color: #34495E; color: white;")
        self.filter_dropdown.currentIndexChanged.connect(self.filter_bills)
        filter_layout.addWidget(self.filter_dropdown)

        layout.addLayout(filter_layout)

        # Bill Table
        self.current_bill_table = QTableWidget()
        self.current_bill_table.setColumnCount(4)
        self.current_bill_table.setHorizontalHeaderLabels(["Category", "Amount", "Due Date", "Download"])
        self.current_bill_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.current_bill_table.setStyleSheet("background-color: #ECF0F1; border-radius: 10px;")
        self.current_bill_table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.current_bill_table)

        # Load Sample Data for Current Bills
        self.load_current_bills_data()

        self.current_bills_tab.setLayout(layout)

    def init_previous_bills_tab(self):
        layout = QVBoxLayout()

        # Filter Section
        filter_layout = QHBoxLayout()
        category_label = QLabel("Filter by Category:")
        category_label.setFont(QFont("Arial", 14))
        filter_layout.addWidget(category_label)

        self.previous_filter_dropdown = QComboBox()
        self.previous_filter_dropdown.addItems(["All", "Electricity", "Water", "Gas", "Internet"])
        self.previous_filter_dropdown.setStyleSheet("padding: 5px; border-radius: 5px; background-color: #34495E; color: white;")
        self.previous_filter_dropdown.currentIndexChanged.connect(self.filter_previous_bills)
        filter_layout.addWidget(self.previous_filter_dropdown)

        layout.addLayout(filter_layout)

        # Bill Table for Previous Bills
        self.previous_bill_table = QTableWidget()
        self.previous_bill_table.setColumnCount(4)
        self.previous_bill_table.setHorizontalHeaderLabels(["Category", "Amount", "Paid Date", "Download"])
        self.previous_bill_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.previous_bill_table.setStyleSheet("background-color: #ECF0F1; border-radius: 10px;")
        self.previous_bill_table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.previous_bill_table)

        # Load Sample Data for Previous Bills
        self.load_previous_bills_data()

        self.previous_bills_tab.setLayout(layout)

    def load_current_bills_data(self):
        sample_data = [
            ["Electricity", "$120", "2025-01-15"],
            ["Water", "$45", "2025-01-20"],
            ["Gas", "$70", "2025-01-25"]
        ]

        self.current_bill_table.setRowCount(len(sample_data))
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                self.current_bill_table.setItem(row, col, item)

            download_button = QPushButton("Download")
            download_button.setStyleSheet(self.button_style())
            download_button.clicked.connect(lambda _, r=row: self.download_bill(r, "current"))
            self.current_bill_table.setCellWidget(row, 3, download_button)

    def load_previous_bills_data(self):
        sample_data = [
            ["Electricity", "$110", "2024-12-15"],
            ["Water", "$40", "2024-12-20"],
            ["Gas", "$65", "2024-12-25"]
        ]

        self.previous_bill_table.setRowCount(len(sample_data))
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                self.previous_bill_table.setItem(row, col, item)

            download_button = QPushButton("Download")
            download_button.setStyleSheet(self.button_style())
            download_button.clicked.connect(lambda _, r=row: self.download_bill(r, "previous"))
            self.previous_bill_table.setCellWidget(row, 3, download_button)

    def filter_bills(self):
        filter_category = self.filter_dropdown.currentText()
        QMessageBox.information(self, "Filter Applied", f"Filtering current bills by category: {filter_category}")

    def filter_previous_bills(self):
        filter_category = self.previous_filter_dropdown.currentText()
        QMessageBox.information(self, "Filter Applied", f"Filtering previous bills by category: {filter_category}")

    def download_bill(self, row, bill_type):
        QMessageBox.information(self, "Download Bill", f"Downloading bill from {bill_type} list, row: {row + 1}")

    def button_style(self):
        return """
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UtilityBillManagement()
    window.show()
    sys.exit(app.exec_())
