# Ticket-Reservation-System
<b>Python Project</b>

### About:
This project is about Ticket Reservation System which is used to view show details, search shows/customers, Seat availability, show timings. We can also enquire about price of different shows. We can book seats online. This provides a easy to use Ticket Reservation System.

### Features
<span style="color:blue">**This Project is built for following purpose:-**</span>
1. View Show details:-
  - All details
  - Particular
2. Movie details:-
  - All details
  - Particular
3. Play details:-
  - All details
  - Particular
4. Reserve seat
5. Check seat availibility
6. Show customer details
7. Update customer details
8. Search customer details through name, email,phone
9. Add new customer details
10. show regular customer details using customer id
11. show premium customer details using customer id
12. Generate ticket

### Technologies used:-
  - Python
  - MySql

### ========== Dummy Database Initialization ===========

STEP 1: Open SQL Plus OR SQL Developer

STEP 2: Login and connect to database using administrator username and password

STEP 3 :Execute the below command first to create a new user:

```SQL

CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

```
NOTE: If the above command fails for alter session issues, try to remove first line and then execute it.

STEP 4: Now execute the below sql query in same terminal

```SQL
CREATE TABLE Show_Details (
    Show_ID INT AUTO_INCREMENT PRIMARY KEY,
    Show_Type VARCHAR(50),
    Show_Date DATE,
    Show_Time TIME,
    Show_Duration INT
) AUTO_INCREMENT = 1001;


CREATE TABLE Movie (
    show_id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
    show_time TIME,
    duration INT,
    genre VARCHAR(50),
    FOREIGN KEY (show_id) REFERENCES show_details(show_id)
) AUTO_INCREMENT = 1001;

    
CREATE TABLE play (
    show_id INT,
    show_time TIME,
    duration INT,
    playwright VARCHAR(100),
    FOREIGN KEY (show_id) REFERENCES show_details(show_id)
) AUTO_INCREMENT = 1011;

    
CREATE TABLE theatre_details (
    Name VARCHAR(255) UNIQUE,
    Location VARCHAR(255),
    Capacity INT,
    Available_seats INT,
    Booked_seats INT
);

    
CREATE TRIGGER before_update
BEFORE UPDATE ON theatre_details
FOR EACH ROW
SET NEW.Booked_seats=(NEW.Capacity-NEW.Available_seats);

    
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) UNIQUE
);

    
CREATE TABLE regular_customer (
    Customer_Id INT PRIMARY KEY,
    Loyalty_point INT,
    FOREIGN KEY (Customer_Id) REFERENCES customers(customer_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

    
CREATE TABLE premium_customer (
    Customer_Id INT PRIMARY KEY,
    Membership_Level VARCHAR(50),
    FOREIGN KEY (Customer_Id) REFERENCES customers(customer_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
); 


CREATE TABLE tickets (
    Ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    show_Name VARCHAR(100),
    Customer_Name VARCHAR(100),
    Seat_number VARCHAR(20),
    Customer_id INT,
    Ticket_price INT,
    FOREIGN KEY (Customer_id) REFERENCES customers(customer_id)
) AUTO_INCREMENT = 101;
  

    
INSERT INTO show_details (Show_ID, Show_Type, Show_Date, Show_Time, Show_Duration)
VALUES
    (1021, 'Movie', '2024-03-15', '18:00:00', 120),
    (1022, 'Play', '2024-03-16', '20:30:00', 150),
    (1023, 'Concert', '2024-03-17', '14:00:00', 180),
    (1024, 'Movie', '2024-03-18', '19:00:00', 135),
    (1025, 'Play', '2024-03-19', '21:45:00', 105),
    (1026, 'Concert', '2024-03-20', '16:30:00', 90),
    (1027, 'Movie', '2024-03-21', '22:15:00', 100),
    (1028, 'Play', '2024-03-22', '17:45:00', 110),
    (1029, 'Concert', '2024-03-23', '20:00:00', 140),
    (1030, 'Movie', '2024-03-24', '15:15:00', 95),
    (1031, 'Play', '2024-03-25', '19:30:00', 125),
    (1032, 'Concert', '2024-03-26', '21:00:00', 115),
    (1033, 'Movie', '2024-03-27', '18:45:00', 130),
    (1034, 'Play', '2024-03-28', '16:00:00', 100),
    (1035, 'Concert', '2024-03-29', '20:45:00', 145);



INSERT INTO Movie (show_id, show_time, duration, genre)
VALUES
    (1001, '18:00:00', 120, 'Drama'),
    (1002, '20:30:00', 150, 'Comedy'),
    (1003, '14:00:00', 180, 'Action'),
    (1004, '19:00:00', 135, 'Thriller'),
    (1005, '21:45:00', 105, 'Romance'),
    (1006, '16:30:00', 90, 'Adventure'),
    (1007, '22:15:00', 100, 'Science Fiction'),
    (1008, '17:45:00', 110, 'Horror'),
    (1009, '20:00:00', 140, 'Fantasy'),
    (1010, '15:15:00', 95, 'Mystery');


    
INSERT INTO play (show_id, show_time, duration, playwright)
VALUES
    (1011, '18:00:00', 120, 'William Shakespeare'),
    (1012, '20:30:00', 150, 'Arthur Miller'),
    (1013, '14:00:00', 180, 'Tennessee Williams'),
    (1014, '19:00:00', 135, 'August Wilson'),
    (1015, '21:45:00', 105, 'Neil Simon'),
    (1016, '16:30:00', 90, 'Edward Albee'),
    (1017, '22:15:00', 100, 'David Mamet'),
    (1018, '17:45:00', 110, 'Harold Pinter'),
    (1019, '20:00:00', 140, 'Anton Chekhov'),
    (1020, '15:15:00', 95, 'Henrik Ibsen');


    
INSERT INTO theatre_details (Name, Location, Capacity, Available_seats, Booked_seats)
VALUES 
    ('Theater India 1', 'Mumbai', 300, 20, 280),
    ('Cinema India 2', 'Delhi', 200, 180, 20),
    ('Concert Hall India 3', 'Bangalore', 500, 200, 300),
    ('Playhouse India 4', 'Kolkata', 400, 370, 30),
    ('Arena India 5', 'Chennai', 1000, 900, 100),
    ('Auditorium India 6', 'Hyderabad', 600, 580, 20),
    ('Stadium India 7', 'Pune', 1500, 1400, 100),
    ('Cinema India 8', 'Ahmedabad', 250, 220, 30),
    ('Theater India 9', 'Surat', 350, 320, 30),
    ('Concert Venue India 10', 'Jaipur', 450, 420, 30);

    

INSERT INTO customers (name, email, phone)
VALUES
    ('John Doe', 'john@example.com', '1234567890'),
    ('Alice Smith', 'alice@example.com', '9876543210'),
    ('Bob Johnson', 'bob@example.com', '4567890123'),
    ('Emma Davis', 'emma@example.com', '7890123456'),
    ('Michael Brown', 'michael@example.com', '2345678901'),
    ('Olivia Wilson', 'olivia@example.com', '8901234567'),
    ('James Taylor', 'james@example.com', '5678901234'),
    ('Sophia Martinez', 'sophia@example.com', '9012345678'),
    ('Colton Hayes', 'colton@example.com', '7054321098'),
    ('Serenity James', 'serenity@example.com', '7345678902'),
    ('Adam Ramirez', 'adam@example.com', '8123456789'),
    ('Juliana Perry', 'juliana@example.com', '7345678901'),
    ('Nolan Foster', 'nolan@example.com', '9567890523'),
    ('Emilia Hughes', 'emilia@example.com', '7090123456'),
    ('Brianna Wright', 'brianna@example.com', '7123456779'),
    ('Tristan Morris', 'tristan@example.com', '9345678981'),
    ('Molly Brooks', 'molly@example.com', '8567890123'),
    ('Eliana Gray', 'eliana@example.com', '7898123456'),
    ('Adrian Simmons', 'adrian@example.com', '8123456770'),
    ('Bella Turner', 'bella@example.com', '9345678911');
  

    
INSERT INTO regular_customer (Customer_Id, Loyalty_point) VALUES
(1, 100),
(2, 150),
(3, 200),
(4, 50),
(5, 300),
(6, 250),
(7, 120),
(8, 180),
(9, 220),
(10, 80);


    
INSERT INTO premium_customer (Customer_Id, Membership_Level) VALUES
(11, 'Gold'),
(12, 'Silver'),
(13, 'Platinum'),
(14, 'Silver'),
(15, 'Gold'),
(16, 'Platinum'),
(17, 'Gold'),
(18, 'Diamond'),
(19, 'Silver'),
(20, 'Gold');

    

INSERT INTO tickets (Ticket_id, show, Customer_Name, Seat_number, Customer_id) VALUES
(101, 'Movie A', 'John Smith', 'A1', 1),
(102, 'Play B', 'Alice Johnson', 'B2', 2),
(103, 'Concert C', 'Bob Williams', 'C3', 3),
(104, 'Movie D', 'Emma Davis', 'D4', 4),
(105, 'Play E', 'Michael Brown', 'E5', 5),
(106, 'Concert F', 'Olivia Wilson', 'F6', 6),
(107, 'Movie G', 'James Taylor', 'G7', 7),
(108, 'Play H', 'Sophia Martinez', 'H8', 8),
(109, 'Concert I', 'William Anderson', 'I9', 9),
(110, 'Movie J', 'Isabella Thomas', 'J10', 10);
Ticket-Reservation-System/Dummy-database.md at main · laxmi-03/Ticket-Reservation-System
```

STEP 5: Now Execute the below query one by one to check if the tables are created successfully
```SQL
SELECT * FROM show_details;
SELECT * FROM Movie;
SELECT * FROM play;
SELECT * FROM Theatre;
SELECT * FROM customers;
SELECT * FROM regular_customer;
SELECT * FROM premium_customer;
SELECT * FROM tickets;

```
Note: If any of the above commands fails, please try to fix it first and then proceed to next step

