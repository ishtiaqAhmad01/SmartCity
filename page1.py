from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from page1_form import AddComplaintDialog
from user_database import delete_complaint_from_db, insert_complain_to_db,load_complains_from_db, add_review_of_complain
from functions import table_style
import globals
from feedback import FeedbackDialog




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
        self.complaint_table.setStyleSheet(table_style())
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
            if insert_complain_to_db(globals.get_user_id(), main_category, sub_category, description, address):
                QMessageBox.information(self, "Complaint Added", f"Complaint Details:\nCategory: {main_category}\nSubcategory: {sub_category}\nDescription: {description}\nAddress: {address}")
                self.load_complaints()
            else:
                QMessageBox.critical(self, "Error", "There Was Error While Inserting Complain")
        
    def load_complaints(self):
        data = load_complains_from_db(globals.get_user_id())
        self.complaint_table.setRowCount(len(data))

        if len(data)==0:
            return

        for row, complaint in enumerate(data):
            for col, value in enumerate(complaint):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.complaint_table.setItem(row, col, item)

            status = complaint[2]
            btn = QPushButton("")

            if status == "pending":
                btn.setText("Cancel")
                btn.setStyleSheet(self.btn_style("#E74C3C","#C0392B"))
            elif status == "resolved":
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

        print(complaint_status)

        if complaint_status == "pending":
            QMessageBox.information(self, "Cancel Action", f"Cancel action for Complaint ID: {complaint_id}")
            if delete_complaint_from_db(complaint_id):
                QMessageBox.information(self, "Success", "Complain has been removed.")
            else:
                QMessageBox.critical(self, "Error", "Complain can not be removed, Try Again.")
            
        elif complaint_status == "resolved":
            feedback_dialog = FeedbackDialog()
            if feedback_dialog.exec_() == QDialog.Accepted:
                feedback, rating = feedback_dialog.get_feedback()
                add_review_of_complain(complaint_id, feedback, rating)
                delete_complaint_from_db(complaint_id) # also delete as we have provided feedback
                QMessageBox.information(self, "Success", "Your feedback has been submitted.")
        
        self.load_complaints()
