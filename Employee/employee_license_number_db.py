import pyodbc

class EmployeeLicenseNumberDB:
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
        self.cursor.execute("SELECT * FROM EmployeeLicenseNumber WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, employee_license_number):
        self.cursor.execute("INSERT INTO EmployeeLicenseNumber (employee_license_number) VALUES (?)", (employee_license_number))
        self.conn.commit()


    def remove(self, employeelicensenumberid):
        self.cursor.execute("UPDATE EmployeeLicenseNumber SET IsDelete = 1 WHERE employeelicensenumberid=?", (employeelicensenumberid,))
        self.conn.commit()


    def update(self, employeelicensenumberid, employee_license_number):
        self.cursor.execute("UPDATE EmployeeLicenseNumber SET employee_license_number = ? WHERE employeelicensenumberid = ?",
                            (employee_license_number, employeelicensenumberid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()