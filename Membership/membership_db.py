import pyodbc

class MembershipDB:
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
        self.cursor.execute("SELECT * FROM Membership WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows
    

    def insert(self, studentid, membershipstatusid, membershipnumberid, membershiptypeid, membership_fee, membership_start_date, membership_end_date):
        self.cursor.execute("INSERT INTO Membership (studentid, membershipstatusid, membershipnumberid, membershiptypeid, membership_fee, "
                            "membership_start_date, membership_end_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (studentid, membershipstatusid, membershipnumberid, membershiptypeid, membership_fee, membership_start_date, membership_end_date))
        self.conn.commit()


    def remove(self, membershipid):
        self.cursor.execute("UPDATE Membership SET IsDelete = 1 WHERE membershipid=?", (membershipid,))
        self.conn.commit()


    def update(self, membershipid, studentid, membershipstatusid, membershipnumberid, membershiptypeid, membership_fee, membership_start_date, membership_end_date):
        self.cursor.execute("UPDATE Membership SET studentid = ?, membershipstatusid = ?, membershipnumberid = ?, membershiptypeid = ?, "
                            "membership_fee = ?, membership_start_date = ?, membership_end_date = ? WHERE membershipid = ?",
                            (studentid, membershipstatusid, membershipnumberid, membershiptypeid, membership_fee, membership_start_date, membership_end_date, membershipid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()