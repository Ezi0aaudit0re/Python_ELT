"""
    This file contains the third part of the ETL project 
    We use threads and queue module in this part of the project 
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

# imports 
import queue
import threading
import sys

sys.path.append("../")

import Extract.CSVReaders.StockCSVReader as StockCSVReader
import Extract.Exceptions


# global variable 
stocks_rows = queue.Queue()
stocks_records = queue.Queue()

class Runnable():
    
    def __init__(self, id):
        self.id = id


    """
        This method makes the class a callable
    """
    def __call__(self):

        global stocks_rows, stock_records
        # run an infinite loop 
        while(True):
            # get from queue 
            try:
                # get the element from the queue
                row = stocks_rows.get(timeout=1)

                # the rows which are added to stocks_rows queue are already validated 
                # this validation is done in the row_to_record method in StockCSVReader class

                # add to the stocks_record queue
                stock_records.put(record)
            except Exception as e:
                # break out of the loop 
                break
        print("{worker_id} is working hard".format(worker_id=self.id))


class FastStocksCSVReader:
    
    def __init__(self, fname):
        self.fname = fname

    def load(self):
        global stocks_rows, stocks_records
        # use the already defined method in StockCSVReader
        records = StockCSVReader.StockCSVReader(self.fname).load()
        # add to the stocks_rows queue
        for record in records:
            stocks_rows.put(record)

        threads = []

        # create 4 new threads
        for i in range(4):
            new_thread = threading.Thread(target=Runnable("Worker {}".format(i)))
            # start the threds
            new_thread.start()
            threads.append(new_thread)

        # join all the threads
        for thread in threads:
            thread.join()

        new_list = []
        for record in iter(stocks_records.get()):
            new_list.append(record)

        return new_list


if __name__ == "__main__":
    records = FastStocksCSVReader("../CSV Files/StockValuations.csv").load()
    for record in records:
        print(record)


