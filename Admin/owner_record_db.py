import pyodbc

class OwnerRecordDB:
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
        self.cursor.execute("SELECT Owner.first_name AS 'Owner First Name', \
                                Owner.last_name AS 'Owner Last Name', \
                                Owner.phone AS 'Phone Number', \
                                Owner.email AS 'Email', \
                                CountryName.country_name As 'Country', \
                                StateName.state_name AS 'State', \
                                CityName.city_name AS 'City', \
                                StreetName.street_name AS 'Street Address', \
                                ZipcodeNumber.zipcode AS 'Zipcode' \
                                FROM Owner \
                                INNER JOIN Address ON Owner.addressid = Address.addressid \
                                INNER JOIN CountryName ON Address.countryid = CountryName.countryid \
                                INNER JOIN StreetName ON Address.streetid = StreetName.streetid \
                                INNER JOIN StateName ON Address.stateid = StateName.stateid \
                                INNER JOIN CityName ON Address.cityid = CityName.cityid \
                                INNER JOIN ZipcodeNumber ON Address.zipcodeid = ZipcodeNumber.zipcodeid \
                                WHERE Owner.IsDelete = 0 \
                                ORDER BY Owner.first_name")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()