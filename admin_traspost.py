# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt, QDate
# from functions import  table_style,line_edit_style_rounded, tab_style

# class Admin_transport(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         # Main layout
#         layout = QVBoxLayout()
#         layout.setContentsMargins(10, 10, 10, 10)

#         # Header
#         header = QLabel("Admin Panel - Public Transport Management")
#         header.setAlignment(Qt.AlignCenter)
#         header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
#         layout.addWidget(header)

#         # Tabs for Route Management, Booking Management, and Reports
#         self.tab_widget = QTabWidget()
#         self.tab_widget.setStyleSheet(tab_style())

#         self.init_route_management_tab()
#         self.init_booking_management_tab()
#         self.init_reports_tab()

#         layout.addWidget(self.tab_widget)
#         self.setLayout(layout)

#     def init_route_management_tab(self):
#         """Initialize the Route Management tab."""
#         route_tab = QWidget()
#         layout = QVBoxLayout(route_tab)

#         # Add New Route Button
#         add_route_button = QPushButton("Add New Route")
#         add_route_button.clicked.connect(self.add_route)
#         layout.addWidget(add_route_button)

#         # Filters and Sorters
#         filter_layout = QHBoxLayout()

#         self.city_filter_input = QLineEdit()
#         self.city_filter_input.setPlaceholderText("Filter by City")
#         self.city_filter_input.textChanged.connect(self.filter_routes)
#         filter_layout.addWidget(self.city_filter_input)

#         self.destination_filter_input = QLineEdit()
#         self.destination_filter_input.setPlaceholderText("Filter by Destination")
#         self.destination_filter_input.textChanged.connect(self.filter_routes)
#         filter_layout.addWidget(self.destination_filter_input)

#         self.sort_time_button = QPushButton("Sort by Time")
#         self.sort_time_button.clicked.connect(self.sort_routes_by_time)
#         filter_layout.addWidget(self.sort_time_button)

#         layout.addLayout(filter_layout)

#         # Table for existing routes
#         self.route_table = QTableWidget()
#         self.route_table.setColumnCount(6)
#         self.route_table.setStyleSheet(table_style())
#         self.route_table.setHorizontalHeaderLabels(["Source", "Destination", "Date", "Time", "Fare", "Actions"])
#         self.route_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         layout.addWidget(self.route_table)

#         self.tab_widget.addTab(route_tab, "Route Management")

#     def init_booking_management_tab(self):
#         """Initialize the Booking Management tab."""
#         booking_tab = QWidget()
#         layout = QVBoxLayout(booking_tab)

#         # Filters and Sorters
#         filter_layout = QHBoxLayout()

#         self.booking_route_filter_input = QLineEdit()
#         self.booking_route_filter_input.setPlaceholderText("Filter by Route")
#         self.booking_route_filter_input.textChanged.connect(self.filter_bookings)
#         filter_layout.addWidget(self.booking_route_filter_input)

#         self.sort_booking_time_button = QPushButton("Sort by Time")
#         self.sort_booking_time_button.clicked.connect(self.sort_bookings_by_time)
#         filter_layout.addWidget(self.sort_booking_time_button)

#         layout.addLayout(filter_layout)

#         # Table for bookings
#         self.booking_table = QTableWidget()
#         self.booking_table.setColumnCount(5)
#         self.booking_table.setStyleSheet(table_style())
#         self.booking_table.setHorizontalHeaderLabels(["Route", "Date", "Time", "Booked Tickets", "Actions"])
#         self.booking_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         layout.addWidget(self.booking_table)

#         # Button to view booking details
#         self.view_booking_details_button = QPushButton("View Booking Details")
#         self.view_booking_details_button.clicked.connect(self.view_booking_details)
#         layout.addWidget(self.view_booking_details_button)

#         self.tab_widget.addTab(booking_tab, "Booking Management")

#     def init_reports_tab(self):
#         """Initialize the Reports tab."""
#         reports_tab = QWidget()
#         layout = QVBoxLayout(reports_tab)

#         # Revenue Generated
#         revenue_label = QLabel("Total Revenue Generated: $0")
#         revenue_label.setStyleSheet("font-size: 16px; font-weight: bold;")
#         layout.addWidget(revenue_label)

#         # Departed Buses
#         departed_buses_label = QLabel("Total Departed Buses: 0")
#         departed_buses_label.setStyleSheet("font-size: 16px; font-weight: bold;")
#         layout.addWidget(departed_buses_label)

#         # Upcoming Buses
#         upcoming_buses_label = QLabel("Total Upcoming Buses: 0")
#         upcoming_buses_label.setStyleSheet("font-size: 16px; font-weight: bold;")
#         layout.addWidget(upcoming_buses_label)

#         # Report for most popular routes
#         popular_routes_label = QLabel("Most Popular Routes:")
#         popular_routes_label.setStyleSheet("font-size: 16px; font-weight: bold;")
#         layout.addWidget(popular_routes_label)

