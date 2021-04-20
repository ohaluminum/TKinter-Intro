import pyodbc

class EmployeeRecordDB:
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
        self.cursor.execute("SELECT Employee.first_name AS 'First Name', \
                            Employee.last_name AS 'Last Name', \
                            Employee.phone AS 'Phone Number', \
                            Employee.email AS 'Email Address', \
                            StreetName.street_name AS 'Street', \
                            ZipcodeNumber.zipcode AS 'Zipcode', \
                            CityName.city_name AS 'City', \
                            StateName.state_name AS 'State', \
                            CountryName.country_name AS 'Country' \
                            FROM Employee \
                            INNER JOIN Address ON Address.addressid = Employee.addressid \
                            INNER JOIN StreetName ON Address.streetid = StreetName.streetid \
                            INNER JOIN ZipcodeNumber ON Address.zipcodeid = ZipcodeNumber.zipcodeid \
                            INNER JOIN CityName ON Address.cityid = CityName.cityid \
                            INNER JOIN StateName ON Address.stateid = StateName.stateid \
                            INNER JOIN CountryName ON Address.countryid = CountryName.countryid \
                            ORDER BY Address.addressid") #\
                            #WHERE Employee.IsDelete = 0")
                                
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()