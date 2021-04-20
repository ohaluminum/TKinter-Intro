import pyodbc

class EmployeeLicenseRecordDB:
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
        self.cursor.execute("SELECT Employee.first_name AS 'First Name', \
                            Employee.last_name AS 'Last Name', \
                            Employee.phone AS 'Phone', \
                            Employee.email AS 'Email', \
                            EmployeeStatus.employee_status AS 'Status', \
                            EmployeeType.employee_type AS 'Type', \
                            EmployeeLicenseNumber.employee_license_number AS 'License Number' \
                            FROM EmployeeLicense \
                            INNER JOIN Employee ON EmployeeLicense.employeeid = Employee.employeeid \
                            INNER JOIN EmployeeStatus ON EmployeeLicense.employeestatusid = EmployeeStatus.employeestatusid \
                            INNER JOIN EmployeeType ON EmployeeLicense.employeetypeid = EmployeeType.employeetypeid \
                            INNER JOIN EmployeeLicenseNumber ON EmployeeLicense.employeelicensenumberid = EmployeeLicenseNumber.employeelicensenumberid \
                            WHERE EmployeeLicense.IsDelete = 0 \
                            ORDER BY Employee.first_name") 
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()