import mysql.connector

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='rahul',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connection Error')

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        select distinct(Destination) from flights
        union
        select distinct(source) from flights;
        """)
        data = self.mycursor.fetchall()

        print(data)

        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights
        WHERE Source = '{}' AND Destination = '{}'       
        """.format(source, destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []
        self.mycursor.execute("""
        select Airline, count(*) from flights
        GROUP BY Airline
        """)
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency1 = []
        self.mycursor.execute("""
        select Airline, count(*) from flights
        GROUP BY Airline
        order by count(*) desc
        """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city, frequency1

    def daily_frquency(self):
        date = []
        frequency2 = []
        self.mycursor.execute("""
        select Date_of_journey, count(*) from flights
        group by Date_of_journey
        """)
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency2.append(item[1])

        return date, frequency2


