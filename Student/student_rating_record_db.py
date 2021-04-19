import pyodbc

class StudentRatingRecordDB:
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
        self.cursor.execute("SELECT Student.first_name AS 'First Name', \
                            Student.last_name AS 'Last Name', \
                            Course.course_name AS 'Class Name', \
                            StudentCategory.student_category AS 'Student Category', \
                            StudentRating.rating_number AS 'Rating', \
                            StudentReview.student_review_comment AS 'Review Comments' \
                            FROM StudentRating \
                            INNER JOIN Student ON StudentRating.studentid = Student.studentid \
                            INNER JOIN Course ON StudentRating.courseid = Course.courseid \
                            INNER JOIN StudentCategory ON StudentRating.studentcategoryid = StudentCategory.studentcategoryid \
                            INNER JOIN StudentReview ON StudentRating.studentreviewid = StudentReview.studentreviewid \
                            ORDER BY StudentRating.rating_number") #\
                            #WHERE StudentRating.IsDelete = 0")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()