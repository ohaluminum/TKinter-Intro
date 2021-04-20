import pyodbc

class StudentCourseStatusRecordDB:
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
                            StudentCategory.student_category AS 'Student Category',  \
                            StudentCode.student_code AS 'Student Code',  \
                            StudentCourseStatus.student_course_status AS 'Student Course Status'  \
                            FROM StudentCourseStatus  \
                            INNER JOIN Student ON StudentCourseStatus.studentid = Student.studentid  \
                            INNER JOIN Course ON StudentCourseStatus.courseid = Course.courseid  \
                            INNER JOIN StudentCategory ON StudentCourseStatus.studentcategoryid = StudentCategory.studentcategoryid  \
                            INNER JOIN StudentCode ON StudentCourseStatus.studentcodeid = StudentCode.studentcodeid  \
                            WHERE StudentCourseStatus.IsDelete = 0  \
                            ORDER BY Student.first_name")
                                    
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()