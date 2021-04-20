import pyodbc

class ReservationRecordDB:
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
                            ReservationNumber.reservation_number AS 'Reservation Number', \
                            DanceTeam.dance_team AS 'Dance Team', \
                            Event.event_name as 'Reservation For Event Name', \
                            Reservation.reservation_description AS 'Reservation Description', \
                            Reservation.reservation_date AS 'Reservation Date' \
                            FROM Reservation \
                            INNER JOIN Student On Reservation.studentid = Student.studentid \
                            INNER JOIN ReservationNumber ON Reservation.reservationnumberid = ReservationNumber.reservationnumberid \
                            INNER JOIN DanceTeam ON Reservation.danceteamid = DanceTeam.danceteamid \
                            INNER JOIN Event On Reservation.eventid = Event.eventid \
                            WHERE Reservation.IsDelete = 0 \
                            ORDER BY Reservation.reservationid")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()