#         self.popular_routes_table = QTableWidget()
#         self.popular_routes_table.setColumnCount(3)
#         self.popular_routes_table.setStyleSheet(table_style())
#         self.popular_routes_table.setHorizontalHeaderLabels(["Route", "Tickets Sold", "Revenue"])
#         self.popular_routes_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         layout.addWidget(self.popular_routes_table)

#         # Generate Reports Button
#         generate_reports_button = QPushButton("Generate Reports")
#         generate_reports_button.clicked.connect(self.generate_reports)
#         layout.addWidget(generate_reports_button)

#         self.tab_widget.addTab(reports_tab, "Reports")

#     def add_route(self):
#         """Add a new route."""
#         QMessageBox.information(self, "Add Route", "Feature to add a new route.")

#     def filter_routes(self):
#         """Filter routes by city or destination."""
#         city_filter = self.city_filter_input.text().lower()
#         destination_filter = self.destination_filter_input.text().lower()

#         for row in range(self.route_table.rowCount()):
#             source_item = self.route_table.item(row, 0)
#             destination_item = self.route_table.item(row, 1)

#             if source_item and destination_item:
#                 source = source_item.text().lower()
#                 destination = destination_item.text().lower()

#                 match = (city_filter in source) and (destination_filter in destination)
#                 self.route_table.setRowHidden(row, not match)

#     def sort_routes_by_time(self):
#         """Sort routes by time."""
#         self.route_table.sortItems(3)

#     def filter_bookings(self):
#         """Filter bookings by route."""
#         route_filter = self.booking_route_filter_input.text().lower()

#         for row in range(self.booking_table.rowCount()):
#             route_item = self.booking_table.item(row, 0)

#             if route_item:
#                 route = route_item.text().lower()
#                 self.booking_table.setRowHidden(row, route_filter not in route)

#     def sort_bookings_by_time(self):
#         """Sort bookings by time."""
#         self.booking_table.sortItems(2)

#     def view_booking_details(self):
#         """View booking details in a popup."""
#         selected_row = self.booking_table.currentRow()

#         if selected_row == -1:
#             QMessageBox.warning(self, "No Selection", "Please select a booking to view details.")
#             return

#         details = []
#         for col in range(self.booking_table.columnCount()):
#             item = self.booking_table.item(selected_row, col)
#             if item:
#                 details.append(item.text())

#         QMessageBox.information(self, "Booking Details", "\n".join(details))

#     def generate_reports(self):
#         """Generate reports for revenue, departed buses, etc."""
#         # Example report generation logic (placeholder)
#         QMessageBox.information(self, "Reports Generated", "Reports have been successfully generated.")

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     admin_window = Admin_transport()
#     admin_window.setStyleSheet("background-color: #2C3E50; color: white;")
#     admin_window.show()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import  table_style,line_edit_style_rounded, tab_style

