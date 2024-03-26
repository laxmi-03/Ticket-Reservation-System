# Just open the Mysql command prompt and login to administrator user and copy paste the following codes for creating dummy database:
<br>
ALTER SESSION SET "_ORACLE_SCRIPT"=TRUE;  
<br>
CREATE USER RESERVATION IDENTIFIED BY MANAGER;
<br>
GRANT DBA TO RESERVATION;
<br>
COMMIT;
<br>
CONNECT Ticket Reservation System;<br>
USE Ticket Reservation System;<br><br>
<pre>
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) UNIQUE
);

INSERT INTO customers (name, email, phone) VALUES
('John Doe', 'john@example.com', '1234567890'),
('Alice Smith', 'alice@example.com', '9876543210'),
('Bob Johnson', 'bob@example.com', '4567890123'),
('Emma Davis', 'emma@example.com', '7890123456'),
('Michael Brown', 'michael@example.com', '2345678901'),
('Olivia Wilson', 'olivia@example.com', '8901234567'),
('James Taylor', 'james@example.com', '5678901234'),
('Sophia Martinez', 'sophia@example.com', '9012345678'),
('William Anderson', 'william@example.com', '3456789012'),
('Isabella Thomas', 'isabella@example.com', '6789012345'),
('Liam Wilson', 'liam@example.com', '0123456789'),
('Emma Johnson', 'emma.j@example.com', '4321098765'),
('Noah Smith', 'noah@example.com', '7654321099'),
('Olivia Brown', 'olivia.b@example.com', '2109876543'),
('William Davis', 'william.d@example.com', '6543210987'),
('Sophia Miller', 'sophia.m@example.com', '9876543211'),
('Benjamin Wilson', 'benjamin.w@example.com', '3210987654'),
('Ava Martinez', 'ava@example.com', '8765432109'),
('Elijah Anderson', 'elijah@example.com', '0987654321'),
('Charlotte Garcia', 'charlotte@example.com', '5432109876'),
('Mason Rodriguez', 'mason@example.com', '7654321098'),
('Amelia Hernandez', 'amelia@example.com', '3456789010'),
('Ethan Lopez', 'ethan@example.com', '6789012340'),
('Harper Gonzalez', 'harper@example.com', '0123156789'),
('Evelyn Perez', 'evelyn@example.com', '4321098365'),
('Landon Torres', 'landon@example.com', '1098765431'),
('Lucas Ramirez', 'lucas@example.com', '7654321091'),
('Luna Flores', 'luna@example.com', '2345678902'),
('Aria Rivera', 'aria@example.com', '4567890129'),
('Mateo Cruz', 'mateo@example.com', '7890123453'),
('Zoey Cooper', 'zoey@example.com', '9876543214'),
('Levi Reed', 'levi@example.com', '3210987652'),
('Mila Bailey', 'mila@example.com', '8765432101'),
('Emma Gonzales', 'emma.g@example.com', '8987634321'),
('Liam Flores', 'liam.f@example.com', '5432109776'),
('Avery Cox', 'avery@example.com', '7654321090'),
('Ella Richardson', 'ella@example.com', '3456289012'),
('Jackson Stewart', 'jackson@example.com', '9789012345'),
('Scarlett Murphy', 'scarlett@example.com', '8123456769'),
('David Morris', 'david@example.com', '4321095765'),
('Madison Ward', 'madison@example.com', '1098765435'),
('Lucy Howard', 'lucy@example.com', '7654321094'),
('Wyatt Ross', 'wyatt@example.com', '2345678909'),
('Paisley Coleman', 'paisley@example.com', '6567890123'),
('Josephine Flores', 'josephine@example.com', '7890123450'),
('Elijah Peterson', 'elijah.p@example.com', '7123456789'),
('Gabriel Long', 'gabriel@example.com', '8234567890'),
('Leah Nguyen', 'leah@example.com', '9345678901'),
('Hannah King', 'hannah@example.com', '8456789012'),
('Nathan Cox', 'nathan@example.com', '9567890123'),
('Sofia Hughes', 'sofia@example.com', '8678901234'),
('Aiden Bell', 'aiden@example.com', '7789012345'),
('Audrey Wright', 'audrey@example.com', '7890123454'),
('Anna Foster', 'anna@example.com', '8901234562'),
('Eva Russell', 'eva@example.com', '9012345673'),
('Dylan Simmons', 'dylan@example.com', '8098755432'),
('Julian Martinez', 'julian@example.com', '9119876543'),
('Brooklyn Perry', 'brooklyn@example.com', '7210987654'),
('Alexa Powell', 'alexa@example.com', '8321098765'),
('Grayson Turner', 'grayson@example.com', '8432109876'),
('Bentley Carter', 'bentley@example.com', '6643210987'),
('Riley Perez', 'riley@example.com', '7654329098'),
('Samantha Brooks', 'samantha@example.com', '8665432109'),
('Angelina Cox', 'angelina@example.com', '9876443210'),
('Jordan Price', 'jordan@example.com', '9987652321'),
('Colton Hayes', 'colton@example.com', '7054321098'),
('Serenity James', 'serenity@example.com', '7345678902'),
('Leonardo Rogers', 'leonardo@example.com', '9567890124'),
('Sawyer Gray', 'sawyer@example.com', '7990123456'),
('Elena Wright', 'elena.w@example.com', '7123456788'),
('Ian Griffin', 'ian@example.com', '8345678909'),
('Violet Alexander', 'violet@example.com', '7567899123'),
('Alyssa Simmons', 'alyssa@example.com', '6890123446'),
('Camila Rivera', 'camila@example.com', '9123456781'),
('Dominic Bennett', 'dominic@example.com', '8345678901'),
('Zoe Cooper', 'zoe@example.com', '7567890123'),
('Lily Coleman', 'lily@example.com', '6890123456'),
('Adam Ramirez', 'adam@example.com', '8123456789'),
('Juliana Perry', 'juliana@example.com', '7345678901'),
('Nolan Foster', 'nolan@example.com', '9567890523'),
('Emilia Hughes', 'emilia@example.com', '7090123456'),
('Brianna Wright', 'brianna@example.com', '7123456779'),
('Tristan Morris', 'tristan@example.com', '9345678981'),
('Molly Brooks', 'molly@example.com', '8567890123'),
('Eliana Gray', 'eliana@example.com', '7898123456'),
('Adrian Simmons', 'adrian@example.com', '8123456770'),
('Bella Turner', 'bella@example.com', '9345678911'),
('Xavier Price', 'xavier@example.com', '7567897223'),
('Hailey Russell', 'hailey@example.com', '9890123456'),
('Peyton Bennett', 'peyton@example.com', '8103456789'),
('Diego Alexander', 'diego@example.com', '6345678901');


