import pyodbc

class MerchandiseRecordDB:
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
        self.cursor.execute("SELECT Vendor.first_name AS 'Vendor First Name', \
                                Vendor.last_name AS 'Vendor Last Name', \
                                Merchandise.merchandise_name AS 'Merchandise Name', \
                                MerchandiseType.merchandise_type AS 'Merchandise Type', \
                                MerchandiseNumber.merchandise_number AS 'Merchandise Number', \
                                MerchandiseStatus.merchandise_status AS 'Merchandise Condition', \
                                Merchandise.merchandise_price AS 'Merchandise Price' \
                                FROM Merchandise \
                                INNER JOIN Vendor ON Merchandise.vendorid = Vendor.vendorid \
                                INNER JOIN MerchandiseType ON Merchandise.merchandisetypeid = MerchandiseType.merchandisetypeid \
                                INNER JOIN MerchandiseNumber ON Merchandise.merchandisenumberid = MerchandiseNumber.merchandisenumberid \
                                INNER JOIN MerchandiseStatus ON Merchandise.merchandisestatusid = MerchandiseStatus.merchandisestatusid \
                                ORDER BY Vendor.first_name") #\
                                #WHERE Merchandise.IsDelete = 0")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()