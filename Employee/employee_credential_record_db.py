import pyodbc

class EmployeeCredentialRecordDB:
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
                            EmployeeType.employee_type AS 'Type', \
                            EmployeeStatus.employee_status AS 'Status' \
                            FROM EmployeeCredentials \
                            INNER JOIN Employee ON EmployeeCredentials.employeeid = Employee.employeeid \
                            INNER JOIN EmployeeType ON EmployeeCredentials.employeetypeid = EmployeeType.employeetypeid \
                            INNER JOIN EmployeeStatus ON EmployeeCredentials.employeestatusid = EmployeeStatus.employeestatusid \
                            ORDER BY Employee.first_name")
                            # WHERE EmployeeCredentials.IsDelete = 0")
                                    
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()