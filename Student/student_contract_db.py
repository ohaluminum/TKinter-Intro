import pyodbc

class StudentContractDB:
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
        self.cursor.execute("SELECT * FROM StudentContract WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows

    
    def insert(self, studentid, studentcategoryid, studentcodeid, studentcontractstatusid):
        self.cursor.execute("INSERT INTO StudentContract (studentid, studentcategoryid, studentcodeid, studentcontractstatusid) VALUES (?, ?, ?, ?)",
                            (studentid, studentcategoryid, studentcodeid, studentcontractstatusid))
        self.conn.commit()


    def remove(self, studentcontractid):
        self.cursor.execute("UPDATE StudentContract SET IsDelete = 1 WHERE studentcontractid=?", (studentcontractid,))
        self.conn.commit()


    def update(self, studentcontractid, studentid, studentcategoryid, studentcodeid, studentcontractstatusid):
        self.cursor.execute("UPDATE studentcontract SET studentid = ?, studentcategoryid = ?, studentcodeid = ?, studentcontractstatusid = ? WHERE studentcontractid = ?",
                            (studentid, studentcategoryid, studentcodeid, studentcontractstatusid, studentcontractid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()