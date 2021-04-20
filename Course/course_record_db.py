import pyodbc

class CourseRecordDB:
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
                            Course.course_name AS 'Course Name',  \
                            Genre.genre_type AS 'Course Genre',  \
                            CourseNumber.course_number AS 'Course Number',  \
                            Employee.first_name AS 'Instructor First Name', \
                            Employee.last_name AS 'Instructor Last Name', \
                            CoursePrice.course_price AS 'Course Price', \
                            Course.course_date AS 'Course Date',  \
                            Course.course_time AS 'Course Time'  \
                            FROM Course  \
                            INNER JOIN Student ON Course.studentid = Student.studentid  \
                            INNER JOIN Employee ON Course.employeeid = Employee.employeeid  \
                            INNER JOIN CourseNumber ON Course.coursenumberid = CourseNumber.coursenumberid  \
                            INNER JOIN Genre ON Course.genreid = Genre.genreid  \
                            INNER JOIN CoursePrice ON Course.coursepriceid = CoursePrice.coursepriceid  \
                            WHERE Course.IsDelete = 0  \
                            ORDER BY CourseNumber.course_number")
                                    
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()