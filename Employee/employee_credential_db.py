import pyodbc

class EmployeeCredentialDB:
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
        self.cursor.execute("SELECT * FROM EmployeeCredentials WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, employeeid, employeetypeid, employeestatusid, employeeloginid):
        self.cursor.execute("INSERT INTO EmployeeCredentials (employeeid, employeetypeid, employeestatusid, employeeloginid) VALUES (?, ?, ?, ?)",
                            (employeeid, employeetypeid, employeestatusid, employeeloginid))
        self.conn.commit()


    def remove(self, employeecredentialsid):
        self.cursor.execute("UPDATE EmployeeCredentials SET IsDelete = 1 WHERE employeecredentialsid=?", (employeecredentialsid,))
        self.conn.commit()


    def update(self, employeecredentialsid, employeeid, employeetypeid, employeestatusid, employeeloginid):
        self.cursor.execute("UPDATE EmployeeCredentials SET employeeid = ?, employeetypeid = ?, employeestatusid = ?, employeeloginid = ? WHERE employeecredentialsid = ?",
                            (employeeid, employeetypeid, employeestatusid, employeeloginid, employeecredentialsid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()