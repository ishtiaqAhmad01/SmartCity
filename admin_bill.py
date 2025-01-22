from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
import sys
from functions import table_style, tab_style, line_edit_style_rounded, spin_box_style, send_bill_email
from database import get_user_info, add_user_bill, get_bill_info
from pdf import generate_utility_bill_pdf


class BillManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create tab widget
        self.setStyleSheet("font-size:20px; ")
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(tab_style())


        # Add tabs
        self.tabs.addTab(self.create_add_bill_tab(), "Add New Bill")
        self.tabs.addTab(self.create_search_bills_tab(), "Search Bills")
        self.tabs.addTab(self.create_reports_tab(), "Reports")

        # Set layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
    
    def create_add_bill_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        # Bill Type Selection
        self.bill_type_dropdown = QComboBox()
        self.bill_type_dropdown.addItems(["Electric", "Gas", "Internet", "Water"])

        # CNIC Input
        self.cnic_input = QLineEdit()
        self.cnic_input.setStyleSheet(line_edit_style_rounded())
        self.cnic_input.setPlaceholderText("Enter CNIC")
        self.fetch_data_button = QPushButton("Fetch Data")
        self.fetch_data_button.clicked.connect(self.fetch_user_data)

        # Labels for fetched name and address
        self.name_label = QLabel("Name: ")
        self.name_label.setStyleSheet("color:white;")
        self.address_label = QLabel("Address: ")
        self.address_label.setStyleSheet("color:white;")

        # Date Pickers
        self.issue_date_picker = QDateEdit()
        self.issue_date_picker.setCalendarPopup(True)
        self.issue_date_picker.setDate(QDate.currentDate())
        self.due_date_picker = QDateEdit()
        self.due_date_picker.setCalendarPopup(True)
        self.due_date_picker.setDate(QDate.currentDate().addDays(15))

        # Unit Input Fields
        self.unit_input = QSpinBox()
        self.unit_input.setStyleSheet(spin_box_style())
        self.unit_input.setRange(0, 10000)

        # Price per Unit and Tax
        self.unit_price_input = QDoubleSpinBox()
        self.unit_price_input.setStyleSheet(spin_box_style())
        self.unit_price_input.setRange(0, 10000)
        self.unit_price_input.setPrefix("Rs ")

        self.tax_input = QDoubleSpinBox()
        self.tax_input.setStyleSheet(spin_box_style())
        self.tax_input.setRange(0, 100)
        self.tax_input.setSuffix(" %")

        # Amount Fields
        self.amount_before_due_label = QLabel("Rs 0")
        self.amount_after_due_label = QLabel("Rs 0")

        self.add_bill_btn = QPushButton("Add Bill")
        self.add_bill_btn.clicked.connect(self.add_bill)

        form_layout.addRow("Bill Type:", self.bill_type_dropdown)
        form_layout.addRow("CNIC:", self.cnic_input)
        form_layout.addRow("", self.fetch_data_button)
        form_layout.addRow(self.name_label)
        form_layout.addRow(self.address_label)
        form_layout.addRow("Issue Date:", self.issue_date_picker)
        form_layout.addRow("Due Date:", self.due_date_picker)
        form_layout.addRow("Units Used:", self.unit_input)
        form_layout.addRow("Unit Price:", self.unit_price_input)
        form_layout.addRow("Tax:", self.tax_input)
        form_layout.addRow("Amount Before Due:", self.amount_before_due_label)
        form_layout.addRow("Amount After Due:", self.amount_after_due_label)

        layout.addLayout(form_layout)
        layout.addWidget(self.add_bill_btn)
        tab.setLayout(layout)
        return tab

    def create_search_bills_tab(self):
        tab = QWidget()
        main_layout = QVBoxLayout()

        # Dropdown for Bill Type Selection
        bill_type_label = QLabel("Select Bill Type:")
        bill_type_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        bill_type_dropdown = QComboBox()
        bill_type_dropdown.addItems(["Electric", "Gas", "Internet", "Water"])
        bill_type_dropdown.setFixedWidth(200)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Enter User CNIC")
        self.search_field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
            }
        """)

        search_button = QPushButton("Search")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        
        
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(bill_type_label)
        self.search_layout.addWidget(bill_type_dropdown)
        self.search_layout.addWidget(self.search_field)
        self.search_layout.addWidget(search_button)

        
        bill_info_group = QGroupBox("Bill Information")
        bill_info_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                padding-top: 20px;
                margin-top: 10px;
            }
        """)
        
        bill_info_layout = QFormLayout()
        bill_info_layout.setHorizontalSpacing(20)
        bill_info_layout.setVerticalSpacing(15)

        self.bill_details = {
            "User Name": QLineEdit(),
            "Address": QLineEdit(),
            "Email": QLineEdit(),
            "Phone No": QLineEdit(),
            "Tax Percentage": QLineEdit(),
            "Tax Amount": QLineEdit(),
            "Bill Amount": QLineEdit()
        }

       
        for label, field in self.bill_details.items():
            field.setReadOnly(True)
            bill_info_layout.addRow(QLabel(label), field)
        
        bill_info_group.setLayout(bill_info_layout)
        bill_info_group.setVisible(False)  # Hide by default

        # Save to PDF Button
        save_pdf_button = QPushButton("Save to PDF")
        save_pdf_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        save_pdf_button.clicked.connect(lambda: self.save_searched_pdf())
        save_pdf_button.setVisible(False)  


        main_layout.addLayout(self.search_layout)
        main_layout.addWidget(bill_info_group)
        main_layout.addWidget(save_pdf_button)
        main_layout.addStretch()
        tab.setLayout(main_layout)


        search_button.clicked.connect(lambda: self.display_bill_info(bill_info_group, save_pdf_button))

        return tab

    def display_bill_info(self, group_box, save_button):
        print("called")
        bill_type = self.bill_type_dropdown.currentText()
        cnic = self.search_field.text()
        print(cnic)
        data =  get_bill_info(cnic, bill_type)
        print(data)
        if data and len(data)!=0:
            first_name, last_name, email, province, district, city, phone_number ,tax_percentage ,tax_amount  ,amount_before_due, late_fee, issue_date, due_date = data
        else:
            first_name = "NA"
            last_name = "NA"
            email = "NA"
            province = "NA"
            district = "NA"
            city = "NA"
            phone_number = "NA"
            tax_percentage = "NA"
            tax_amount = "NA"
            amount_before_due = "NA"
        
        self.bill_data = {
            "User Name": first_name +" "+ last_name,
            "Address": f'city : {city} | district : {district} | province : {province}',
            "Email": email,
            "Phone No": phone_number,
            "Tax Percentage": str(tax_percentage),
            "Tax Amount": str(tax_amount),
            "Bill Amount": str(amount_before_due)
        }
        
        for label, field in self.bill_details.items():
            field.setText(self.bill_data[label])

        # Show data and save button
        group_box.setVisible(True)
        save_button.setVisible(True)

    def create_reports_tab(self): # TBD
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        return tab

    def fetch_user_data(self):
        cnic = self.cnic_input.text()
        if cnic:
            data = get_user_info(cnic)
            if data and len(data)!=0:
                first_name, last_name, province, district, city, self.user_email = data
                # Simulate fetching user data
                self.name_label.setText(f"Name: {first_name} {last_name} (for CNIC: {cnic})")
                self.address_label.setText(f"Address: {city} {district}, {province}")
                return
            
        
        self.name_label.setText("Name: ")
        self.address_label.setText("Address: ")

    def add_bill(self):
        bill_type = self.bill_type_dropdown.currentText()
        cnic = self.cnic_input.text()
        issue_date = self.issue_date_picker.date().toString("yyyy-MM-dd")
        due_date = self.due_date_picker.date().toString("yyyy-MM-dd")
        units = self.unit_input.value()
        unit_price = self.unit_price_input.value()
        tax_percentage = self.tax_input.value()

        if not (bill_type or cnic or issue_date or due_date or units or unit_price or tax_percentage):
            QMessageBox.critical(self, "Error", "Please Enter All deatials.")
            return

        amount_before_due = units * unit_price
        tax_amount = tax_percentage * amount_before_due
        amount_before_due += tax_amount
        
        late_fee = 0.1 * amount_before_due  # 1% incement on current ammount
        amount_after_due = amount_before_due + late_fee

        
        self.amount_before_due_label.setText(f"Rs {amount_before_due:.2f}")
        self.amount_after_due_label.setText(f"Rs {amount_after_due:.2f}")
            
        if add_user_bill(cnic, bill_type, issue_date, amount_before_due, amount_after_due, due_date, tax_percentage,tax_amount,late_fee):
            bill_info = {
                "user_cnic": cnic,
                "bill_type": bill_type,
                "issue_date": issue_date,
                "due_date": due_date,
                "amount_before_due": amount_before_due,
                "tax_percentage": '1', 
                "tax_amount": tax_amount, 
                "late_fee": late_fee,   
                "amount_after_due": amount_after_due
            }
            
            generate_utility_bill_pdf('utility_bill.pdf', bill_info)
            send_bill_email(self.user_email,'utility_bill.pdf',bill_info)
            QMessageBox.information(self, "Success", "Bill is added Successfully")
        else:
            QMessageBox.critical(self, "Error", "Failed to add bill")

    def save_searched_pdf(self):
        cnic = self.search_field.text()
        bill_type = self.bill_type_dropdown.currentText()
        first_name, last_name, email, province, district, city, phone_number ,tax_percentage ,tax_amount  ,amount_before_due, late_fee, issue_date, due_date = get_bill_info(cnic, bill_type)
        bill_info = {
            "user_cnic": cnic,
            "bill_type": bill_type,
            "issue_date": "2025-01-01",
            "due_date": "2025-01-15",
            "amount_before_due": amount_before_due,
            "tax_percentage": tax_percentage, 
            "tax_amount": tax_amount, 
            "late_fee":late_fee,   
            "amount_after_due": amount_before_due + late_fee  
        }
        generate_utility_bill_pdf("searched_bill_pdf.pdf",bill_info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BillManagement()
    window.setWindowTitle("Admin - Bill Management System")
    window.show()
    sys.exit(app.exec_())