CREATE TABLE users (
  CNIC varchar(15) NOT NULL,
  first_name varchar(100) NOT NULL,
  last_name varchar(100),
  email varchar(255) NOT NULL unique,
  phone_number varchar(20) NOT NULL unique,
  pic longblob,
  dob date NOT NULL,
  gender enum('male', 'female') NOT NULL,
  password_hash varchar(255) NOT NULL,
  PRIMARY KEY (CNIC)
);


CREATE TABLE documents (
  document_id int NOT NULL auto_increment,
  cnic varchar(255) NOT NULL,
  document_name varchar(255) NOT NULL,
  document_ext varchar(50) NOT NULL,
  document_type varchar(255) NOT NULL,
  encrypted tinyint NOT NULL,
  upload_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  doc longblob not null,
  PRIMARY KEY (document_id),
  FOREIGN KEY (cnic) REFERENCES users(CNIC)
);


CREATE TABLE complains (
  complain_id int NOT NULL auto_increment,
  cnic varchar(255) NOT NULL,
  main_category TEXT NOT NULL,
  sub_category varchar(255),
  description TEXT NOT NULL,
  date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  address varchar(255) NOT NULL,
  status varchar(50) NOT NULL default 'pending',
  FOREIGN KEY (cnic) REFERENCES users(CNIC),
  PRIMARY KEY (complain_id)
);


CREATE TABLE payments (
  payment_id int NOT NULL auto_increment,
  bill_id int NOT NULL,
  payment_date timestamp DEFAULT CURRENT_TIMESTAMP ,
  payment_amount decimal NOT NULL,
  PRIMARY KEY (payment_id)
);



CREATE TABLE Admin (
  CNIC varchar(15),
  name varchar(100) NOT NULL,
  email varchar(255) NOT NULL unique,
  phone_number varchar(20) NOT NULL unique,
  password_hash varchar(255) NOT NULL,
  address varchar(255),
  PRIMARY KEY (CNIC)
);



CREATE TABLE routes (
  route_id int NOT NULL auto_increment,
  route_number varchar(50) NOT NULL,
  start_location varchar(255) NOT NULL,
  end_location varchar(255) NOT NULL,
  distance decimal NOT NULL,
  duration time NOT NULL,
  PRIMARY KEY (route_id)
);


CREATE TABLE feedback (
  feedback_id int NOT NULL auto_increment,
  refer_id varchar(255) NOT NULL,
  refer_type enum('appointment', 'complain') NOT NULL,
  feedback_text TEXT NOT NULL,
  feedback_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  feedback_rating int NOT NULL,
  PRIMARY KEY (feedback_id)
);



CREATE TABLE Appointments (
  id int PRIMARY key AUTO_INCREMENT,
  user_cnic varchar(255) NOT NULL,
  service varchar(255) NOT NULL,
  location varchar(255) NOT NULL,
  booking_date date NOT NULL,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status varchar(50) NOT NULL,
  FOREIGN KEY (user_cnic) REFERENCES users(CNIC)
); 

select * from Appointments where user_cnic = '3660245605291'


CREATE TABLE utility_bills (
  bill_id INT NOT NULL AUTO_INCREMENT,          
  user_cnic VARCHAR(15) NOT NULL,              
  bill_type VARCHAR(50) NOT NULL,              
  issue_date DATE NOT NULL,                     
  due_date DATE NOT NULL,                       
  amount_before_due DECIMAL(10, 2) NOT NULL,    
  tax_percentage DECIMAL(5, 2) NOT NULL,        
  tax_amount DECIMAL(10, 2) NOT NULL,          
  late_fee DECIMAL(10, 2) NOT NULL,            
  amount_after_due DECIMAL(10, 2) NOT NULL,    
  status ENUM('pending', 'paid') DEFAULT 'pending' NOT NULL,
  FOREIGN KEY (user_cnic) REFERENCES users(CNIC), 
  PRIMARY KEY (bill_id)
);


CREATE TABLE trips (
  trip_id int NOT NULL auto_increment,
  vehicle_id int NOT NULL,
  route_id int NOT NULL,
  trip_date date NOT NULL,
  departure_time datetime NOT NULL,
  status enum('scheduled', 'in-progress', 'completed', 'cancelled') NOT NULL,
  PRIMARY KEY (trip_id),
  FOREIGN KEY (route_id) REFERENCES routes(route_id)
);

CREATE TABLE address (
  cnic varchar(15) NOT NULL,
  province varchar(100) NOT NULL,
  district varchar(100) NOT NULL,
  city varchar(100) NOT null
);

CREATE TABLE bookings (
  booking_id int NOT NULL auto_increment,
  trip_id int NOT NULL,
  cnic varchar(20) NOT NULL,
  seat_number varchar(10) NOT NULL,
  booking_date datetime NOT NULL,
  status enum('confirmed', 'pending', 'cancelled') NOT NULL,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (trip_id) REFERENCES trips(trip_id),
  FOREIGN KEY (cnic) REFERENCES users(CNIC)
);