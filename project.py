import mysql.connector as myconn

mydb=myconn.connect(host='localhost',
                  user='root',
                  password='root',
                  database='ticket_management_system')

name=input("Enter your name: ")
print(f"Welcome {name} in Ticket Managenment System")


class show:
        def particular_show_details(self,show_Id):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Show_details")
            found=False
            for db_data in db_cursor1.fetchall():
                if show_Id==db_data[0]:
                    print(f"Show Id: {db_data[0]}\nShow_Type: {db_data[1]}\nShow_Date: {db_data[2]}\nShow_Time: {db_data[3]}\nShow_Duration: {db_data[4]} min")
                    found=True
                    break
            if not found:
                print("Not Available")

        def all_shows(self):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Show_details")
            for db_data in db_cursor1.fetchall():
                print(db_data)

class Movie(show):
        def particular_show_details(self,show_Id):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Movie")
            found=False
            for db_data in db_cursor1.fetchall():
                if show_Id==db_data[0]:
                    print(f"Show Id: {db_data[0]}\nShow_Time: {db_data[1]}\nDuration: {db_data[2]} min\nGenre: {db_data[3]}")
                    found=True
                    break
            if not found:
                print("Not Available")
        def all_shows(self):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Movie")
            for db_data in db_cursor1.fetchall():
                print(db_data)

class Play(show):
        def particular_show_details(self,show_Id):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Play")
            found=False
            for db_data in db_cursor1.fetchall():
                if show_Id==db_data[0]:
                    print(f"Show Id: {db_data[0]}\nShow_Time: {db_data[1]}\nDuration: {db_data[2]} min\nPlaywright: {db_data[3]}")
                    found=True
                    break
            if not found:
                print("Not Available")
        def all_shows(self):
            db_cursor1=mydb.cursor()
            db_cursor1.execute("select*from Play")
            for db_data in db_cursor1.fetchall():
                print(db_data)



class Theatre:
    def reserve_seat(self, num_seats,name):
        db_cursor2=mydb.cursor()
        db_cursor2.execute("select*from theatre_details")
        for db_data in db_cursor2.fetchall():
            if name==db_data[0]:       
                if num_seats <= db_data[3]:
                    update_data="update theatre_details set Available_seats =%s where name =%s"
                    db_value=(db_data[3]-num_seats,db_data[0])
                    db_cursor2.execute(update_data,db_value)
                    mydb.commit()
                    print(f"{num_seats} seats reserved successfully.")
                else:
                    print("Not enough seats available.")

    def check_seat_availability(self):
        db_cursor2=mydb.cursor()
        db_cursor2.execute("select*from theatre_details")
        print(f"Available seats: ")
        for db_data in db_cursor2.fetchall():
            print({db_data})



class Customer:
    def show_details(self):
        db_cursor3=mydb.cursor()
        db_cursor3.execute("select*from customers")

        for db_data in db_cursor3.fetchall():
            print(db_data)

    def update_details(self,name):
        db_cursor3=mydb.cursor()
        db_cursor3.execute("select*from customers")
        found=False

        for db_data in db_cursor3.fetchall():
            if name == db_data[1]:
                print("Select the field to edit:")
                print("1. Name")
                print("2. Email")
                print("3. Phone number")
                choice = input("Enter your choice (1-3):")


                if choice == "1":
                    new_name = input("Enter new name: ")
                    update_data="update customers set name =%s where customer_id =%s"
                    db_value=(new_name,db_data[0])
                    db_cursor3.execute(update_data,db_value)
                    mydb.commit()
                elif choice == "2":
                    new_email = input("Enter new email address: ")
                    update_data="update customers set email =%s where customer_id =%s"
                    db_value=(new_email,db_data[0])
                    db_cursor3.execute(update_data,db_value)
                    mydb.commit()
                elif choice == "3":
                    new_phone = input("Enter new phone number: ")
                    update_data="update customers set phone =%s where customer_id =%s"
                    db_value=(new_phone,db_data[0])
                    db_cursor3.execute(update_data,db_value)
                    mydb.commit()
                
                else:
                    print("Invalid choice.")
                    return

                print("Details updated sucessfully!")
                found = True
                break
        if not found:
            print("Details not available")


    def search_details(self):
        db_cursor3=mydb.cursor()
        db_cursor3.execute("select*from customers")
        query = input("Enter search query: ")
        found_details = []

        for db_data in db_cursor3.fetchall():
            if (
                query.lower() in db_data[1].lower()
                or query.lower() in db_data[2].lower()
                or query.lower() in db_data[3].lower()
            ):
                found_details.append(db_data)

        if found_details:
            for detail in found_details:
                print("Search results:")
                print(f"Customer Id: {detail[0]}\nName: {detail[1]}\nEmail: {detail[2]}\nPhone No: {detail[3]}")
        else:
            print("No contact found.")

    def add_details(self):
        db_cursor3=mydb.cursor()
        name=input("Enter name: ")
        email=input("Enter email id: ")
        phone=input("Enter phone no: ")
        db_cursor3.execute("insert into customers (name,email,phone) values (%s,%s,%s)",(name,email,phone))
        mydb.commit()

