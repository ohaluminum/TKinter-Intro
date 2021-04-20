import pyodbc

class EmployeeLoginDB:
    # Establish connection to database
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=CoT-CIS3365-09.cougarnet.uh.edu;"
                "Port=1433;"
                "Database=SoundboxDB;"
                "Trusted_Connection=no;"
                "UID=bchi2;"
                "PWD=Qwer123$;"
            )
            self.cursor = self.conn.cursor()
        except:
            print("Failed to connect to database.")


    def fetch(self):
        self.cursor.execute("SELECT * FROM EmployeeLogin WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, inputData):
        self.cursor.execute("INSERT INTO EmployeeLogin (employee_username, employee_password) VALUES (?, ?)",
                            (inputData[0], inputData[1]))
        self.conn.commit()

    
    def remove(self, employeeloginid):
        self.cursor.execute("UPDATE EmployeeLogin SET IsDelete = 1 WHERE employeeloginid=?", (employeeloginid,))
        self.conn.commit()


    def update(self, employeeloginid, employee_username, employee_password):
        self.cursor.execute("UPDATE EmployeeLogin SET employee_username = ?, employee_password = ? WHERE employeeloginid = ?",
                            (employee_username, employee_password, employeeloginid))
        self.conn.commit()


    def search(self, search):
        self.cursor.execute("SELECT * FROM EmployeeLogin WHERE employee_username = (?)", search)    # Search by username

        # Fetch the record
        rows = self.cursor.fetchall()

        if rows == []:
            return 0    # No record found
        else:
            return 1    # Record found


    def validate(self, search, inputData):
        self.cursor.execute("SELECT * FROM EmployeeLogin WHERE employee_username = (?)", search)    # Search by username

        # Fetch the record
        rows = self.cursor.fetchall()
        
        if rows == []:
            return 0    # No record found

        # Compare passwords
        if rows[0][2] == inputData[1]:
            return 1    # Password correct    
        else:
            return 2    # Password incorrect
        

    def __del__(self):
        self.conn.close()