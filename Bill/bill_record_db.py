import pyodbc

class BillRecordDB:
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
        self.cursor.execute("SELECT Student.first_name AS 'Student First Name', \
                                Student.last_name AS 'Student Last Name', \
                                Membership.membership_fee AS 'Membership Fee', \
                                CoursePrice.course_price AS 'Course Price', \
                                BillNumber.bill_number AS 'Bill Number', \
                                Bill.total_bill AS 'Total Bill', \
                                Bill.bill_date AS 'Bill Date' \
                                FROM Bill \
                                INNER JOIN Student ON Bill.studentid = Student.studentid \
                                INNER JOIN Membership ON Bill.membershipid = Membership.membershipid \
                                INNER JOIN CoursePrice ON Bill.coursepriceid = CoursePrice.coursepriceid \
                                INNER JOIN BillNumber ON Bill.billnumberid = BillNumber.billnumberid \
                                WHERE Bill.IsDelete = 0 \
                                ORDER BY Student.first_name")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()