class RegularCustomer(Customer):
    def show_details(self,customer_id):
        db_cursor3=mydb.cursor()
        db_cursor3.execute("select*from regular_customer")
        found=False
        for db_data in db_cursor3.fetchall():
            if customer_id==db_data[0]:
                Customer.search_details(self)
                print(f"Loyalty Points: {db_data[1]}")
                found=True
                break
        if not found:
            print("Not available!")
           
class PremiumCustomer(Customer):
    def show_details(self,customer_id):
        db_cursor3=mydb.cursor()
        db_cursor3.execute("select*from premium_customer")
        found=False
        for db_data in db_cursor3.fetchall():
            if customer_id==db_data[0]:
                Customer.search_details(self)
                print(f"Membership Level: {db_data[1]}")
                found=True
                break
        if not found:
            print("Not available!")
           


class Ticket:
    def generate_ticket(self,Ticket_Id):
        db_cursor4=mydb.cursor()
        db_cursor4.execute("select*from tickets")
        found=False
        for db_data in db_cursor4.fetchall():
            if Ticket_Id==db_data[0]:
                print(f"Ticket ID: {Ticket_Id}")
                print(f"Show Name: {db_data[1]}")
                print(f"Customer_Id: {db_data[4]}")
                print(f"Customer: {db_data[2]}")
                print(f"Seat Number: {db_data[3]}")
                print(f"Ticket Price: {db_data[5]}")
                found=True
                break
        if not found:
            print("Not found")    


while True:
    print("\n1. Show Details ")
    print("2. Movie details")
    print("3. Play details")
    print("4. Theatre details")
    print("5. Customer details")
    print("6. Regular Customer details ")
    print("7. Premium Customer details ")
    print("8. Ticket details")
    print("9. Exist")

    choice=input("Enter your choice(1-9): ")
    match choice:
        case '1':
            opt=input("1. Show particular detail\n2. Show all details\n")
            s1=show()
            match opt:
                case '1':
                    id=int(input("Enter Show id: "))
                    s1.particular_show_details(id)
                case '2':
                    s1.all_shows()
                case _:
                    print("Invalid input!")
        case '2':
            opt=input("1. Show particular detail\n2. Show all details\n")
            m1=Movie()
            match opt:
                case '1':
                    id=int(input("Enter Show id: "))
                    m1.particular_show_details(id)
                case '2':
                    m1.all_shows()
                case _:
                    print("Invalid input!")
        case  '3':
            opt=input("1. Show particular detail\n2. Show all details\n")
            p1=Play()
            match opt:
                case '1':
                    id=int(input("Enter Show id: "))
                    p1.particular_show_details(id)
                case '2':
                    p1.all_shows()
                case _:
                    print("Invalid input!")
        case '4':
            opt=input("1. Reserve seat\n2. Check Seat Avaibility\n")
            t1=Theatre()
            match opt:
                case '1':
                    seats=int(input("Enter number of seats: "))
                    name=input("Enter name of theatre: ")
                    t1.reserve_seat(seats,name)
                case '2':
                    t1.check_seat_availability()
                case _:
                    print("Invalid input!")
        case '5':
            opt =input("1. Show details\n2. Update details\n3. Seach details\n4. Insert details\n")
            c1=Customer()
            match opt:
                case '1':
                    c1.show_details()
                case '2':
                    name=input("Enter name to update: ")
                    c1.update_details(name)
                case '3':
                    c1.search_details()
                case '4':
                    c1.add_details()
                case _:
                    print("Invalid input!")
        case '6':
            id=int(input("Enter Customer id: "))
            r1=RegularCustomer()
            r1.show_details(id)
        case '7':
            id=int(input("Enter Customer id: "))
            pr=PremiumCustomer()
            pr.show_details(id)
        case '8':
            id=int(input("Enter ticket id: "))
            t=Ticket()
            t.generate_ticket(id)
        case '9':
            break
        case _:
            print("Invalid input!")
