import pyodbc

class OwnerDB:
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
        self.cursor.execute("SELECT * FROM Owner WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, addressid, ownerstatusid, first_name, last_name, phone, email):
        self.cursor.execute("INSERT INTO Owner (addressid, ownerstatusid, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
                            (addressid, ownerstatusid, first_name, last_name, phone, email))
        self.conn.commit()


    def remove(self, ownerid):
        self.cursor.execute("UPDATE Owner SET IsDelete = 1 WHERE ownerid=?", (ownerid,))
        self.conn.commit()


    def update(self, ownerid, addressid, ownerstatusid, first_name, last_name, phone, email):
        self.cursor.execute("UPDATE Owner SET addressid = ?, ownerstatusid = ?, first_name = ?, last_name = ?, phone = ?, email = ? WHERE ownerid = ?",
                            (addressid, ownerstatusid, first_name, last_name, phone, email, ownerid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()