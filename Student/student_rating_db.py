import pyodbc

class StudentRatingDB:
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
        self.cursor.execute("SELECT * FROM StudentRating WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, studentid, studentcategoryid, courseid, studentreviewid, rating_number):
        self.cursor.execute("INSERT INTO StudentRating (studentid, studentcategoryid, courseid, studentreviewid, rating_number) VALUES (?, ?, ?, ?, ?)",
                            (studentid, studentcategoryid, courseid, studentreviewid, rating_number))
        self.conn.commit()


    def remove(self, ratingid):
        self.cursor.execute("UPDATE StudentRating SET IsDelete = 1 WHERE ratingid=?", (ratingid,))
        self.conn.commit()


    def update(self, ratingid, studentid, studentcategoryid, courseid, studentreviewid, rating_number):
        self.cursor.execute("UPDATE StudentRating SET studentid = ?, studentcategoryid = ?, courseid = ?, "
                            "studentreviewid = ?, rating_number = ? WHERE ratingid = ?",
                            (studentid, studentcategoryid, courseid, studentreviewid, rating_number, ratingid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()