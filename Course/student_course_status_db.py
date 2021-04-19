import pyodbc

class StudentCourseStatusDB:
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
        self.cursor.execute("SELECT * FROM StudentCourseStatus WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, studentid, courseid, studentcategoryid, studentcodedid, student_course_status):
        self.cursor.execute("INSERT INTO StudentCourseStatus (studentid, courseid, studentcategoryid, studentcodeid, "
                            "student_course_status) VALUES (?, ?, ?, ?, ?)",
                            (studentid, courseid, studentcategoryid, studentcodedid, student_course_status))
        self.conn.commit()


    def remove(self, studentcoursestatusid):
        self.cursor.execute("UPDATE StudentCourseStatus SET IsDelete = 1 WHERE studentcoursestatusid = ?", (studentcoursestatusid,))
        self.conn.commit()


    def update(self, studentcoursestatusid, studentid, courseid, studentcategoryid, studentcodeid, student_course_status):
        self.cursor.execute("UPDATE StudentCourseStatus SET studentid = ?, courseid = ?, studentcategoryid = ?, "
                            "studentcodeid = ?, student_course_status = ? WHERE studentcoursestatusid = ?",
                            (studentid, courseid, studentcategoryid, studentcodeid, student_course_status, studentcoursestatusid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()