import pyodbc

class MerchandiseDB:
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
        self.cursor.execute("SELECT merchandiseid, vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid, merchandise_name, merchandise_price FROM Merchandise WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid, merchandise_name, merchandise_price):
        self.cursor.execute("INSERT INTO Merchandise (vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid,"
                            "merchandise_name, merchandise_price) VALUES (?, ?, ?, ?, ?, ?)",
                            (vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid, merchandise_name, merchandise_price))
        self.conn.commit()
        

    def remove(self, merchandiseid):
        self.cursor.execute("UPDATE Merchandise SET IsDelete = 1 WHERE merchandiseid=?", (merchandiseid,))
        self.conn.commit()


    def update(self, merchandiseid, vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid, merchandise_name, merchandise_price):
        self.cursor.execute("UPDATE Merchandise SET vendorid = ?, merchandisetypeid = ?, merchandisenumberid = ?, merchandisestatusid = ?, "
                            "merchandise_name = ?, merchandise_price = ? WHERE merchandiseid = ?",
                            (vendorid, merchandisetypeid, merchandisenumberid, merchandisestatusid, merchandise_name, merchandise_price, merchandiseid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()