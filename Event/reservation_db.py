import pyodbc

class ReservationDB:
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
        self.cursor.execute("SELECT * FROM Reservation WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, studentid, eventid, reservationnumberid, danceteamid, reservation_description, reservation_date):
        self.cursor.execute("INSERT INTO Reservation (studentid, eventid, reservationnumberid, danceteamid, reservation_description, reservation_date) VALUES (?, ?, ?, ?, ?, ?)",
                            (studentid, eventid, reservationnumberid, danceteamid, reservation_description, reservation_date))
        self.conn.commit()


    def remove(self, reservationid):
        self.cursor.execute("UPDATE Reservation SET IsDelete = 1 WHERE reservationid=?", (reservationid,))
        self.conn.commit()


    def update(self, reservationid, studentid, eventid, reservationnumberid, danceteamid, reservation_description, reservation_date):
        self.cursor.execute("UPDATE Reservation SET studentid = ?, eventid = ?, reservationnumberid = ?, danceteamid= ?, reservation_description = ?, reservation_date = ? WHERE reservationid = ?",
                            (studentid, eventid, reservationnumberid, danceteamid, reservation_description, reservation_date, reservationid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()