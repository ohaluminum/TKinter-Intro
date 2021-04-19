import pyodbc

class DanceTeamDB:
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
        self.cursor.execute("SELECT * FROM DanceTeam WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, dance_team):
        self.cursor.execute("INSERT INTO DanceTeam (dance_team) VALUES (?)", (dance_team,))
        self.conn.commit()


    def remove(self, danceteamid):
        self.cursor.execute("UPDATE DanceTeam SET IsDelete = 1 WHERE danceteamid=?", (danceteamid,))
        self.conn.commit()


    def update(self, danceteamid, dance_team):
        self.cursor.execute("UPDATE DanceTeam SET dance_team = ? WHERE danceteamid = ?", (dance_team, danceteamid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()