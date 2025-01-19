from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import table_style, tab_style

class AdminAppointmentManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        # Header
        header = QLabel("Admin Panel - Appointment Management")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(header)

        # Tab Widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())

        # Initialize Tabs
        self.init_appointment_management_tab()
        self.init_appointment_history_tab()
        self.init_reports_tab()

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def init_appointment_management_tab(self):
        """Initialize the Appointment Management tab."""
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

        # Add Manage Appointment tab to the tab widget
        self.tab_widget.addTab(management_tab, "Manage Appointments")

    def init_appointment_history_tab(self):
        """Initialize the Appointment History tab."""
        history_tab = QWidget()
        layout = QVBoxLayout(history_tab)

        # Table for Appointment History
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setStyleSheet(table_style())
        self.history_table.setHorizontalHeaderLabels(["Service", "Location", "Date", "Time", "Status", "Actions"])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.history_table)

        # Export History Button
        export_button = QPushButton("Export History")
        export_button.clicked.connect(self.export_history)
        layout.addWidget(export_button)

        # Add Appointment History tab to the tab widget
        self.tab_widget.addTab(history_tab, "Appointment History")

    def init_reports_tab(self):
        """Initialize the Reports tab."""
        reports_tab = QWidget()
        layout = QVBoxLayout(reports_tab)

        # Total Appointments
        total_appointments_label = QLabel("Total Appointments: 0")
        total_appointments_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(total_appointments_label)

        # Revenue Generated
        revenue_label = QLabel("Total Revenue Generated: $0")
        revenue_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(revenue_label)

        # Feedback Statistics
        feedback_label = QLabel("Feedback Summary: Positive (0), Neutral (0), Negative (0)")
        feedback_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(feedback_label)

        # Most Popular Services
        popular_services_label = QLabel("Most Popular Services:")
        popular_services_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(popular_services_label)

        self.popular_services_table = QTableWidget()
        self.popular_services_table.setColumnCount(2)
        self.popular_services_table.setStyleSheet(table_style())
        self.popular_services_table.setHorizontalHeaderLabels(["Service", "Appointments"])
        self.popular_services_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.popular_services_table)

        # Generate Reports Button
        generate_reports_button = QPushButton("Generate Reports")
        generate_reports_button.clicked.connect(self.generate_reports)
        layout.addWidget(generate_reports_button)

        # Add Reports tab to the tab widget
        self.tab_widget.addTab(reports_tab, "Reports")

    def filter_appointments(self):
        """Filter appointments based on selected criteria."""
        print("Applying filters...")
        pass  # Implement filtering logic

    def sort_appointments(self):
        """Sort appointments by date or time."""
        print("Sorting appointments...")
        pass  # Implement sorting logic

    def export_history(self):
        """Export appointment history to a file."""
        print("Exporting history...")
        pass  # Implement export logic

    def generate_reports(self):
        """Generate and display reports."""
        print("Generating reports...")
        pass  # Implement report generation logic

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    admin_window = AdminAppointmentManagement()
    admin_window.setStyleSheet("background-color: #FFFFFF; color: #333;")
    admin_window.show()
    sys.exit(app.exec_())
