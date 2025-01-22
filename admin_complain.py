from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from functions import majorProblem_to_subProblem, table_style
from database import get_feedback, get_comlpains, update_complain_status

class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout for the page
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        # Title for the page
        title = QLabel("Admin - Complaint Management")
        title.setStyleSheet("font-size: 24px; color: white; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Table for displaying complaints
        self.complaint_table = QTableWidget()
        self.complaint_table.setColumnCount(5)
        self.complaint_table.setHorizontalHeaderLabels(["Complaint ID", "Category", "Description", "Status", "Action"])
        self.complaint_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.complaint_table.setStyleSheet(table_style())
        self.complaint_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Load initial placeholder data
        self.load_complaints()

        # Add widgets to the layout
        layout.addWidget(self.complaint_table)
        self.setLayout(layout)

    def load_complaints(self):
        data = get_comlpains()
        print(data)
        if len(data)==0:
            self.complaint_table.setRowCount(0)
            return
            
        


        self.complaint_table.setRowCount(len(data))
        for row, complaint in enumerate(data):
            for col, value in enumerate(complaint):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.complaint_table.setItem(row, col, item)

            status = complaint[3]
            btn = QPushButton("Action")

            if status == "pending":
                btn.setText("Resolve")
                btn.setStyleSheet(self.btn_style("#eb4034"," #bf342a"))
            else:
                btn.setText("Feedback")
                btn.setStyleSheet(self.btn_style("#27AE60","#229954"))
            
            btn.clicked.connect(lambda _, r=row: self.btn_action(r))
            self.complaint_table.setCellWidget(row, 4, btn)

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
        complaint_status = self.complaint_table.item(row, 3).text()

        if complaint_status == "pending":
            self.resolve_complaint(complaint_id)
        else:
            self.show_feedback(complaint_id)

    def resolve_complaint(self, complaint_id):
        update_complain_status(complaint_id)
        QMessageBox.information(self, "Complaint Resolved", f"Complaint ID: {complaint_id} has been resolved.")
        self.load_complaints()

    def show_feedback(self, complaint_id):
        feedback = get_feedback('complain', complaint_id)
        print(complaint_id)
        if feedback:
            text, rating, date = feedback
            QMessageBox.information(self, "FeedBack", f" Review : {text} \n {'⭐'*rating} \n Date : {date}")
        else:
            QMessageBox.information(self, "Feedback", "")
        

