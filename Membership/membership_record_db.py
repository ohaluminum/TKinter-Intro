import pyodbc

class MembershipRecordDB:
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
                                MembershipStatus.membership_status, MembershipNumber.membership_number, \
                                MembershipType.membership_type, Membership.membership_fee, \
                                Membership.membership_start_date, Membership.membership_end_date \
                                FROM Membership \
                                INNER JOIN Student ON Membership.studentid = Student.studentid \
                                INNER JOIN MembershipStatus ON Membership.membershipstatusid = MembershipStatus.membershipstatusid \
                                INNER JOIN MembershipNumber ON Membership.membershipnumberid = MembershipNumber.membershipnumberid \
                                INNER JOIN MembershipType ON Membership.membershiptypeid = MembershipType.membershiptypeid \
                                ORDER BY Student.first_name") #\
                                #WHERE Membership.IsDelete = 0")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()