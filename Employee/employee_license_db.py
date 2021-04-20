import pyodbc

class EmployeeLicenseDB:
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
        self.cursor.execute("SELECT * FROM EmployeeLicense WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, employeeid, employeestatusid, employeetypeid, employeelicensenumberid):
        self.cursor.execute("INSERT INTO EmployeeLicense (employeeid, employeestatusid, employeetypeid, employeelicensenumberid) VALUES (?, ?, ?, ?)",
                            (employeeid, employeestatusid, employeetypeid, employeelicensenumberid))
        self.conn.commit()


    def remove(self, employeelicenseid):
        self.cursor.execute("UPDATE EmployeeLicense SET IsDelete = 1 WHERE employeelicenseid=?", (employeelicenseid,))
        self.conn.commit()


    def update(self, employeelicenseid, employeeid, employeestatusid, employeetypeid, employeelicensenumberid):
        self.cursor.execute("UPDATE EmployeeLicense SET employeeid = ?, employeestatusid = ?, employeetypeid = ?, employeelicensenumberid = ? WHERE employeelicenseid = ?",
                            (employeeid, employeestatusid, employeetypeid, employeelicensenumberid, employeelicenseid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()