CREATE TRIGGER before_update
BEFORE UPDATE ON theatre_details
FOR EACH ROW
SET NEW.Booked_seats=(NEW.Capacity-NEW.Available_seats);

CREATE TABLE regular_customer (
    Customer_Id INT PRIMARY KEY,
    Loyalty_point INT,
    FOREIGN KEY (Customer_Id) REFERENCES customers(customer_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

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
(10, 80),
(11, 130),
(12, 170),
(13, 90),
(14, 240),
(15, 160),
(16, 110),
(17, 70),
(18, 140),
(19, 260),
(20, 200);


CREATE TABLE premium_customer (
    Customer_Id INT PRIMARY KEY,
    Membership_Level VARCHAR(50),
    FOREIGN KEY (Customer_Id) REFERENCES customers(customer_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

INSERT INTO premium_customer (Customer_Id, Membership_Level) VALUES
(21, 'Gold'),
(22, 'Silver'),
(23, 'Platinum'),
(24, 'Silver'),
(25, 'Gold'),
(26, 'Platinum'),
(27, 'Gold'),
(28, 'Diamond'),
(29, 'Silver'),
(30, 'Gold'),
(31, 'Platinum'),
(32, 'Silver'),
(33, 'Gold'),
(34, 'Silver'),
(35, 'Platinum'),
(36, 'Gold'),
(37, 'Silver'),
(38, 'Platinum'),
(39, 'Gold'),
(40, 'Silver'),
(41, 'Gold'),
(42, 'Platinum'),
(43, 'Silver'),
(44, 'Gold'),
(45, 'Platinum'),
(46, 'Gold'),
(47, 'Silver'),
(48, 'Gold'),
(49, 'Platinum'),
(50, 'Silver');


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
(1035, 'Concert', '2024-03-29', '20:45:00', 145),
(1036, 'Movie', '2024-03-30', '14:30:00', 85),
(1037, 'Play', '2024-03-31', '22:30:00', 110),
(1038, 'Concert', '2024-04-01', '19:15:00', 120),
(1039, 'Movie', '2024-04-02', '17:00:00', 95),
(1040, 'Play', '2024-04-03', '21:30:00', 135),
(1041, 'Movie', '2024-04-04', '18:00:00', 120),
(1042, 'Play', '2024-04-05', '20:30:00', 150),
(1043, 'Concert', '2024-04-06', '14:00:00', 180),
(1044, 'Movie', '2024-04-07', '19:00:00', 135),
(1045, 'Play', '2024-04-08', '21:45:00', 105),
(1046, 'Concert', '2024-04-09', '16:30:00', 90),
(1047, 'Movie', '2024-04-10', '22:15:00', 100),
(1048, 'Play', '2024-04-11', '17:45:00', 110),
(1049, 'Concert', '2024-04-12', '20:00:00', 140),
(1050, 'Movie', '2024-04-13', '15:15:00', 95),
(1051, 'Play', '2024-04-14', '19:30:00', 125),
(1052, 'Concert', '2024-04-15', '21:00:00', 115),
(1053, 'Movie', '2024-04-16', '18:45:00', 130),
(1054, 'Play', '2024-04-17', '16:00:00', 100),
(1055, 'Concert', '2024-04-18', '20:45:00', 145),
(1056, 'Movie', '2024-04-19', '14:30:00', 85),
(1057, 'Play', '2024-04-20', '22:30:00', 110),
(1058, 'Concert', '2024-04-21', '19:15:00', 120),
(1059, 'Movie', '2024-04-22', '17:00:00', 95),
(1060, 'Play', '2024-04-23', '21:30:00', 135);



CREATE TABLE Movie (
    show_id INT PRIMARY KEY,
    show_time TIME,
    duration INT,
    genre VARCHAR(50),
    FOREIGN KEY (show_id) REFERENCES show_details(show_id)
);

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


CREATE TABLE play (
    show_id INT,
    show_time TIME,
    duration INT,
    playwright VARCHAR(100),
    FOREIGN KEY (show_id) REFERENCES show_details(show_id)
);
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


CREATE TABLE tickets (
    Ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    show_Name VARCHAR(100),
    Customer_Name VARCHAR(100),
    Seat_number VARCHAR(20),
    Customer_id INT,
    Ticket_price INT,
    FOREIGN KEY (Customer_id) REFERENCES customers(customer_id)
);

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
(110, 'Movie J', 'Isabella Thomas', 'J10', 10),
(111, 'Play K', 'Liam Wilson', 'K11', 11),
(112, 'Concert L', 'Emma Johnson', 'L12', 12),
(113, 'Movie M', 'Noah Smith', 'M13', 13),
(114, 'Play N', 'Olivia Brown', 'N14', 14),
(115, 'Concert O', 'William Davis', 'O15', 15),
(116, 'Movie P', 'Sophia Miller', 'P16', 16),
(117, 'Play Q', 'Benjamin Wilson', 'Q17', 17),
(118, 'Concert R', 'Ava Martinez', 'R18', 18),
(119, 'Movie S', 'Elijah Anderson', 'S19', 19),
(120, 'Play T', 'Charlotte Thomas', 'T2', 20),
(121, 'Concert U', 'James Jackson', 'U21', 21),
(122, 'Movie V', 'Mia White', 'V22', 22),
(123, 'Play W', 'Lucas Harris', 'W23', 23),
(124, 'Concert X', 'Harper Wilson', 'X24', 24),
(125, 'Movie Y', 'Mason Davis', 'Y25', 25),
(126, 'Play Z', 'Evelyn Taylor', 'Z26', 26),
(127, 'Concert AA', 'Oliver Martinez', 'AA27', 27),
(128, 'Movie AB', 'Amelia Anderson', 'AB28', 28),
(129, 'Play AC', 'Ethan Thomas', 'AC29', 29),
(130, 'Concert AD', 'Isabella Garcia', 'AD30', 30),
(131, 'Movie AE', 'Liam Smith', 'AE31', 31),
(132, 'Play AF', 'Sophia Johnson', 'AF32', 32),
(133, 'Concert AG', 'Mason Brown', 'AG33', 33),
(134, 'Movie AH', 'Ava Davis', 'AH34', 34),
(135, 'Play AI', 'Oliver Miller', 'AI35', 35),
(136, 'Concert AJ', 'Amelia Wilson', 'AJ36', 36),
(137, 'Movie AK', 'Elijah Martinez', 'AK37', 37),
(138, 'Play AL', 'Harper Anderson', 'AL38', 38),
(139, 'Concert AM', 'Benjamin Thomas', 'AM39', 39),
(140, 'Movie AN', 'Charlotte Garcia', 'AN40', 40),
(141, 'Play AO', 'Mia Smith', 'AO41', 41),
(142, 'Concert AP', 'Lucas Johnson', 'AP42', 42),
(143, 'Movie AQ', 'Evelyn Brown', 'AQ43', 43),
(144, 'Play AR', 'Oliver Davis', 'AR44', 44),
(145, 'Concert AS', 'Amelia Taylor', 'AS45', 45),
(146, 'Movie AT', 'Elijah Martinez', 'AT46', 46),
(147, 'Play AU', 'Harper Anderson', 'AU47', 47),
(148, 'Concert AV', 'Benjamin Thomas', 'AV48', 48),
(149, 'Movie AW', 'Charlotte Garcia', 'AW49', 49),
(150, 'Play AX', 'Mia Smith', 'AX50', 50),
(151, 'Concert AY', 'Lucas Johnson', 'AY51', 51),
(152, 'Movie AZ', 'Evelyn Brown', 'AZ52', 52),
(153, 'Play BA', 'Oliver Davis', 'BA53', 53),
(154, 'Concert BB', 'Amelia Taylor', 'BB54', 54),
(155, 'Movie BC', 'Elijah Martinez', 'BC55', 55),
(156, 'Play BD', 'Harper Anderson', 'BD56', 56),
(157, 'Concert BE', 'Benjamin Thomas', 'BE57', 57),
(158, 'Movie BF', 'Charlotte Garcia', 'BF58', 58),
(159, 'Play BG', 'Mia Smith', 'BG59', 59),
(160, 'Concert BH', 'Lucas Johnson', 'BH60', 60),
(161, 'Movie BI', 'Evelyn Brown', 'BI61', 61),
(162, 'Play BJ', 'Oliver Davis', 'BJ62', 62),
(163, 'Concert BK', 'Amelia Taylor', 'BK63', 63),
(164, 'Movie BL', 'Elijah Martinez', 'BL64', 64),
(165, 'Play BM', 'Harper Anderson', 'BM65', 65),
(166, 'Concert BN', 'Benjamin Thomas', 'BN66', 66),
(167, 'Movie BO', 'Charlotte Garcia', 'BO67', 67),
(168, 'Play BP', 'Mia Smith', 'BP68', 68),
(169, 'Concert BQ', 'Lucas Johnson', 'BQ69', 69),
(170, 'Movie BR', 'Evelyn Brown', 'BR70', 70),
(171, 'Play BS', 'Oliver Davis', 'BS71', 71),
(172, 'Concert BT', 'Amelia Taylor', 'BT72', 72),
(173, 'Movie BU', 'Elijah Martinez', 'BU73', 73),
(174, 'Play BV', 'Harper Anderson', 'BV74', 74),
(175, 'Concert BW', 'Benjamin Thomas', 'BW75', 75),
(176, 'Movie BX', 'Charlotte Garcia', 'BX76', 76),
(177, 'Play BY', 'Mia Smith', 'BY77', 77),
(178, 'Concert BZ', 'Lucas Johnson', 'BZ78', 78),
(179, 'Movie CA', 'Evelyn Brown', 'CA79', 79),
(180, 'Play CB', 'Oliver Davis', 'CB80', 80);

</pre>
