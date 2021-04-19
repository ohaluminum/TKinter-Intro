import pyodbc

class EventStatusDB:
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
        self.cursor.execute("SELECT * FROM EventStatus WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, event_status, event_start_date, event_end_date):
        self.cursor.execute("INSERT INTO EventStatus (event_status, event_start_date, event_end_date) VALUES (?, ?, ?)",
                            (event_status, event_start_date, event_end_date))
        self.conn.commit()


    def remove(self, eventstatusid):
        self.cursor.execute("UPDATE EventStatus SET IsDelete = 1 WHERE eventstatusid=?", (eventstatusid,))
        self.conn.commit()


    def update(self, eventstatusid, event_status, event_start_date, event_end_date):
        self.cursor.execute("UPDATE EventStatus SET event_status = ?, event_start_date = ?, event_end_date = ? WHERE eventstatusid = ?",
                            (event_status, event_start_date, event_end_date, eventstatusid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()