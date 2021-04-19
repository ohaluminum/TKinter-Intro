import pyodbc

class AdminDB:
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
        self.cursor.execute("SELECT * FROM Admin WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, admininfoid, adminloginid, adminstatusid, addressid):
        self.cursor.execute("INSERT INTO Admin (admininfoid, adminloginid, adminstatusid, addressid) VALUES (?, ?, ?, ?)",
                            (admininfoid, adminloginid, adminstatusid, addressid))
        self.conn.commit()


    def remove(self, adminid):
        self.cursor.execute("UPDATE Admin SET IsDelete = 1 WHERE adminid=?", (adminid,))
        self.conn.commit()


    def update(self, adminid, admininfoid, adminloginid, adminstatusid, addressid):
        self.cursor.execute("UPDATE Admin SET admininfoid = ?, adminloginid = ?, adminstatusid = ?, addressid= ? WHERE adminid = ?",
                            (admininfoid, adminloginid, adminstatusid, addressid, adminid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()