create database UCSP;
use UCSP;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    password_hash VARCHAR(255)
);

CREATE TABLE statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) -- e.g., Pending, In Progress, Resolved
);

CREATE TABLE complaints (
    complaint_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category VARCHAR(100),
    description TEXT,
    location VARCHAR(255),
    status_id INT,
    complaint_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (status_id) REFERENCES statuses(status_id)
);

CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_id INT,
    user_id INT,
    rating INT, -- rating out of 5
    comments TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (complaint_id) REFERENCES complaints(complaint_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE transport_routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(255),
    destination VARCHAR(255),
    schedule_time TIME,
    transport_type VARCHAR(50) -- e.g., Train, Bus
);


CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    route_id INT,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    seat_number INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (route_id) REFERENCES transport_routes(route_id)
);


CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    ticket_number VARCHAR(100) UNIQUE,
    e_receipt TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);


CREATE TABLE utility_bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    bill_type VARCHAR(50), -- e.g., Electricity, Water, Gas
    bill_amount DECIMAL(10, 2),
    due_date DATE,
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT,
    user_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_amount DECIMAL(10, 2),
    payment_status VARCHAR(50), -- e.g., Paid, Pending
    FOREIGN KEY (bill_id) REFERENCES utility_bills(bill_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100),
    description TEXT
);


CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    service_id INT,
    appointment_date DATE,
    appointment_time TIME,
    status VARCHAR(50), -- e.g., Scheduled, Completed, Cancelled
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    document_name VARCHAR(255),
    document_type VARCHAR(50), -- e.g., CNIC, Utility Bill
    document_path VARCHAR(255), -- Path to stored document
    encrypted BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);











