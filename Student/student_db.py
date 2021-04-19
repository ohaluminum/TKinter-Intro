import pyodbc

class StudentDB:
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
        self.cursor.execute("SELECT * FROM Student WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, addressid, first_name, last_name, phone, email):
        self.cursor.execute("INSERT INTO Student (addressid, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?)",
                            (addressid, first_name, last_name, phone, email))
        self.conn.commit()


    def remove(self, studentid):
        self.cursor.execute("UPDATE Student SET IsDelete = 1 WHERE studentid=?", (studentid,))
        self.conn.commit()


    def update(self, studentid, addressid, first_name, last_name, phone, email):
        self.cursor.execute("UPDATE student SET addressid = ?, first_name = ?, last_name = ?, phone = ?, email = ? WHERE studentid = ?",
                            (addressid, first_name, last_name, phone, email, studentid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()