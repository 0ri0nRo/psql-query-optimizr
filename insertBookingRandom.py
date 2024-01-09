import psycopg2
import random
import time
from datetime import datetime

hostname = 'localhost'
database = 'exercises'
username = 'postgres'
pwd = '1234'
port_id = 5432
cur = None
conn = None

class insertBookings():


    def __init__(self):
        self.conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )
        
        
    def maxBookid(self):
        #prendo l'ultimo booid inserito
        try:
            self.cur = self.conn.cursor()
            query = """select b.bookid
                        from cd.bookings b
                        where b.bookid = (select max(b.bookid) from cd.bookings b)
                    """
            self.cur.execute(query)
            max = self.cur.fetchone()
            self.conn.commit
        
            return max[0]
        
        except Exception as error:
            print(error)
 

    def insertValuesIntoBooking(self, n):
        try:
            max = self.maxBookid()
            while n >= max:
                new_max_to_insert = max + 1
                #random_facid = random.randrange(0, 8)	
                #random_memid = random.randrange(0, 36)	
                timestamp = self.randomDate("20-01-2013 13:30:00", "31-12-2023 04:50:34")
                random_slots = random.randrange(0, 14)	

                query = """
                INSERT INTO cd.bookings VALUES(%s, %s, %s, %s, %s)
                """
                values = (new_max_to_insert, 1, 1, timestamp, random_slots)
                self.cur.execute(query, values)
                self.conn.commit()
                max = new_max_to_insert
                print("inserito")
            return "ok", 200


        except Exception as error:
            print(error)
    
    def randomDate(self, start, end):
        frmt = '%d-%m-%Y %H:%M:%S'

        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))

        ptime = stime + random.random() * (etime - stime)
        dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
        
        return dt

d = insertBookings()
print(d.insertValuesIntoBooking(1000000))


