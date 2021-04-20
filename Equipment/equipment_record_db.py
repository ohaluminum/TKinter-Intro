import pyodbc

class EquipmentRecordDB:
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
        self.cursor.execute("SELECT Vendor.first_name AS 'Vendor First Name', Vendor.last_name AS 'Vendor Last Name', \
                                Equipment.equipment_name AS 'Equipment Name', \
                                EquipmentType.equipment_type AS 'Equipment Type', \
                                EquipmentNumber.equipment_number AS 'Equipment Number', \
                                EquipmentStatus.equipment_status AS 'Equipment Condition', \
                                Equipment.equipment_price AS 'Equipment Price' \
                                FROM Equipment \
                                INNER JOIN Vendor ON Equipment.vendorid = Vendor.vendorid \
                                INNER JOIN EquipmentType ON Equipment.equipmenttypeid = EquipmentType.equipmenttypeid \
                                INNER JOIN EquipmentNumber ON Equipment.equipmentnumberid = EquipmentNumber.equipmentnumberid \
                                INNER JOIN EquipmentStatus ON Equipment.equipmentstatusid = EquipmentStatus.equipmentstatusid \
                                WHERE Equipment.IsDelete = 0 \
                                ORDER BY Vendor.first_name")

        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()