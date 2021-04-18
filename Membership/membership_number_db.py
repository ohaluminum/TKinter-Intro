import pyodbc

class MembershipNumberDB:
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
        self.cursor.execute("SELECT * FROM MembershipNumber")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, membership_number):
        self.cursor.execute("INSERT INTO MembershipNumber (membership_number) VALUES (?)", (membership_number,))
        self.conn.commit()


    def remove(self, membershipnumberid):
        self.cursor.execute("DELETE FROM MembershipNumber WHERE membershipnumberid=?", (membershipnumberid,))
        self.conn.commit()


    def update(self, membershipnumberid, membership_number):
        self.cursor.execute("UPDATE MembershipNumber SET membership_number = ? WHERE membershipnumberid = ?", (membershipnumberid, ))
        self.conn.commit()
        

    def __del__(self):
        self.conn.close()