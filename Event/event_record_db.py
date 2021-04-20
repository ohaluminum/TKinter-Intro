import pyodbc

class EventRecordDB:
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
        self.cursor.execute("SELECT Event.event_name AS 'Event Name', \
                            EventStatus.event_status AS 'Event Status', \
                            EventStatus.event_start_date AS 'Event Start Date', \
                            EventStatus.event_end_date AS 'Event Start Date', \
                            DanceTeam.dance_team AS 'Dance Team', \
                            EventNumber.event_number as 'Event Number', \
                            EventPeriod.event_period as 'Event Period' \
                            FROM Event \
                            INNER JOIN EventStatus On Event.eventstatusid = Event.eventstatusid \
                            INNER JOIN DanceTeam ON Event.danceteamid = DanceTeam.danceteamid \
                            INNER JOIN EventNumber ON Event.eventnumberid = EventNumber.eventnumberid \
                            INNER JOIN EventPeriod ON Event.eventperiodid = EventPeriod.eventperiodid \
                            WHERE Event.IsDelete = 0 \
	                        ORDER BY Event.eventid")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()