import pyodbc

class EquipmentDB:
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
        self.cursor.execute("SELECT equipmentid, vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price FROM Equipment WHERE IsDelete = 0")
        rows = self.cursor.fetchall()
        return rows
    

    def insert(self, vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price):
        self.cursor.execute("INSERT INTO Equipment (vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price) VALUES (?, ?, ?, ?, ?, ?)",
                            (vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price))
        self.conn.commit()


    def remove(self, equipmentid):
        self.cursor.execute("UPDATE Equipment SET IsDelete = 1 WHERE equipmentid=?", (equipmentid,))
        self.conn.commit()


    def update(self, equipmentid, vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price):
        self.cursor.execute("UPDATE equipment SET vendorid = ?, equipmenttypeid = ?, equipmentnumberid = ?, equipmentstatusid = ?, "
                            "equipment_name = ?, equipment_price = ? WHERE equipmentid = ?",
                            (vendorid, equipmenttypeid, equipmentnumberid, equipmentstatusid, equipment_name, equipment_price, equipmentid))
        self.conn.commit()


    def __del__(self):
        self.conn.close()

        
    
