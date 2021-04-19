import pyodbc

class EventDB:
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
        self.cursor.execute("SELECT * FROM Event WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, eventstatusid, danceteamid, eventnumberid, eventperiodid, event_name):
        self.cursor.execute("INSERT INTO Event (eventstatusid, danceteamid, eventnumberid, eventperiodid, event_name) VALUES (?, ?, ?, ?, ?)",
                            (eventstatusid, danceteamid, eventnumberid, eventperiodid, event_name))
        self.conn.commit()


    def remove(self, eventid):
        self.cursor.execute("UPDATE Event SET IsDelete = 1 WHERE eventid=?", (eventid,))
        self.conn.commit()


    def update(self, eventid, eventstatusid, danceteamid, eventnumberid, eventperiodid, event_name):
        self.cursor.execute("UPDATE Event SET eventstatusid = ?, danceteamid = ?, eventnumberid = ?, eventperiodid= ?, event_name = ? WHERE eventid = ?",
                            (eventstatusid, danceteamid, eventnumberid, eventperiodid, event_name, eventid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()