class Admin_transport(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        # Header
        header = QLabel("Admin Panel - Public Transport Management")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        layout.addWidget(header)

        # Tabs for Route Management, Booking Management, and Reports
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())

        self.init_route_management_tab()
        self.init_booking_management_tab()
        self.init_reports_tab()

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def init_route_management_tab(self):
        """Initialize the Route Management tab."""
        route_tab = QWidget()
        layout = QVBoxLayout(route_tab)

        # Add New Route Button
        add_route_button = QPushButton("Add New Route")
        add_route_button.clicked.connect(self.add_route)
        layout.addWidget(add_route_button)

        # Filters and Sorters
        filter_layout = QHBoxLayout()

        self.city_filter_dropdown = QComboBox()
        self.city_filter_dropdown.addItems(["All", "City A", "City B", "City C"])
        self.city_filter_dropdown.setStyleSheet(line_edit_style_rounded())
        filter_layout.addWidget(QLabel("City:"))
        filter_layout.addWidget(self.city_filter_dropdown)

        self.destination_filter_dropdown = QComboBox()
        self.destination_filter_dropdown.addItems(["All", "City X", "City Y", "City Z"])
        self.destination_filter_dropdown.setStyleSheet(line_edit_style_rounded())
        filter_layout.addWidget(QLabel("Destination:"))
        filter_layout.addWidget(self.destination_filter_dropdown)

        self.apply_filter_button = QPushButton("Apply Filter")
        self.apply_filter_button.clicked.connect(self.filter_routes)
        filter_layout.addWidget(self.apply_filter_button)

        self.sort_time_button = QPushButton("Sort by Time")
        self.sort_time_button.clicked.connect(self.sort_routes_by_time)
        filter_layout.addWidget(self.sort_time_button)

        layout.addLayout(filter_layout)

        # Table for existing routes
        self.route_table = QTableWidget()
        self.route_table.setColumnCount(6)
        self.route_table.setStyleSheet(table_style())
        self.route_table.setHorizontalHeaderLabels(["Source", "Destination", "Date", "Time", "Fare", "Actions"])
        self.route_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.route_table)

        self.tab_widget.addTab(route_tab, "Route Management")

    def init_booking_management_tab(self):
        """Initialize the Booking Management tab."""
        booking_tab = QWidget()
        layout = QVBoxLayout(booking_tab)

        # Filters and Sorters
        filter_layout = QHBoxLayout()

        self.booking_route_dropdown = QComboBox()
        self.booking_route_dropdown.addItems(["All", "Route 1", "Route 2", "Route 3"])
        self.booking_route_dropdown.setStyleSheet(line_edit_style_rounded())
        filter_layout.addWidget(QLabel("Route:"))
        filter_layout.addWidget(self.booking_route_dropdown)

        self.apply_booking_filter_button = QPushButton("Apply Filter")
        self.apply_booking_filter_button.clicked.connect(self.filter_bookings)
        filter_layout.addWidget(self.apply_booking_filter_button)

        self.sort_booking_time_button = QPushButton("Sort by Time")
        self.sort_booking_time_button.clicked.connect(self.sort_bookings_by_time)
        filter_layout.addWidget(self.sort_booking_time_button)

        layout.addLayout(filter_layout)

        # Table for bookings
        self.booking_table = QTableWidget()
        self.booking_table.setColumnCount(5)
        self.booking_table.setStyleSheet(table_style())
        self.booking_table.setHorizontalHeaderLabels(["Route", "Date", "Time", "Booked Tickets", "Actions"])
        self.booking_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.booking_table)

        # Button to view booking details
        self.view_booking_details_button = QPushButton("View Booking Details")
        self.view_booking_details_button.clicked.connect(self.view_booking_details)
        layout.addWidget(self.view_booking_details_button)

        self.tab_widget.addTab(booking_tab, "Booking Management")

    def init_reports_tab(self):
        """Initialize the Reports tab."""
        reports_tab = QWidget()
        layout = QVBoxLayout(reports_tab)

        # Revenue Generated
        revenue_label = QLabel("Total Revenue Generated: $0")
        revenue_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(revenue_label)

        # Departed Buses
        departed_buses_label = QLabel("Total Departed Buses: 0")
        departed_buses_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(departed_buses_label)

        # Upcoming Buses
        upcoming_buses_label = QLabel("Total Upcoming Buses: 0")
        upcoming_buses_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(upcoming_buses_label)

        # Report for most popular routes
        popular_routes_label = QLabel("Most Popular Routes:")
        popular_routes_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(popular_routes_label)

        self.popular_routes_table = QTableWidget()
        self.popular_routes_table.setColumnCount(3)
        self.popular_routes_table.setStyleSheet(table_style())
        self.popular_routes_table.setHorizontalHeaderLabels(["Route", "Tickets Sold", "Revenue"])
        self.popular_routes_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.popular_routes_table)

        # Generate Reports Button
        generate_reports_button = QPushButton("Generate Reports")
        generate_reports_button.clicked.connect(self.generate_reports)
        layout.addWidget(generate_reports_button)

        self.tab_widget.addTab(reports_tab, "Reports")

    def add_route(self):
        """Add a new route."""
        QMessageBox.information(self, "Add Route", "Feature to add a new route.")

    def filter_routes(self):
        """Filter routes by city or destination."""
        city_filter = self.city_filter_dropdown.currentText().lower()
        destination_filter = self.destination_filter_dropdown.currentText().lower()

        for row in range(self.route_table.rowCount()):
            source_item = self.route_table.item(row, 0)
            destination_item = self.route_table.item(row, 1)

            if source_item and destination_item:
                source = source_item.text().lower()
                destination = destination_item.text().lower()

                match = ((city_filter == "all" or city_filter in source) and
                         (destination_filter == "all" or destination_filter in destination))
                self.route_table.setRowHidden(row, not match)

    def sort_routes_by_time(self):
        """Sort routes by time."""
        self.route_table.sortItems(3)

    def filter_bookings(self):
        """Filter bookings by route."""
        route_filter = self.booking_route_dropdown.currentText().lower()

        for row in range(self.booking_table.rowCount()):
            route_item = self.booking_table.item(row, 0)

            if route_item:
                route = route_item.text().lower()
                self.booking_table.setRowHidden(row, route_filter != "all" and route_filter not in route)

    def sort_bookings_by_time(self):
        """Sort bookings by time."""
        self.booking_table.sortItems(2)

    def view_booking_details(self):
        """View booking details in a popup."""
        selected_row = self.booking_table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a booking to view details.")
            return

        details = []
        for col in range(self.booking_table.columnCount()):
            item = self.booking_table.item(selected_row, col)
            if item:
                details.append(item.text())

        QMessageBox.information(self, "Booking Details", "\n".join(details))

    def generate_reports(self):
        """Generate reports for revenue, departed buses, etc."""
        # Example report generation logic (placeholder)
        QMessageBox.information(self, "Reports Generated", "Reports have been successfully generated.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    admin_window = Admin_transport()
    admin_window.setStyleSheet("background-color: #2C3E50; color: white;")
    admin_window.show()
    sys.exit(app.exec_())
