import pyodbc

class EnrollmentDB:
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
        self.cursor.execute("SELECT * FROM Enrollment WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows
    

    def insert(self, studentid, enrollmentstatusid, enrollmentnumberid, enrollmentperiodid, enrollment_date):
        self.cursor.execute("INSERT INTO Enrollment (studentid, enrollmentstatusid, enrollmentnumberid, enrollmentperiodid, enrollment_date) VALUES (?, ?, ?, ?, ?)",
                            (studentid, enrollmentstatusid, enrollmentnumberid, enrollmentperiodid, enrollment_date))
        self.conn.commit()


    def remove(self, enrollmentid):
        self.cursor.execute("UPDATE Enrollment SET IsDelete = 1 WHERE enrollmentid=?", (enrollmentid,))
        self.conn.commit()


    def update(self, enrollmentid, studentid, enrollmentstatusid, enrollmentnumberid, enrollmentperiodid, enrollment_date):
        self.cursor.execute("UPDATE Enrollment SET studentid = ?, enrollmentstatusid = ?, enrollmentnumberid = ?, enrollmentperiodid = ?, enrollment_date = ? WHERE enrollmentid = ?",
                            (studentid, enrollmentstatusid, enrollmentnumberid, enrollmentperiodid, enrollment_date, enrollmentid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()