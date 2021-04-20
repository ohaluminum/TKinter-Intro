import pyodbc 

class EmployeeDB:
    def __init__(self):
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


    def fetch(self):
        self.cursor.execute("SELECT * FROM Employee WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, addressid, first_name, last_name, phone, email):
        self.cursor.execute("INSERT INTO Employee (addressid, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?)",
                            (addressid, first_name, last_name, phone, email))
        self.conn.commit()


    def remove(self, employeeid):
        self.cursor.execute("UPDATE Employee SET IsDelete = 1 WHERE employeeid=?", (employeeid,))
        self.conn.commit()


    def update(self, employeeid, addressid, first_name, last_name, phone, email):
        self.cursor.execute("UPDATE Employee SET addressid = ?, first_name = ?, last_name = ?, phone = ?, email = ? WHERE employeeid = ?",
                            (addressid, first_name, last_name, phone, email, employeeid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()
        
