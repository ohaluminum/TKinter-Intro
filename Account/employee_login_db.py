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


    def validateData(self, data, inputData):
        self.cursor.execute("SELECT * FROM EmployeeLogin WHERE employee_username = (?)", data)    # Search by username

        # Fetch the record
        row = self.cursor.fetchone()
        
        # No record find
        if row == None:
            return 1

        # Compare the provided password with database
        if row[2] == inputData[1]:
            return 0    # Password correct    
        else:
            return 2    # Password incorrect
        

    def __del__(self):
        self.conn.close()