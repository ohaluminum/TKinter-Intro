import pyodbc

class VendorDB:
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
        self.cursor.execute("SELECT * FROM Vendor WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows
    

    def insert(self, addressid, vendorstatusid, first_name, last_name, phone, email):
        self.cursor.execute("INSERT INTO Vendor (addressid, vendorstatusid, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
                            (addressid, vendorstatusid, first_name, last_name, phone, email))
        self.conn.commit()


    def remove(self, vendorid):
        self.cursor.execute("UPDATE Vendor SET IsDelete = 1 WHERE vendorid= ?", (vendorid,))
        self.conn.commit()


    def update(self, vendorid, addressid, vendorstatusid, first_name, last_name, phone, email):
        self.cursor.execute("UPDATE Vendor SET addressid = ?, vendorstatusid = ?, first_name = ?, last_name = ?, phone = ?, email = ? WHERE vendorid = ?",
                            (addressid, vendorstatusid, first_name, last_name, phone, email, vendorid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()