import pyodbc

class AdminInfoDB:
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
        self.cursor.execute("SELECT * FROM AdminInfo WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, first_name, last_name):
        self.cursor.execute("INSERT INTO AdminInfo (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()


    def remove(self, admininfoid):
        self.cursor.execute("UPDATE AdminInfo SET IsDelete = 1 WHERE admininfoid=?", (admininfoid,))
        self.conn.commit()


    def update(self, admininfoid, first_name, last_name):
        self.cursor.execute("UPDATE AdminInfo SET first_name = ?, last_name = ? WHERE admininfoid = ?", (first_name, last_name, admininfoid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()