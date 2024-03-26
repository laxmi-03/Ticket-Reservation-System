# Ticket-Reservation-System
Python Projects
<br><br>
About<br>
This project is about Ticket Reservation System which is used to view show details, search shows/customers, Seat availability, show timings. We can also enquire about price of different shows. We can book seats online. This provides a easy to use Ticket Reservation System.
<br>

1. View Show details-<br>
  All details<br>
  Particular<br>
2. Movie details-<br>
  All details<br>
  Particular<br>
3. Play details-<br>
  All details<br>
  Particular<br>
4. Reserve seat<br>
5. Check seat availibility<br>
6. Show customer details<br>
7. Update customer details<br>
8. Search customer details through name, email,phone<br>
9. Add new customer details<br>
10. show regular customer details using customer id<br>
11. show premium customer details using customer id<br>
12. Generate ticket<br>
<br>
Technologies used:-<br>
  * Python<br>
  * MySql
<br><br>
========= Dummy Database Initialization ===========
STEP 1: Open SQL Plus OR SQL Developer
<br><br>
STEP 2: Login and connect to database using administrator username and password
<br><br>
STEP 3 :Execute the below command first to create a new user:
<br><br>
<p>ALTER SESSION SET "_ORACLE_SCRIPT"=TRUE;  
CREATE USER RESERVATION IDENTIFIED BY MANAGER;
GRANT DBA TO RESERVATION;
COMMIT;<p></p>
NOTE: If the above command fails for alter session issues, try to remove first line and then execute it.
STEP 4: Now execute the below sql query in same terminal

