import pyodbc

class StudentReviewDB:
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
        self.cursor.execute("SELECT * FROM StudentReview WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, student_review_comment, student_review_date):
        self.cursor.execute("INSERT INTO StudentReview (student_review_comment, student_review_date) VALUES (?, ?)",
                            (student_review_comment, student_review_date))
        self.conn.commit()


    def remove(self, studentreviewid):
        self.cursor.execute("UPDATE StudentReview SET IsDelete = 1 WHERE studentreviewid=?", (studentreviewid,))
        self.conn.commit()


    def update(self, studentreviewid, student_review_comment, student_review_date):
        self.cursor.execute("UPDATE StudentReview SET student_review_comment = ?, student_review_date = ? WHERE studentreviewid = ?",
                            (student_review_comment, student_review_date, studentreviewid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()