import pyodbc

class StudentContractRecordDB:
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
        self.cursor.execute("SELECT Student.first_name AS 'First Name', \
                            Student.last_name AS 'Last Name', \
                            StudentCategory.student_category AS 'Student Category', \
                            StudentCode.student_code AS 'Student Code', \
                            StudentContract.studentcontractid AS 'Contract ID', \
                            StudentContractStatus.student_contract_status AS 'Contract Status' \
                            FROM StudentContract \
                            INNER JOIN Student ON StudentContract.studentid = Student.studentid \
                            INNER JOIN StudentCategory ON StudentContract.studentcategoryid = StudentCategory.studentcategoryid \
                            INNER JOIN StudentCode ON StudentContract.studentcodeid = StudentCode.studentcodeid \
                            INNER JOIN StudentContractStatus ON StudentContract.studentcontractstatusid = StudentContractStatus.studentcontractstatusid \
                            WHERE StudentContract.IsDelete = 0 \
                            ORDER BY Student.last_name")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()
