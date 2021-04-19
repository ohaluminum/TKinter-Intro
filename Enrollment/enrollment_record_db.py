import pyodbc

class EnrollmentRecordDB:
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
        self.cursor.execute("SELECT Student.first_name, Student.last_name, \
                                EnrollmentStatus.enrollment_status, EnrollmentNumber.enrollment_number, \
                                EnrollmentPeriod.enrollment_period, Enrollment.enrollment_date \
                                FROM Enrollment \
                                INNER JOIN Student ON Enrollment.studentid = Student.studentid \
                                INNER JOIN EnrollmentStatus ON Enrollment.enrollmentstatusid = EnrollmentStatus.enrollmentstatusid \
                                INNER JOIN EnrollmentNumber ON Enrollment.enrollmentnumberid = EnrollmentNumber.enrollmentnumberid \
                                INNER JOIN EnrollmentPeriod ON Enrollment.enrollmentperiodid = EnrollmentPeriod.enrollmentperiodid \
                                ORDER BY Student.first_name \
                                WHERE IsDelete = 0")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()