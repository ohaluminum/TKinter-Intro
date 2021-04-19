import pyodbc

class VendorRecordDB:
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
                                CountryName.country_name AS 'Country', \
                                StateName.state_name AS 'State', \
                                CityName.city_name AS 'City', \
                                StreetName.street_name AS 'Street Name', \
                                ZipcodeNumber.zipcode AS 'Zipcode', \
                                Vendor.phone AS 'Phone Number', \
                                Vendor.email AS 'Email Address', \
                                VendorStatus.vendor_status AS 'Vendor Status' \
                                FROM Vendor \
                                INNER JOIN Address ON Vendor.addressid = Address.addressid \
                                INNER JOIN CountryName ON Address.countryid = CountryName.countryid \
                                INNER JOIN StateName ON Address.stateid = StateName.stateid \
                                INNER JOIN CityName  ON Address.cityid = CityName.cityid \
                                INNER JOIN StreetName ON Address.streetid = StreetName.streetid \
                                INNER JOIN ZipcodeNumber ON Address.zipcodeid = ZipcodeNumber.zipcodeid \
                                INNER JOIN VendorStatus ON Vendor.vendorstatusid = VendorStatus.vendorstatusid \
                                ORDER BY Vendor.first_name") #\
                                #WHERE Vendor.IsDelete = 0")

        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()