import pyodbc

class AdminLoginDB:
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


    def insert(self, inputData):
        self.cursor.execute("INSERT INTO AdminLogin (adminusername, adminpassword) VALUES (?, ?)",
                            (inputData[0], inputData[1]))
        self.conn.commit()


    def search(self, search):
        self.cursor.execute("SELECT * FROM AdminLogin WHERE adminusername = (?)", search)    # Search by username

        # Fetch the record
        rows = self.cursor.fetchall()

        if rows == []:
            return 0    # No record found
        else:
            return 1    # Record found


    def validate(self, search, inputData):
        self.cursor.execute("SELECT * FROM AdminLogin WHERE adminusername = (?)", search)    # Search by username

        # Fetch the record
        row = self.cursor.fetchone()
        
        # No record find
        if row == None:
            return 0

        # Compare the provided password with database
        if row[2] == inputData[1]:
            return 1    # Password correct    
        else:
            return 2    # Password incorrect
        

    def __del__(self):
        self.conn.close()