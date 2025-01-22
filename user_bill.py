import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from functions import table_style, tab_style
from database import load_current_bills_data, get_bill_info, update_bill_status, get_bill_id, insertPayment
from pdf import generate_utility_bill_pdf
from payments import PaymentPopup
import globals

class UtilityBillManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Utility Bill Management")
        self.setGeometry(300, 100, 1000, 600)
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
        self.tabs.setStyleSheet(tab_style())

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
        self.current_bill_table.setStyleSheet(table_style())
        self.current_bill_table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.current_bill_table)

        
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
        self.previous_bill_table.setStyleSheet(table_style())
        self.previous_bill_table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.previous_bill_table)

        self.load_previous_bills_data()

        self.previous_bills_tab.setLayout(layout)

    def load_current_bills_data(self):
        fetched_data = load_current_bills_data(globals.get_user_id(), "pending")

        if not fetched_data or len(fetched_data) == 0:
            return
        
        self.current_bill_table.setRowCount(len(fetched_data))
        for row, data in enumerate(fetched_data):
            bt = QTableWidgetItem(data[0]) # bill type
            dd = QTableWidgetItem(data[1].strftime('%Y-%m-%d'))  # due date
            de = QTableWidgetItem(f"{data[2]:,.2f}")  # bill amount

            self.current_bill_table.setItem(row, 0, bt)
            self.current_bill_table.setItem(row, 1, de)
            self.current_bill_table.setItem(row, 2, dd)

            button_layout = QWidget()
            button_hbox = QHBoxLayout()
            button_hbox.setContentsMargins(0, 0, 0, 0)
            button_layout.setStyleSheet("background-color: #ffffff;")
            button_hbox.setSpacing(5)

            # Download Button
            download_button = QPushButton("Download")
            download_button.setStyleSheet(self.button_style())
            download_button.clicked.connect(lambda _, r=row: self.download_bill(r, "current"))
            button_hbox.addWidget(download_button)

            # Pay Button
            pay_button = QPushButton("Pay")
            pay_button.setStyleSheet("""
                QPushButton {
                    background-color: #eb4034;
                    color: white;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 5px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #bf342a;
                }
            """)
            pay_button.clicked.connect(lambda _, r=row: self.pay_bill(r))
            button_hbox.addWidget(pay_button)

            button_layout.setLayout(button_hbox)
            self.current_bill_table.setCellWidget(row, 3, button_layout)

    def pay_bill(self, row):
        popup = PaymentPopup()
        if popup.exec_() == QDialog.Accepted:  
            QMessageBox.information(self, "Succes", "Payment was successful!")
            bill_type = self.current_bill_table.item(row, 0).text()
            cnic = globals.get_user_id()
            id = get_bill_id(cnic, bill_type)[0]
            amount = self.current_bill_table.item(row, 1).text()
            insertPayment(id, amount) # insert in paymnets
            update_bill_status(cnic, bill_type) # marking a bill prevoius

            self.load_current_bills_data()
            self.load_previous_bills_data()
            
        else:
            QMessageBox.critical(self, "Error", "Payment failed.")

    def load_previous_bills_data(self):
        fetched_data = load_current_bills_data(globals.get_user_id(), "paid")

        if not fetched_data or len(fetched_data) == 0:
            return
        self.previous_bill_table.setRowCount(len(fetched_data))
        for row, data in enumerate(fetched_data):
            bt = QTableWidgetItem(data[0]) # bill type
            dd = QTableWidgetItem(data[1].strftime('%Y-%m-%d'))  # due date
            de = QTableWidgetItem(f"{data[2]:,.2f}")  # bill amount

            self.previous_bill_table.setItem(row, 0, bt)
            self.previous_bill_table.setItem(row, 1, de)
            self.previous_bill_table.setItem(row, 2, dd)

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

    def download_bill(self, row, status):
        cnic = globals.get_user_id()
        if status == "current":
            bill_type = self.current_bill_table.item(row, 0).text()
        else:
            bill_type = self.previous_bill_table.item(row, 0).text()
        print(cnic, bill_type)
        data = get_bill_info(cnic, bill_type)
        print(data)
        if data :
            first_name, last_name, email, province, district, city, phone_number ,tax_percentage ,tax_amount  ,amount_before_due, late_fee, issue_date, due_date = data
            bill_info = {
                "user_cnic": cnic,
                "bill_type": bill_type,
                "issue_date": issue_date,
                "due_date": due_date,
                "amount_before_due": amount_before_due,
                "tax_percentage": tax_percentage, 
                "tax_amount": tax_amount, 
                "late_fee":late_fee,   
                "amount_after_due": amount_before_due + late_fee  
            }
            generate_utility_bill_pdf("download_bill_pdf.pdf",bill_info)
    
    def button_style(self):
        return """
            QPushButton {
                background-color: #27AE60;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UtilityBillManagement()
    window.show()
    sys.exit(app.exec_())