import pyodbc

class BillDB:
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
        self.cursor.execute("SELECT billid, studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill FROM Bill WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows
    

    def insert(self, studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill):
        self.cursor.execute("INSERT INTO Bill (studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill) VALUES (?, ?, ?, ?, ?, ?)",
                            (studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill))
        self.conn.commit()


    def remove(self, billid):
        self.cursor.execute("UPDATE Bill SET IsDelete = 1 WHERE billid=?", (billid,))
        self.conn.commit()


    def update(self, billid, studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill):
        self.cursor.execute("UPDATE Bill SET studentid = ?, coursepriceid = ?, membershipid = ?, billnumberid = ?, bill_date = ?, total_bill = ? WHERE billid =?",
                            (studentid, coursepriceid, membershipid, billnumberid, bill_date, total_bill, billid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()