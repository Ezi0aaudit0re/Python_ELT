__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import sys
import sqlite3
from collections import deque, defaultdict

sys.path.append("../")

from Extract.Records import Baseball, Stock
from Extract.Exceptions import BadDataError, NoFileError
from Helper.create_connection import createConnection
from Extract.CSVReaders import AbstractCsvReader, BaseballCSVReader, StockCSVReader

"""
    This is an Abstract class which is used to connect to the database
"""
class AbstractDAO: 
    """
        Constructor for the class
        :param: db_name -> The name of the database to connect to 
    """
    def __init__(self, db_name):
        self.db_name = db_name

    """
        This method is implemented in the child class
    """
    def insert_records(self, records):
        raise NotImplementedError("This method needs to be implemented in the child class")

    """
        This method is implemented in the child class
    """
    def select_all(self):
        raise NotImplementedError("This method needs to be implemented in the child class")

    """
        This method is used to connect to the database
    """
    def connect(self):
        with sqlite3.connect(self.db_name) as conn:
            return conn
            # if we return conn here the connection gets closed that is why we set it equal to instance variable


"""
    This class is related to baseball data
"""
class BaseballStatsDAO(AbstractDAO):

    """
        Instantiate method calls __init__ method of the parent class
    """
    def __init__(self, db_name):
        super().__init__(db_name)

    """
        This methods inserts the records in the database
        :param: records -> A list of all the baseball stats records
    """
    def insert_records(self, records):
        try:
            conn = super().connect()
            # create a cursor
            cursor = conn.cursor()
            for record in records:
                query = "INSERT INTO baseball_stats VALUES (?, ?, ?, ?)"
                cursor.execute(query, (getattr(record, "_name"), getattr(record, "_g_played"), getattr(record, "_avg"), getattr(record, "_salary")))

            conn.commit()
            conn.close()

        except sqlite3.OperationalError:
            print("The table you are trying to insert to doesnot exist please run the 'Nagpal_Aman_create_db.py' first")
            exit(1)
        
        except Exception as e:
            print(str(e))

    """
        this methods gets all the rows from the database
        retruns in the form of deque 
        :return: new_deque -> deque of rows in the database
    """
    def select_all(self):
        try:
            # connect to the databse
            conn = super().connect()
            # create a cursor from the connection
            cursor = conn.cursor()
            # create an empty deque
            new_deque = deque()
            # get the data from the tables
            cursor.execute("SELECT * FROM baseball_stats")
            datas = cursor.fetchall()
            # populate the deque with the data
            # order - name, slaray, games_played, avg
            for data in datas:
                new_deque.append(Baseball.BaseballRecord(data[0], data[3], data[1], data[2]))
            # close the connection
            conn.close()
            return new_deque

        except Exception as e:
            print(str(e))



    """
        This method creates a dictionary of the data in the database based on 
        {batting_avg: AVG of salaries}
        :param: deck -> The deque of data that we get from the database
    """
    def printData(self, deck):

        data = {}
        occurance= {} # this dict keep tracks the number of times a batting avg has occired

        # this loop would add the salaries with similar batting average 
        for d in deck:
            avg = getattr(d, "_avg")
            if avg in data.keys():
                data[avg] += getattr(d, "_salary")
                occurance[avg] += 1
            else:
                data[avg] = getattr(d, "_salary")
                occurance[avg] = 1

        # now we find the avg of slaray using the occurance dict
        for k, v in occurance.items():
            data[k] = data[k]/v

        # sort the data according to keys
        sorted_data = sorted(data.items(), key= lambda x:x[0])

        # print the data in ordered form
        for x in sorted_data:
            print(x[0], x[1])


                

           

            



class StockStatsDAO(AbstractDAO):

    """
        This method initializes the object
        Calls the parent __init__ method with the name of the databse
    """
    def __init__(self, db_name):
        super().__init__(db_name)

    """
        This method inserts the records in the database
        :param: records -> The stock record to insert in the database
    """
    def insert_records(self, records):
        try:
            conn = super().connect();
            cursor = conn.cursor()
            #insert every record into the database
            for record in records:
                query = "Insert into stock_stats values (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (getattr(record, "_company_name"), getattr(record, "_name"), getattr(record, "_exchange_country"), getattr(record, "_price"), getattr(record, "_exchange_rate"), getattr(record, "_shares_outstanding"), getattr(record, "_net_income"), getattr(record, "_market_value_usd"), getattr(record, "_pe_ratio")))

            # commit the changes and then close the databse
            conn.commit()
            conn.close()

        except sqlite3.OperationalError:
            print("The table you are trying to insert to doesnot exist please run the 'Nagpal_Aman_create_db.py' first")
            exit(1)
        
        except Exception as e:
            print(str(e))


    """
        This method gets rows from the stocks.db database
        :return: a deque of rows from the db
    """
    def select_all(self):
        try:
            #establist a connection
            conn = super().connect()
            # create a cursor
            cursor = conn.cursor()
            stocks_deque = deque()
            cursor.execute("SELECT * FROM stock_stats")
            datas = cursor.fetchall()
            # close the connection
            conn.close()
            for data in datas:
                stocks_deque.append(Stock.StockRecord(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
            
            return stocks_deque
        except Exception as e:
            print("An exception has occured in the select_all method in stocks class")
            print(str(e))


    """
        This method prints the number of tickers basaed on the exchange country using a dict
        :param: deck -> the dequee of data from the database stocks.db
    """
    def printData(self, deck):
        
        # dict to store the data
        data = {}
        
        # loop through the rows 
        for d in deck:
            exchange_country = getattr(d, "_exchange_country")
            if exchange_country in data.keys():
                data[exchange_country] += 1
            else:
                data[exchange_country] = 1

        sorted_data = sorted(data.items(), key=lambda x: x[0])

        for data in sorted_data:
            print(data[0], data[1])





if __name__ == "__main__":
    print("--------------- Baseball Data ----------------------\n")
    # add baseball records to the database
    baseball_records = BaseballCSVReader.BaseballCSVReader("../CSV Files/MLB2008.csv").load()
    baseball = BaseballStatsDAO("baseball.db")
    baseball.insert_records(baseball_records)
    deck = baseball.select_all()
    baseball.printData(deck)

    print("--------------- Stock Data ----------------------\n")
    # add stock records to the databse after extracting from csv file
    stock_records = StockCSVReader.StockCSVReader("../CSV Files/StockValuations.csv").load()
    stock = StockStatsDAO("stocks.db")
    stock.insert_records(stock_records)
    deck = stock.select_all()
    stock.printData(deck)
 

        
