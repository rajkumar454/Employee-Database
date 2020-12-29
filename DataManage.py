import sqlite3 as lite

#fuctionality goes here

class DataManage(object):
    def __init__(self):
        global con
        try:
            con=lite.connect('employee.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS employee(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Department TEXT, Salary TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB")

    #TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO employee(Name, Department, Salary, is_private) VALUES(?,?,?,?)",data
                    )
                return True
        except Exception:
            return False

    #TODO: Read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM employee")
                return cur.fetchall()
        except Exception:
            return False
    #TODO: Delete data
    def delete_data(self, Id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM employee WHERE Id = ?"
                cur.execute(sql, [Id])
                return True
        except Exception:
            return False


#TODO: Provide interface to use
def main():
    print("*"*40)
    print("\n:: EMPLOYEE DATA :: \n")
    print("*"*40)
    print("\n")

    db = DataManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\nPress 1. Insert a New employee\n')
    print('Press 2. Show all employee\n')
    print('Press 3. Delete employee(NEED Id OF EMPLOYEE)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a Choice: ")

    if choice == "1":
        Name = input("Enter a Employee name: ")
        Department = input("Enter a Employee Department: ")
        Salary = input("Enter a Employee Salary: ")
        private = input("Is it private(0/1): ")

        if db.insert_data([Name, Department, Salary, private]):
            print("Employee data successfully inserted")
        else:
            print("Oops Something went wrong")
    elif choice =="2":
        print("\n :: Employee List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no :" + str(index + 1))
            print("Employee Id : "+ str(item[0]))
            print("Employee Name : "+ str(item[1]))
            print("Employee Department : "+ str(item[2]))
            print("Employee Salary : "+ str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is Private " + private)
            print("\n")

    elif choice == "3":
        record_id=input("Enter Employee Id: ")

        if db.delete_data(record_id):
            print("Employee Data Deleted Successfully")
        else:
            print("Oops something wrong")

    else:
        print("\n BAD CHOICE")

if __name__ == '__main__':
    main()
