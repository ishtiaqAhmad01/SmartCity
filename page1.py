from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from page1_form import AddComplaintDialog
from user_database import delete_complaint_from_db


class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout for the page
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        
        top_bar = QHBoxLayout()
        title = QLabel("Complaint Management")
        title.setStyleSheet("font-size: 24px; color: white; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        add_btn = QPushButton("Add New Complaint")
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 8px 15px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        add_btn.clicked.connect(self.add_new_complaint)  # Connect button to its function

        
        top_bar.addStretch()
        top_bar.addWidget(add_btn)

        # Table for displaying previous complaints
        self.complaint_table = QTableWidget()
        self.complaint_table.setColumnCount(4)
        self.complaint_table.setHorizontalHeaderLabels(["Complaint ID", "Description", "Status", "Action"])
        self.complaint_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.complaint_table.setStyleSheet("""
            QTableWidget {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                border-radius: 10px;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #3498DB;
                color: white;
                font-weight: bold;
                border: 1px solid #2980B9;
                padding: 5px;
            }
        """)
        self.complaint_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Load initial placeholder data
        self.load_complaints()

        # Add widgets to the layout
        layout.addLayout(top_bar)
        layout.addWidget(self.complaint_table)
        self.setLayout(layout)

    def add_new_complaint(self): 
        dialog = AddComplaintDialog()
        if dialog.exec_() == QDialog.Accepted:
            main_category, sub_category, description, address = dialog.get_data()
            QMessageBox.information(self, "Complaint Added", f"Complaint Details:\nCategory: {main_category}\nSubcategory: {sub_category}\nDescription: {description}\nAddress: {address}")
            
            self.load_complaints()

    def load_complaints(self):
        data = [
            [1, "Street light not working", "Pending"],
            [2, "Potholes on main road", "Resolved"],
            [3, "Garbage collection delayed", "Pending"],
        ]
        self.complaint_table.setRowCount(len(data))
        for row, complaint in enumerate(data):
            for col, value in enumerate(complaint):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.complaint_table.setItem(row, col, item)

            status = complaint[2]
            btn = QPushButton("")

            if status == "Pending":
                btn.setText("Cancel")
                btn.setStyleSheet(self.btn_style("#E74C3C","#C0392B"))
            elif status == "Resolved":
                btn.setText("Feedback")
                btn.setStyleSheet(self.btn_style("#27AE60","#229954"))
            btn.clicked.connect(lambda _, r=row: self.btn_action(r))
            self.complaint_table.setCellWidget(row, 3, btn)

    def btn_style(self, color, hover_color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """
    
    def btn_action(self, row):
        complaint_id = self.complaint_table.item(row, 0).text()
        complaint_status = self.complaint_table.item(row, 2).text()

        if complaint_status == "Pending":
            QMessageBox.information(self, "Cancel Action", f"Cancel action for Complaint ID: {complaint_id}")
            delete_complaint_from_db(complaint_id)
            
        elif complaint_status == "Resolved":
            QMessageBox.information(self, "Feedback Action", f"Feedback action for Complaint ID: {complaint_id}")

