from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import table_style, tab_style

class AdminAppointmentManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        header = QLabel("Admin Panel - Appointment Management")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(header)

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())

        self.init_appointment_management_tab()
        self.init_appointment_history_tab()
        self.init_reports_tab()

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def init_appointment_management_tab(self):
        management_tab = QWidget()
        layout = QVBoxLayout(management_tab)

        # Filters and Sorters
        filter_layout = QHBoxLayout()

        self.service_filter_dropdown = QComboBox()
        self.service_filter_dropdown.addItems(["All", "Passport Renewal", "CNIC Issuance", "Driver's License"])
        filter_layout.addWidget(QLabel("Service:"))
        filter_layout.addWidget(self.service_filter_dropdown)

        self.location_filter_dropdown = QComboBox()
        self.location_filter_dropdown.addItems(["All", "City Hall", "Regional Office", "Downtown Office"])
        filter_layout.addWidget(QLabel("Location:"))
        filter_layout.addWidget(self.location_filter_dropdown)

        self.status_filter_dropdown = QComboBox()
        self.status_filter_dropdown.addItems(["All", "Upcoming", "Completed", "Canceled"])
        filter_layout.addWidget(QLabel("Status:"))
        filter_layout.addWidget(self.status_filter_dropdown)

        self.apply_filter_button = QPushButton("Apply Filter")
        self.apply_filter_button.clicked.connect(self.filter_appointments)
        filter_layout.addWidget(self.apply_filter_button)

        self.sort_button = QPushButton("Sort by Date/Time")
        self.sort_button.clicked.connect(self.sort_appointments)
        filter_layout.addWidget(self.sort_button)

        layout.addLayout(filter_layout)

        # Table for Appointment Management
        self.management_table = QTableWidget()
        self.management_table.setColumnCount(6)
        self.management_table.setStyleSheet(table_style())
        self.management_table.setHorizontalHeaderLabels(["Service", "Location", "Date", "Time", "Status", "Actions"])
        self.management_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.management_table)

        self.tab_widget.addTab(management_tab, "Manage Appointments")

    def init_appointment_history_tab(self):
        history_tab = QWidget()
        layout = QVBoxLayout(history_tab)

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setStyleSheet(table_style())
        self.history_table.setHorizontalHeaderLabels(["Service", "Location", "Date", "Time", "Status", "Actions"])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.history_table)

        export_button = QPushButton("Export History")
        export_button.clicked.connect(self.export_history)
        layout.addWidget(export_button)

        self.tab_widget.addTab(history_tab, "Appointment History")

    def init_reports_tab(self):
        reports_tab = QWidget()
        layout = QVBoxLayout(reports_tab)

        total_appointments_label = QLabel("Total Appointments: 0")
        total_appointments_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(total_appointments_label)

        revenue_label = QLabel("Total Revenue Generated: $0")
        revenue_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(revenue_label)

        feedback_label = QLabel("Feedback Summary: Positive (0), Neutral (0), Negative (0)")
        feedback_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(feedback_label)

        popular_services_label = QLabel("Most Popular Services:")
        popular_services_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(popular_services_label)

        self.popular_services_table = QTableWidget()
        self.popular_services_table.setColumnCount(2)
        self.popular_services_table.setStyleSheet(table_style())
        self.popular_services_table.setHorizontalHeaderLabels(["Service", "Appointments"])
        self.popular_services_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.popular_services_table)

        generate_reports_button = QPushButton("Generate Reports")
        generate_reports_button.clicked.connect(self.generate_reports)
        layout.addWidget(generate_reports_button)

        self.tab_widget.addTab(reports_tab, "Reports")

    def filter_appointments(self):
        pass

    def sort_appointments(self):
        pass 

    def export_history(self):
        pass 

    def generate_reports(self):
        pass